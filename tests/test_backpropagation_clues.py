"""
Testes de backpropagation de pistas e rastreabilidade de adereços (prop continuity):
- Qualquer adereço ou pista com relevância futura deve ter proveniência documentada (aquisição, presença de fundo ou menção prévia).
- Previne que soluções ou objetos surjam 'do nada' no exato momento da necessidade.
- Valida rigorosamente que o episódio de génese antecede o episódio de payoff e que os IDs figuram nos respetivos ficheiros.
"""

import unittest
import re
from pathlib import Path
from tests.parser import REPO_ROOT, extract_props_from_registry

class TestBackpropagationAndProps(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.registry_file = REPO_ROOT / "canon" / "narrative" / "PROP_AND_CLUE_REGISTRY.md"
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = list(cls.episodes_dir.glob("EP*.*"))
        cls.props = extract_props_from_registry()

    def test_registry_file_exists(self):
        """O ficheiro de registo de adereços e pistas retropropagadas deve existir no canon."""
        self.assertTrue(
            self.registry_file.exists(),
            f"Ficheiro {self.registry_file} deve existir para rastrear a proveniência de adereços e pistas."
        )

    def test_clues_have_provenance_and_payoff_ordering(self):
        """Verifica se cada pista/adereço registado possui génese anterior ou concomitante (com precedência cronológica) ao episódio da sua resolução."""
        self.assertGreaterEqual(len(self.props), 5, "Devem existir pelo menos 5 adereços/pistas documentados no registo.")
        
        for prop in self.props:
            prop_id = prop["id"]
            gen_ep = prop["genesis_ep"]
            payoff_eps = prop["payoff_eps"]
            
            self.assertTrue(bool(gen_ep), f"{prop_id} deve ter um episódio de génese identificado.")
            self.assertTrue(len(payoff_eps) > 0, f"{prop_id} deve ter pelo menos um episódio de payoff identificado.")
            
            gen_num = int(re.search(r'\d+', gen_ep).group(0))
            for pay_ep in payoff_eps:
                pay_num = int(re.search(r'\d+', pay_ep).group(0))
                self.assertLessEqual(
                    gen_num, pay_num,
                    f"Violação de causalidade em {prop_id}: episódio de génese ({gen_ep}) surge após o payoff ({pay_ep})."
                )

    def test_props_and_clues_presence_in_episodes(self):
        """Verifica se cada adereço/pista (ID [PROP-xxx] ou [CLUE-xxx]) está textualmente presente nos ficheiros dos respetivos episódios de génese e payoff."""
        for prop in self.props:
            prop_id = prop["id"]
            gen_ep = prop["genesis_ep"]
            payoff_eps = prop["payoff_eps"]
            
            # Verificar presença no episódio de génese
            gen_files = [f for f in self.episode_files if f.name.startswith(gen_ep)]
            gen_found = any(prop_id in f.read_text(encoding='utf-8') for f in gen_files)
            self.assertTrue(
                gen_found,
                f"O adereço {prop_id} ({prop['name']}) tem génese declarada em {gen_ep}, mas a tag [{prop_id}] não foi encontrada nos ficheiros de {gen_ep}."
            )
            
            # Verificar presença em cada episódio de payoff
            for pay_ep in payoff_eps:
                pay_files = [f for f in self.episode_files if f.name.startswith(pay_ep)]
                pay_found = any(prop_id in f.read_text(encoding='utf-8') for f in pay_files)
                self.assertTrue(
                    pay_found,
                    f"O adereço {prop_id} ({prop['name']}) tem payoff declarado em {pay_ep}, mas a tag [{prop_id}] não foi encontrada nos ficheiros de {pay_ep}."
                )

    def test_background_presence_documented(self):
        """Verifica se todos os adereços e pistas possuem registo explícito de presenças naturais em fundo de cena."""
        for prop in self.props:
            prop_id = prop["id"]
            bg = prop["background_raw"].strip()
            self.assertTrue(
                len(bg) > 10,
                f"{prop_id} deve ter detalhe documental de presença em fundo de cena (recebeu apenas '{bg}')."
            )

if __name__ == '__main__':
    unittest.main()
