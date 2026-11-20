"""
Testes automatizados para a integridade da cronologia multitemporadas e arquitetura global:
- Validação determinística das idades das personagens calculadas a partir das datas canónicas de nascimento.
- Validação da definição formal e unívoca da coordenada temporal t no intervalo [0.0, 1.0] (2009-09-07 a 2021-09-07).
- Verificação dos domínios explícitos de autoridade SSOT entre SERIES_GLOBAL_ARCHITECTURE e MULTI_SEASON_CHRONOLOGY_MAP.
- Verificação do enquadramento histórico real de 2020–2021 (COVID-19) e integração dos marcadores WD.
"""

import unittest
import re
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
ARCH_FILE = REPO_ROOT / "canon" / "narrative" / "SERIES_GLOBAL_ARCHITECTURE.md"
MAP_FILE = REPO_ROOT / "canon" / "timeline" / "MULTI_SEASON_CHRONOLOGY_MAP.md"
WD_REGISTRY = REPO_ROOT / "canon" / "narrative" / "WORLD_DIFFERENCE_REGISTRY.md"

# Datas de nascimento canónicas
BIRTHDATES = {
    "Nathan": date(1996, 9, 7),
    "Alex": date(1997, 1, 14),
    "Haley": date(1993, 12, 10),
    "Luke": date(1998, 11, 28),
    "Manny": date(1999, 1, 15),
}

# Períodos canónicos das temporadas (Início e Fim do ciclo letivo / civil)
# Os ciclos letivos e temporadas iniciam canonicamente em setembro com o aniversário de Nathan (07/09)
SEASON_PERIODS = {
    "S01": (date(2009, 9, 7), date(2010, 6, 25)),
    "S02": (date(2010, 9, 7), date(2011, 6, 24)),
    "S03": (date(2011, 9, 7), date(2012, 6, 22)),
    "S04": (date(2012, 9, 7), date(2013, 6, 21)),
    "S05": (date(2013, 9, 7), date(2014, 6, 20)),
    "S06": (date(2014, 9, 7), date(2015, 6, 19)),
    "S07": (date(2015, 9, 7), date(2016, 6, 17)),
    "S08": (date(2016, 9, 7), date(2017, 6, 16)),
    "S09": (date(2017, 9, 7), date(2018, 6, 15)),
    "S10": (date(2018, 9, 7), date(2019, 6, 14)),
    "S11+": (date(2019, 9, 7), date(2021, 9, 7)),
}

def calculate_age(birthdate: date, target_date: date) -> int:
    """Calcula a idade exata em anos completos numa determinada data gregoriana."""
    years = target_date.year - birthdate.year
    if (target_date.month, target_date.day) < (birthdate.month, birthdate.day):
        years -= 1
    return years

def expected_season_age_str(birthdate: date, start_date: date, end_date: date) -> str:
    """Gera a string esperada de idade para uma temporada (ex: '13 anos' ou '12–13 anos')."""
    age_start = calculate_age(birthdate, start_date)
    age_end = calculate_age(birthdate, end_date)
    if age_start == age_end:
        return f"{age_start} anos"
    else:
        return f"{age_start}–{age_end} anos"


class TestMultiSeasonChronology(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.arch_text = ARCH_FILE.read_text(encoding="utf-8") if ARCH_FILE.exists() else ""
        cls.map_text = MAP_FILE.read_text(encoding="utf-8") if MAP_FILE.exists() else ""
        cls.wd_text = WD_REGISTRY.read_text(encoding="utf-8") if WD_REGISTRY.exists() else ""

    def test_chronology_files_exist(self):
        """Os ficheiros centrais da arquitetura multitemporadas devem existir no repositório."""
        self.assertTrue(ARCH_FILE.is_file(), "canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md deve existir.")
        self.assertTrue(MAP_FILE.is_file(), "canon/timeline/MULTI_SEASON_CHRONOLOGY_MAP.md deve existir.")

    def test_ssot_authority_domains_are_explicit_and_reciprocal(self):
        """Garante que cada documento define o seu domínio explícito de autoridade e referencia o outro."""
        # SERIES_GLOBAL_ARCHITECTURE governa estrutura dramática e causalidade
        self.assertIn("AUTHORITATIVE DRAMATIC ARCHITECTURE", self.arch_text)
        self.assertIn("MULTI_SEASON_CHRONOLOGY_MAP.md", self.arch_text)
        
        # MULTI_SEASON_CHRONOLOGY_MAP governa datas, idades e calendários
        self.assertIn("AUTHORITATIVE CHRONOLOGICAL INDEX", self.map_text)
        self.assertIn("SERIES_GLOBAL_ARCHITECTURE.md", self.map_text)

    def test_formal_definition_of_t_is_consistent_and_monotonic(self):
        """Verifica se t está formalmente definido no calendário real de 2009-09-07 a 2021-09-07."""
        t_start = date(2009, 9, 7)
        t_quarter = date(2012, 9, 7)
        t_mid = date(2015, 9, 7)
        t_three_quarter = date(2018, 9, 7)
        t_end = date(2021, 9, 7)
        
        total_days = (t_end - t_start).days
        self.assertEqual(total_days, 4383, "O intervalo total de 12 anos civis (com anos bissextos) deve ter 4383 dias.")
        
        # Verificar que os documentos definem t=0.0 em 2009 e t=1.0 em Setembro de 2021
        self.assertIn("2009-09-07", self.map_text)
        self.assertIn("2021-09-07", self.map_text)
        self.assertIn("t = 1.0", self.map_text)
        
        # Verificar que a arquitetura global não desloca o ponto final para 2020
        self.assertNotIn("Junho de 2020 em diante ($t=1.0$)", self.arch_text)
        self.assertIn("Setembro de 2021", self.arch_text)

    def test_character_ages_per_season_match_canonical_birthdates(self):
        """Compara matematicamente as idades declaradas na tabela do mapa cronológico com as datas de nascimento."""
        # Extrair linhas da tabela de MULTI_SEASON_CHRONOLOGY_MAP.md
        # Formato: | **S01** | Set 2009 – Jun 2010 | **13 anos** | **12–13 anos** | 15–16 anos | 10–11 anos | ...
        for line in self.map_text.splitlines():
            line = line.strip()
            if not line.startswith("|") or not any(line.startswith(f"| **{s}") for s in SEASON_PERIODS.keys()):
                continue
            
            cells = [c.strip() for c in line.strip("|").split("|")]
            season_code_match = re.search(r"S\d{2}\+?", cells[0])
            self.assertIsNotNone(season_code_match)
            season_code = season_code_match.group(0)
            
            start_date, end_date = SEASON_PERIODS[season_code]
            
            # Idades no texto
            nathan_cell = cells[2].replace("*", "")
            alex_cell = cells[3].replace("*", "")
            haley_cell = cells[4].replace("*", "")
            luke_cell = cells[5].replace("*", "")
            
            # Idades esperadas calculadas matematicamente
            exp_nathan = expected_season_age_str(BIRTHDATES["Nathan"], start_date, end_date)
            exp_alex = expected_season_age_str(BIRTHDATES["Alex"], start_date, end_date)
            exp_haley = expected_season_age_str(BIRTHDATES["Haley"], start_date, end_date)
            exp_luke = expected_season_age_str(BIRTHDATES["Luke"], start_date, end_date)
            
            with self.subTest(season=season_code):
                self.assertIn(exp_nathan, nathan_cell, f"{season_code}: Idade de Nathan deve ser {exp_nathan}, recebido: '{nathan_cell}'.")
                self.assertIn(exp_alex, alex_cell, f"{season_code}: Idade de Alex deve ser {exp_alex}, recebido: '{alex_cell}'.")
                self.assertIn(exp_haley, haley_cell, f"{season_code}: Idade de Haley deve ser {exp_haley}, recebido: '{haley_cell}'.")
                self.assertIn(exp_luke, luke_cell, f"{season_code}: Idade de Luke deve ser {exp_luke}, recebido: '{luke_cell}'.")

    def test_nathan_is_25_at_the_final_scene(self):
        """Garante que na cena final de encerramento em Setembro de 2021 (t=1.0), Nathan tem 25 anos completos."""
        final_date = date(2021, 9, 7)
        final_age = calculate_age(BIRTHDATES["Nathan"], final_date)
        self.assertEqual(final_age, 25, "Nathan deve ter exatamente 25 anos a 07/09/2021.")
        self.assertIn("25 anos", self.arch_text)
        self.assertIn("25 anos", self.map_text)

    def test_historical_context_covid_19_documented_for_2020_2021(self):
        """O mundo paralelo preserva os acontecimentos históricos reais; 2020–2021 deve integrar o contexto de COVID-19."""
        self.assertIn("COVID-19", self.arch_text, "SERIES_GLOBAL_ARCHITECTURE.md deve referenciar o contexto de COVID-19 em 2020–2021.")
        self.assertIn("COVID-19", self.map_text, "MULTI_SEASON_CHRONOLOGY_MAP.md deve referenciar o contexto de COVID-19 em 2020–2021.")

    def test_world_difference_markers_complete_for_chronology_map(self):
        """MULTI_SEASON_CHRONOLOGY_MAP.md deve conter os 4 marcadores WD e estar listado nas 4 dependências em WORLD_DIFFERENCE_REGISTRY.md."""
        for wd in ["WD-001", "WD-002", "WD-003", "WD-004"]:
            with self.subTest(marker=wd):
                self.assertIn(f"<!-- {wd} -->", self.map_text, f"MULTI_SEASON_CHRONOLOGY_MAP.md deve conter o marcador <!-- {wd} -->.")
                self.assertIn("canon/timeline/MULTI_SEASON_CHRONOLOGY_MAP.md", self.wd_text, f"WORLD_DIFFERENCE_REGISTRY.md deve listar o mapa cronológico em {wd}.")

if __name__ == '__main__':
    unittest.main()
