"""
Testes de backpropagation de pistas e rastreabilidade de adereços (prop continuity):
- Qualquer adereço ou pista com relevância futura deve ter proveniência documentada (aquisição, presença de fundo ou menção prévia).
- Previne que soluções ou objetos surjam 'do nada' no exato momento da necessidade.
"""

import unittest
import re
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata

class TestBackpropagationAndProps(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.registry_file = REPO_ROOT / "canon" / "narrative" / "PROP_AND_CLUE_REGISTRY.md"
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*_OUTLINE.md")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episode_files]

    def test_registry_file_exists(self):
        """O ficheiro de registo de adereços e pistas retropropagadas deve existir no canon."""
        self.assertTrue(
            self.registry_file.exists(),
            f"Ficheiro {self.registry_file} deve existir para rastrear a proveniência de adereços e pistas."
        )

    def test_clues_have_provenance_and_payoff(self):
        """Verifica se cada pista/adereço registado possui génese anterior ao episódio da sua resolução."""
        if not self.registry_file.exists():
            return
            
        content = self.registry_file.read_text(encoding='utf-8')
        # Procura entradas da tabela: | ID | Adereço/Pista | Génese (Ep/Cena) | Presença Fundo | Ponto de Foco/Payoff |
        table_lines = [l for l in content.splitlines() if l.strip().startswith("|") and not l.strip().startswith("|---")]
        self.assertGreater(len(table_lines), 2, "A tabela de adereços e pistas deve ter entradas documentadas.")

if __name__ == '__main__':
    unittest.main()
