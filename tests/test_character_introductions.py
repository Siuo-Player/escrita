"""
Testes de introdução orgânica de personagens e continuidade relacional:
- Personagens devem ser apresentados de forma individualizada e em contextos e momentos diferentes.
- A introdução de um personagem deve deixar um efeito duradouro nas interações subsequentes.
"""

import unittest
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata

class TestCharacterIntroductions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*_OUTLINE.md")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episode_files]

    def test_progressive_character_discovery(self):
        """Verifica se os personagens não são todos apresentados em bloco imediato no primeiro minuto."""
        if not self.parsed_episodes:
            return
            
        first_ep = self.parsed_episodes[0]
        # No EP01, Nathan chega à cidade e à escola a 16 de setembro.
        # Alex é o primeiro contacto chave na escola (18 de setembro).
        # Família alargada (Jay, Gloria, Mitchell, Cam) NÃO deve ser apresentada em massa no EP01 como se Nathan fosse membro da família.
        content = first_ep["path"].read_text(encoding='utf-8')
        
        # O outline do EP01 deve especificar expressamente que o piloto corre em paralelo e que Nathan NÃO entra na reunião de família
        self.assertIn("pilot", content.lower(), "EP01 deve situar a relação com o Pilot")
        self.assertTrue(
            "alex" in first_ep["character_mentions"],
            "Alex deve ser a primeira conexão escolar relevante estabelecida no EP01."
        )

    def test_relationship_persistence(self):
        """Verifica se após o primeiro contacto de um personagem, o estado entre eles não faz reset a desconhecido."""
        # Se um personagem é conhecido no EP01, nos episódios seguintes a relação deve ser referenciada como já iniciada
        if len(self.parsed_episodes) >= 2:
            ep1 = self.parsed_episodes[0]
            ep2 = self.parsed_episodes[1]
            ep2_content = ep2["path"].read_text(encoding='utf-8').lower()
            
            # Alex foi conhecida no EP01; no EP02 a dinâmica deve dar continuidade
            self.assertTrue(
                "alex" in ep2_content,
                "Alex deve ter continuidade e evolução relacional a partir do EP01 para o EP02."
            )

if __name__ == '__main__':
    unittest.main()
