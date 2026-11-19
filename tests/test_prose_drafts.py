"""
Verificações mecânicas dos rascunhos de prosa (EP*_DRAFT.md):
- Confirma que cada rascunho tem um outline correspondente.
- Procura marcadores de diálogo e uma lista fixa de expressões proibidas.
- Não avalia idioma, naturalidade, voz, POV, ritmo ou qualidade literária.
"""

import unittest
import re
from pathlib import Path
from tests.parser import REPO_ROOT

class TestProseDrafts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.draft_files = sorted(list(cls.episodes_dir.glob("EP*_DRAFT.md")))

    def test_draft_has_corresponding_outline(self):
        """Cada rascunho de prosa deve ter um outline correspondente registado na mesma pasta."""
        for draft in self.draft_files:
            prefix = draft.name.split("_")[0] # ex: EP01
            outlines = list(self.episodes_dir.glob(f"{prefix}_*OUTLINE.md"))
            self.assertTrue(
                len(outlines) >= 1,
                f"O rascunho {draft.name} não tem nenhum outline correspondente ({prefix}_*OUTLINE.md)."
            )

    def test_prose_quality_and_no_camera_monologues(self):
        """Garante que a prosa contém diálogo natural com travessão e sem monólogos em frente à câmara."""
        forbidden_tropes = [
            r"olhando para a câmara",
            r"virado para a câmara",
            r"como um narrador de comédia",
            r"o destino sussurrou",
            r"com um brilho premonitório nos olhos",
            r"looking at the camera",
            r"facing the camera",
            r"like a sitcom narrator",
            r"destiny whispered",
            r"with a premonitory gleam"
        ]
        
        for draft in self.draft_files:
            content = draft.read_text(encoding='utf-8')
            
            # Deve conter diálogo real com travessões ou aspas
            has_dialogue = (
                bool(re.search(r'—\s+[A-ZÀ-Ú]', content)) or 
                bool(re.search(r'«[^»]+»', content)) or
                bool(re.search(r'"[^"\n]{2,}"', content))
            )
            self.assertTrue(has_dialogue, f"O rascunho {draft.name} deve conter diálogo formatado.")
            
            # Não deve conter os clichés proibidos
            for trope in forbidden_tropes:
                self.assertFalse(
                    re.search(trope, content, re.IGNORECASE),
                    f"Cliché ou quebra de quarta parede proibida detetada em {draft.name}: '{trope}'"
                )

if __name__ == '__main__':
    unittest.main()
