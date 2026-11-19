"""
Testes de introdução orgânica de personagens e continuidade relacional:
- Personagens devem ser apresentados de forma individualizada, progressiva e ancorada em EVENT_REGISTRY.md.
- O protagonista NÃO deve ter contacto direto prematuro com personagens antes dos seus episódios canónicos de introdução.
- A introdução de um personagem deve deixar um efeito duradouro nas interações subsequentes (persistência relacional).
"""

import unittest
import re
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata, extract_events_from_registry

class TestCharacterIntroductions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*.*")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episodes_dir.glob("EP*_OUTLINE.md")]
        cls.events = extract_events_from_registry()
        
        # Os nomes canónicos são estáveis; o episódio de estreia é derivado do EVENT_REGISTRY.
        # Eventos explicitamente marcados como paralelos não contam como encontro direto.
        cls.character_patterns = {
            "alex": r"\bAlex\b",
            "phil": r"\bPhil\b",
            "maxwell": r"\bMaxwell\b",
            "claire": r"\bClaire\b",
            "luke": r"\bLuke\b",
            "haley": r"\bHaley\b",
            "jay": r"\bJay\b",
            "manny": r"\bManny\b",
            "mitchell": r"\bMitchell\b",
            "cameron": r"\bCameron\b",
        }
        cls.first_direct_contact = cls._derive_first_contact_episodes()

    @classmethod
    def _derive_first_contact_episodes(cls):
        first_contact = {}
        for event in cls.events:
            participants = event["characters"]
            normalized = [participant.casefold() for participant in participants]
            if "nathan" not in normalized:
                continue
            if any("parallel" in participant for participant in normalized):
                continue

            episode_match = re.fullmatch(r"EP(\d{2})", event["episode"].strip())
            if not episode_match:
                continue
            episode_number = int(episode_match.group(1))
            participant_text = " ".join(participants)

            for character, pattern in cls.character_patterns.items():
                if re.search(pattern, participant_text, re.IGNORECASE):
                    first_contact[character] = min(
                        episode_number, first_contact.get(character, episode_number)
                    )
        return first_contact

    def test_registry_defines_every_tracked_character_introduction(self):
        """Assegura que o registo tem um primeiro evento elegível para cada personagem monitorizada."""
        self.assertEqual(
            set(self.first_direct_contact),
            set(self.character_patterns),
            "EVENT_REGISTRY.md deve definir o primeiro evento com Nathan para todas as personagens monitorizadas.",
        )

    def test_progressive_character_discovery(self):
        """Verifica se os contactos canónicos não são despejados em bloco imediato no primeiro episódio."""
        # Alex e Phil são os únicos contactos diretos do núcleo Dunphy no EP01
        ep1_files = [f for f in self.episode_files if f.name.startswith("EP01")]
        ep1_text = " ".join(f.read_text(encoding='utf-8') for f in ep1_files)
        
        self.assertIn("alex", ep1_text.lower(), "Alex deve ser a primeira conexão intelectual estabelecida no EP01.")
        self.assertIn("phil", ep1_text.lower(), "Phil deve ter o primeiro encontro acidental com Nathan no EP01.")
        
        # Família alargada (Jay, Manny, Mitchell, Cam) NÃO deve ter diálogos ou encontros com Nathan no EP01
        for distant_char in ["jay pritchett", "manny delgado", "mitchell pritchett", "cameron toucker", "cameron tucker"]:
            self.assertNotIn(
                distant_char, ep1_text.lower(),
                f"{distant_char} não deve surgir introduzido no EP01."
            )

    def test_no_premature_direct_interaction_with_protagonist(self):
        """Garante que Nathan não tem diálogo direto nem interage cara a cara com personagens antes do episódio previsto no EVENT_REGISTRY."""
        for char, first_ep in self.first_direct_contact.items():
            for ep_num in range(1, first_ep):
                ep_prefix = f"EP{ep_num:02d}"
                files_to_check = [f for f in self.episode_files if f.name.startswith(ep_prefix)]
                for f in files_to_check:
                    content = f.read_text(encoding='utf-8')
                    # Verificar padrões onde Nathan conversa ou se encontra diretamente com o personagem
                    suspicious_patterns = [
                        rf'Nathan[^\n]{{0,50}}(?:meets|conversa com|dialoga com|cumprimenta|answers)\s+{char}',
                        rf'{char}[^\n]{{0,50}}(?:meets|conversa com|dialoga com|cumprimenta|answers)\s+Nathan',
                        rf'—\s*[^—\n]*Nathan[^\n]*\b{char}\b',
                    ]
                    for pattern in suspicious_patterns:
                        match = re.search(pattern, content, re.IGNORECASE)
                        self.assertIsNone(
                            match,
                            f"Contacto prematuro indevido de {char} com Nathan encontrado em {f.name}: '{match.group(0) if match else ''}' (introdução oficial prevista apenas para EP{first_ep:02d})."
                        )

    def test_relationship_persistence(self):
        """Verifica se após a introdução de um personagem-chave (Alex), o vínculo tem continuidade cumulativa em todos os episódios subsequentes."""
        for ep_num in range(1, 7):
            ep_prefix = f"EP{ep_num:02d}"
            ep_files = [f for f in self.episode_files if f.name.startswith(ep_prefix)]
            alex_present = any("alex" in f.read_text(encoding='utf-8').lower() for f in ep_files)
            self.assertTrue(
                alex_present,
                f"Alex Dunphy deve manter presença e continuidade cumulativa em todos os episódios da Temporada 1 (falhou em {ep_prefix})."
            )

    def test_extended_canon_progressive_appearance(self):
        """Verifica se as introduções nos outlines dos episódios avançados respeitam os marcos previstos."""
        ep_map = {ep["file"]: ep for ep in self.parsed_episodes}
        
        # EP05 introduz Manny formalmente
        if "EP05_LAUNCH_TRAJECTORY_OUTLINE.md" in ep_map:
            content5 = ep_map["EP05_LAUNCH_TRAJECTORY_OUTLINE.md"]["path"].read_text(encoding='utf-8').lower()
            self.assertIn("manny", content5)
            
        # EP06 introduz Cameron e Mitchell
        if "EP06_WINTER_CONSTANTS_OUTLINE.md" in ep_map:
            content6 = ep_map["EP06_WINTER_CONSTANTS_OUTLINE.md"]["path"].read_text(encoding='utf-8').lower()
            self.assertIn("mitchell", content6)
            self.assertIn("cameron", content6)

if __name__ == '__main__':
    unittest.main()
