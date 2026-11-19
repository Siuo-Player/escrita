"""
Parser e utilitários de extração de dados narrativos para testes automáticos de história.
Analisa os ficheiros em canon/ e episodes/season-1/ para verificar:
- Linearidade temporal e correspondência de calendário (2009/2010).
- Estrutura multi-trama (>= 3 tramas por episódio, com >= 1 principal e >= 2 secundárias).
- Introdução orgânica e individualizada de personagens.
- Rastreamento e backpropagation de adereços/pistas.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

# Raiz do repositório
REPO_ROOT = Path(__file__).resolve().parent.parent

# Dicionário de meses em inglês/português para 2009
MONTHS = {
    "january": 1, "janeiro": 1, "jan": 1,
    "february": 2, "fevereiro": 2, "feb": 2, "fev": 2,
    "march": 3, "março": 3, "marco": 3, "mar": 3,
    "april": 4, "abril": 4, "apr": 4, "abr": 4,
    "may": 5, "maio": 5,
    "june": 6, "junho": 6, "jun": 6,
    "july": 7, "julho": 7, "jul": 7,
    "august": 8, "agosto": 8, "aug": 8, "ago": 8,
    "september": 9, "setembro": 9, "sep": 9, "set": 9,
    "october": 10, "outubro": 10, "oct": 10, "out": 10,
    "november": 11, "novembro": 11, "nov": 11,
    "december": 12, "dezembro": 12, "dec": 12, "dez": 12,
}

DAYS_OF_WEEK_PT = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
DAYS_OF_WEEK_EN = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def parse_date_string(text: str, default_year: int = 2009) -> Optional[datetime]:
    """Tenta converter strings como '7 September 2009', '2009-09-07', '7 de Setembro' em objeto datetime."""
    text = text.strip()
    
    # Formato ISO YYYY-MM-DD
    iso_match = re.search(r'\b(2009|2010|2011|2012)-(\d{2})-(\d{2})\b', text)
    if iso_match:
        y, m, d = int(iso_match.group(1)), int(iso_match.group(2)), int(iso_match.group(3))
        return datetime(y, m, d)
        
    # Formato DD [de] Mês [de] [YYYY]
    date_match = re.search(r'\b(\d{1,2})\s+(?:de\s+)?([A-Za-zç]+)(?:\s+(?:de\s+)?(2009|2010|2011|2012))?\b', text, re.IGNORECASE)
    if date_match:
        day = int(date_match.group(1))
        month_name = date_match.group(2).lower()
        year = int(date_match.group(3)) if date_match.group(3) else default_year
        if month_name in MONTHS:
            try:
                return datetime(year, MONTHS[month_name], day)
            except ValueError:
                return None
    return None

def extract_episode_metadata(filepath: Path) -> Dict[str, Any]:
    """Extrai tramas, datas, alterações de estado persistente e menções a personagens de um episódio."""
    content = filepath.read_text(encoding='utf-8')
    data = {
        "file": filepath.name,
        "path": filepath,
        "title": "",
        "story_window": "",
        "start_date": None,
        "end_date": None,
        "threads": [],
        "main_threads": [],
        "minor_threads": [],
        "dates_in_file": [],
        "persistent_state_changes": [],
        "character_mentions": set(),
        "props_and_clues": []
    }
    
    lines = content.splitlines()
    
    # Extrair título
    for line in lines:
        if line.startswith("# "):
            data["title"] = line.replace("# ", "").strip()
            break
            
    # Extrair Story window
    window_match = re.search(r'\*\*Story window:\*\*\s*(.+)', content, re.IGNORECASE)
    if not window_match:
        window_match = re.search(r'##\s*Story window\s*\n+\*\*([^\*]+)\*\*', content, re.IGNORECASE)
    if window_match:
        data["story_window"] = window_match.group(1).strip()
        # Encontrar datas no story window
        dates = []
        for part in re.split(r'–|-|to|até', data["story_window"]):
            parsed = parse_date_string(part)
            if parsed:
                dates.append(parsed)
        if len(dates) >= 2:
            data["start_date"] = min(dates)
            data["end_date"] = max(dates)
        elif len(dates) == 1:
            data["start_date"] = dates[0]
            
    # Extrair Persistent threads
    in_threads = False
    current_thread = None
    for line in lines:
        if re.match(r'^##\s+Persistent threads', line, re.IGNORECASE) or re.match(r'^##\s+Threads', line, re.IGNORECASE):
            in_threads = True
            continue
        if in_threads and line.startswith("## ") and not line.startswith("### "):
            in_threads = False
            break
        if in_threads:
            thread_match = re.match(r'^###\s+([A-Z0-9]+)\s*—\s*(.+)', line)
            if thread_match:
                tag = thread_match.group(1).strip()
                desc = thread_match.group(2).strip()
                thread_info = {"tag": tag, "desc": desc, "type": "minor"}
                # Avaliar se é trama principal (ex: Nathan / game, ou explicitamente rotulado)
                if any(k in desc.lower() for k in ["game", "principal", "main", "jogo", "pesquisa"]):
                    thread_info["type"] = "main"
                    data["main_threads"].append(thread_info)
                else:
                    data["minor_threads"].append(thread_info)
                data["threads"].append(thread_info)

    # Extrair cabeçalhos com datas
    date_header_regex = re.compile(r'^###+\s+(\d{1,2}\s+(?:de\s+)?[A-Za-zç]+(?:\s+\d{4})?)\b', re.IGNORECASE)
    for line in lines:
        dm = date_header_regex.search(line)
        if dm:
            parsed = parse_date_string(dm.group(1))
            if parsed:
                data["dates_in_file"].append((parsed, line.strip()))

    # Extrair Persistent state changes
    state_change_regex = re.compile(r'(?:persistent state change|alteração de estado|estado persistente):\s*(.+)', re.IGNORECASE)
    for line in lines:
        sm = state_change_regex.search(line)
        if sm:
            data["persistent_state_changes"].append(sm.group(1).strip())
            
    # Extrair menções de personagens
    canon_characters = ["Alex", "Claire", "Phil", "Luke", "Haley", "Jay", "Gloria", "Manny", "Mitchell", "Cameron"]
    for char in canon_characters:
        if re.search(r'\b' + char + r'\b', content, re.IGNORECASE):
            data["character_mentions"].add(char.lower())
            
    # Extrair pistas / props marcadas
    prop_regex = re.compile(r'\[(PROP|CLUE|PISTA|ADEREÇO):\s*([^\]]+)\]', re.IGNORECASE)
    for match in prop_regex.finditer(content):
        data["props_and_clues"].append({
            "type": match.group(1).upper(),
            "detail": match.group(2).strip(),
            "line": match.group(0)
        })

    return data
