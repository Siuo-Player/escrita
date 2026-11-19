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
    iso_match = re.search(r'\b(20\d{2})-(\d{2})-(\d{2})\b', text)
    if iso_match:
        y, m, d = int(iso_match.group(1)), int(iso_match.group(2)), int(iso_match.group(3))
        try:
            return datetime(y, m, d)
        except ValueError:
            return None
        
    # Formato DD [de] Mês [de] [YYYY]
    date_match = re.search(r'\b(\d{1,2})\s+(?:de\s+)?([A-Za-zç]+)(?:\s+(?:de\s+)?(20\d{2}))?\b', text, re.IGNORECASE)
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

def parse_heading_date_range(heading: str, default_year: int = 2009):
    """Extrai a data visível de um heading, aceitando datas simples e intervalos no mesmo mês.

    Exemplos: '### 7 September', '### 2–3 October', '### 22 de Outubro'.
    Devolve (início, fim) ou None quando o heading não contém uma data suportada.
    """
    visible_heading = re.sub(r"<!--.*?-->", "", heading).strip()
    match = re.match(
        r"^\s*#{1,6}\s+(\d{1,2})(?:\s*[–-]\s*(\d{1,2}))?\s+(?:de\s+)?([A-Za-zç]+)(?:\s+(?:de\s+)?(20\d{2}))?\b",
        visible_heading,
        re.IGNORECASE,
    )
    if not match:
        return None

    day_start = int(match.group(1))
    day_end = int(match.group(2)) if match.group(2) else day_start
    month_name = match.group(3).lower()
    year = int(match.group(4)) if match.group(4) else default_year
    month = MONTHS.get(month_name)
    if month is None:
        return None

    try:
        return datetime(year, month, day_start), datetime(year, month, day_end)
    except ValueError:
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
        win = data["story_window"]
        
        # Padrão multi-mês: ex: '19 November – 05 December 2009'
        m_multi = re.search(r'(\d{1,2})\s+([A-Za-zç]+)\s*(?:–|-)\s*(\d{1,2})\s+([A-Za-zç]+)(?:\s+(?:de\s+)?(20\d{2}))?', win, re.IGNORECASE)
        # Padrão mesmo mês: ex: '7–30 September 2009', '1–15 October 2009'
        m_single = re.search(r'(\d{1,2})\s*(?:–|-)\s*(\d{1,2})\s+(?:de\s+)?([A-Za-zç]+)(?:\s+(?:de\s+)?(20\d{2}))?', win, re.IGNORECASE)
        
        if m_multi and m_multi.group(2).lower() in MONTHS and m_multi.group(4).lower() in MONTHS:
            y = int(m_multi.group(5)) if m_multi.group(5) else 2009
            m1 = MONTHS[m_multi.group(2).lower()]
            d1 = int(m_multi.group(1))
            m2 = MONTHS[m_multi.group(4).lower()]
            d2 = int(m_multi.group(3))
            data["start_date"] = datetime(y, m1, d1)
            data["end_date"] = datetime(y, m2, d2)
        elif m_single and m_single.group(3).lower() in MONTHS:
            y = int(m_single.group(4)) if m_single.group(4) else 2009
            m = MONTHS[m_single.group(3).lower()]
            d1 = int(m_single.group(1))
            d2 = int(m_single.group(2))
            data["start_date"] = datetime(y, m, d1)
            data["end_date"] = datetime(y, m, d2)
        else:
            # Encontrar datas no story window por partes
            dates = []
            for part in re.split(r'–|-|to|até', win):
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

def parse_event_registry_content(content: str):
    """Parseia a tabela de eventos sem descartar silenciosamente linhas malformadas.

    Retorna (eventos, problemas). Cada linha com um token EVT- é tratada como
    uma linha de dados candidata e tem de respeitar as nove colunas canónicas.
    """
    events = []
    issues = []

    for line_number, raw_line in enumerate(content.splitlines(), start=1):
        line = raw_line.strip()
        if not line.startswith("|") or "EVT-" not in line:
            continue

        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 9:
            issues.append(
                f"Linha {line_number}: esperado exatamente 9 colunas; encontradas {len(parts)}."
            )
            continue

        id_text = parts[0].strip("*` ")
        if not re.fullmatch(r"EVT-\d{3}", id_text):
            issues.append(
                f"Linha {line_number}: Event ID inválido na primeira coluna: {parts[0]!r}."
            )
            continue

        empty_columns = [
            index + 1 for index, value in enumerate(parts[1:], start=1) if not value
        ]
        if empty_columns:
            issues.append(
                f"Linha {line_number} ({id_text}): colunas obrigatórias vazias: {empty_columns}."
            )

        date_raw = parts[1].replace("*", "").strip()
        ep_raw = parts[2].replace("*", "").strip()
        location = parts[3].strip()
        characters = [character.strip() for character in parts[4].split(",") if character.strip()]
        trigger = parts[5].strip()
        action = parts[6].strip()
        result = parts[7].strip()
        dep_docs = [doc.strip().strip("`") for doc in parts[8].split(",") if doc.strip()]

        # O formato atual permite datas ISO simples e intervalos no mesmo mês:
        # 2009-09-14 ou 2009-09-14/15.
        iso_match = re.search(
            r"\b(20\d{2})-(\d{2})-(\d{2})(?:/(\d{1,2}))?\b",
            date_raw,
        )
        dt = None
        date_end = None
        if iso_match:
            year, month, day = (int(iso_match.group(index)) for index in (1, 2, 3))
            try:
                dt = datetime(year, month, day)
                date_end = (
                    datetime(year, month, int(iso_match.group(4)))
                    if iso_match.group(4)
                    else dt
                )
            except ValueError:
                dt = None
                date_end = None

        if dt is None or date_end is None:
            issues.append(
                f"Linha {line_number} ({id_text}): data ISO inválida ou não suportada: {date_raw!r}."
            )

        weekday_range_match = re.search(r"\(([A-Za-z]+)-([A-Za-z]+)", date_raw)
        weekday_match = re.search(r"\(([A-Za-z]+)", date_raw)
        declared_weekday = weekday_match.group(1) if weekday_match else ""
        declared_weekday_end = (
            weekday_range_match.group(2) if weekday_range_match else declared_weekday
        )
        if not declared_weekday:
            issues.append(
                f"Linha {line_number} ({id_text}): dia da semana não declarado em {date_raw!r}."
            )

        events.append({
            "id": id_text,
            "line": line_number,
            "date_raw": date_raw,
            "date": dt,
            "date_end": date_end,
            "declared_weekday": declared_weekday,
            "declared_weekday_end": declared_weekday_end,
            "episode": ep_raw,
            "location": location,
            "characters": characters,
            "trigger": trigger,
            "action": action,
            "result": result,
            "dependent_docs": dep_docs,
        })

    return events, issues


def extract_events_from_registry() -> List[Dict[str, Any]]:
    """Extrai os eventos canónicos do EVENT_REGISTRY.md."""
    registry_file = REPO_ROOT / "canon" / "narrative" / "EVENT_REGISTRY.md"
    if not registry_file.exists():
        return []

    content = registry_file.read_text(encoding="utf-8")
    events, _issues = parse_event_registry_content(content)
    return events

def extract_props_from_registry() -> List[Dict[str, Any]]:
    """Extrai os adereços e pistas registados a partir de PROP_AND_CLUE_REGISTRY.md."""
    registry_file = REPO_ROOT / "canon" / "narrative" / "PROP_AND_CLUE_REGISTRY.md"
    if not registry_file.exists():
        return []
        
    content = registry_file.read_text(encoding='utf-8')
    props = []
    
    for line in content.splitlines():
        line = line.strip()
        if not line.startswith("|") or not any(k in line for k in ["PROP-", "CLUE-"]):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 6:
            continue
            
        id_match = re.search(r'(PROP|CLUE)-\d+', parts[0])
        if not id_match:
            continue
            
        prop_id = id_match.group(0)
        name = parts[1].replace("*", "").strip()
        genesis_raw = parts[2]
        background_raw = parts[3]
        payoff_raw = parts[4]
        status = parts[5].strip()
        
        # Extrair episódio de génese
        gen_ep_match = re.search(r'EP\d+', genesis_raw)
        genesis_ep = gen_ep_match.group(0) if gen_ep_match else ""
        
        # Extrair episódios de payoff
        payoff_eps = re.findall(r'EP\d+', payoff_raw)
        
        props.append({
            "id": prop_id,
            "name": name,
            "genesis_raw": genesis_raw,
            "genesis_ep": genesis_ep,
            "background_raw": background_raw,
            "payoff_raw": payoff_raw,
            "payoff_eps": payoff_eps,
            "status": status
        })
        
    return props
