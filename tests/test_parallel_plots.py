"""
Verificações heurísticas da estrutura de múltiplos enredos:
- Conta as tramas declaradas e procura palavras-chave associadas a outras personagens.
- Procura indicadores textuais de persistência; não avalia causalidade ou qualidade narrativa.
"""

import unittest
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata

class TestParallelPlotsAndAntiFiller(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*_OUTLINE.md")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episode_files]

    def test_minimum_three_plots_per_episode(self):
        """Verifica se cada episódio contém no mínimo 3 tramas ativas em paralelo."""
        for ep in self.parsed_episodes:
            total_threads = len(ep["threads"])
            self.assertGreaterEqual(
                total_threads, 3,
                f"O episódio {ep['file']} tem apenas {total_threads} tramas declaradas. Mínimo exigido: 3 (1 grande + >=2 menores)."
            )

    def test_has_major_and_minor_threads(self):
        """Verifica se há pelo menos 1 trama de grande escala e pelo menos 2 tramas menores focadas em outros personagens."""
        for ep in self.parsed_episodes:
            # Se não classificado explicitamente pelo parser, verifica a contagem geral
            threads = ep["threads"]
            self.assertTrue(len(threads) >= 3, f"Episódio {ep['file']} deve ter >= 3 tramas")
            
            # Pelo menos duas tramas devem envolver pessoas que não sejam apenas o código a solo de Nathan
            non_solo_threads = [
                t for t in threads 
                if any(k in t["desc"].lower() for k in ["alex", "family", "school", "football", "dunphy", "callahan", "modern", "whitaker"])
            ]
            self.assertGreaterEqual(
                len(non_solo_threads), 2,
                f"O episódio {ep['file']} deve ter pelo menos 2 tramas secundárias com outros personagens (encontradas: {len(non_solo_threads)})."
            )

    def test_anti_filler_persistent_consequences(self):
        """Verifica se o episódio define alterações permanentes de estado (sem episódios fillers que resetam ao fim)."""
        for ep in self.parsed_episodes:
            content = ep["path"].read_text(encoding='utf-8').lower()
            # Deve conter indicação explícita de consequências, mudanças ou evolução de estado
            has_persistence_indicator = (
                "persistent" in content or 
                "consequences" in content or 
                "consequências" in content or 
                "estado persistente" in content or
                "consequência" in content or
                len(ep["persistent_state_changes"]) > 0
            )
            self.assertTrue(
                has_persistence_indicator,
                f"O episódio {ep['file']} não define consequências duradouras ou estado persistente (risco de ser filler)."
            )

if __name__ == '__main__':
    unittest.main()
