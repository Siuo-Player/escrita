"""Cross-document story canon synchronization regressions.

These tests protect deterministic documentation contracts. They do not
replace human review of prose, characterization, pacing, or factual research.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(path):
    target = ROOT / path
    return target.read_text(encoding="utf-8") if target.exists() else ""


class TestStoryCanonSynchronization(unittest.TestCase):
    def test_story_bible_defines_document_ownership_and_canon_hierarchy(self):
        bible = read("canon/STORY_BIBLE.md")
        self.assertIn("CANON SNAPSHOT", bible)
        self.assertIn("DECISION_LOG.md", bible)
        self.assertIn("WORLD_DIFFERENCE_REGISTRY.md", bible)
        self.assertIn("EVENT_REGISTRY.md", bible)
        self.assertIn("MULTI_SEASON_CHRONOLOGY_MAP.md", bible)
        self.assertIn("SERIES_GLOBAL_ARCHITECTURE.md", bible)

    def test_memory_is_human_fallible_not_eidetic_or_verbatim(self):
        nathan = read("canon/characters/NATHAN_CALLAHAN.md").lower()
        policy = read("canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md").lower()
        decisions = read("canon/STORY_DECISIONS_TO_MAKE.md").lower()
        for document in (nathan, policy, decisions):
            with self.subTest(document=document[:50]):
                self.assertNotIn("eidetic memory", document)
                self.assertNotIn("everything actually shown", document)
                self.assertNotIn("exact dialogue", document)
                self.assertNotIn("perfect recall", document)
        self.assertIn("fallible", nathan)
        self.assertIn("attention", nathan)
        self.assertIn("off-screen", policy)
        self.assertIn("dec-019", read("canon/DECISION_LOG.md").lower())

    def test_no_artificial_four_contact_quota_before_pilot_anchor(self):
        decisions = read("canon/STORY_DECISIONS_TO_MAKE.md").lower()
        nathan = read("canon/characters/NATHAN_CALLAHAN.md").lower()
        arc = read("canon/narrative/SEASON_1_ARC_PLAN.md").lower()
        for document in (decisions, nathan, arc):
            with self.subTest(document=document[:50]):
                self.assertNotIn("at least four members", document)
                self.assertNotIn("four family members", document)
                self.assertNotIn("four-family-member contact target", document)
        self.assertIn("dec-018", read("canon/DECISION_LOG.md").lower())
        self.assertIn("18 de setembro de 2009", arc)
        self.assertIn("28 de setembro de 2009", arc)

    def test_timeline_uses_qualitative_memory_phases_not_fake_percentages(self):
        chronology = read("canon/timeline/MULTI_SEASON_CHRONOLOGY_MAP.md")
        self.assertIn("qualitative", chronology.lower())
        self.assertIn("memória", chronology.lower())
        self.assertNotIn("95%", chronology)
        self.assertNotIn("85%", chronology)
        self.assertNotIn("00%", chronology)

    def test_story_opens_in_seattle_and_relocation_happens_later(self):
        architecture = read("canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md").lower()
        bible = read("canon/STORY_BIBLE.md").lower()
        self.assertIn("seattle", architecture)
        self.assertIn("14/09", bible)
        self.assertIn("15/09", bible)
        self.assertNotIn("chegada a los angeles, 13.º aniversário", architecture)

    def test_all_dialogue_examples_follow_the_prose_language_decision(self):
        dialogue = read("canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md")
        self.assertNotIn("— Esse é o", dialogue)
        self.assertIn("— Is that", dialogue)
        self.assertIn("American English", dialogue)

    def test_style_guide_uses_focalisation_not_fixed_character_caricatures(self):
        style = read("canon/narrative/MODERN_PROSE_AND_THEATRICAL_STYLE.md").lower()
        self.assertIn("não são arquétipos fixos", style)
        self.assertIn("focalização", style)
        self.assertIn("o que a personagem repara", style)

    def test_decision_review_is_summarised_in_season_register(self):
        register = read("canon/narrative/SEASON_1_DECISION_AND_STATUS_REGISTER.md")
        for decision in ("DEC-016", "DEC-017", "DEC-018", "DEC-019", "DEC-020"):
            with self.subTest(decision=decision):
                self.assertIn(decision, register)
        self.assertIn("2026-11-21", register)

    def test_technical_pair_counts_define_unordered_pairs(self):
        decisions = read("canon/DECISION_LOG.md").lower()
        arc = read("canon/narrative/SEASON_1_ARC_PLAN.md").lower()
        self.assertIn("unordered", decisions)
        self.assertIn("435", arc)
        self.assertIn("19,900", arc)

    def test_global_story_snapshot_and_key_documents_share_current_genre_boundary(self):
        for path in (
            "README.md",
            "canon/characters/NATHAN_CALLAHAN.md",
            "canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md",
            "canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md",
            "canon/timeline/MULTI_SEASON_CHRONOLOGY_MAP.md",
        ):
            content = read(path).lower()
            with self.subTest(path=path):
                self.assertIn("slice of life", content)
                self.assertIn("reincarnation is the only supernatural exception", content)


if __name__ == "__main__":
    unittest.main()
