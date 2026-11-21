"""Regression contracts for character agency and narrative quality.

These tests check that the project documents its own review standard and that
core planning documents point to it. They cannot determine literary quality,
voice, emotional credibility, or whether an individual scene succeeds.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD = ROOT / "canon" / "narrative" / "NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md"
SCOPE = ROOT / "canon" / "STORY_SCOPE_AND_PROTAGONIST_DESIGN.md"
WORKFLOW = ROOT / "canon" / "narrative" / "STORY_DEVELOPMENT_WORKFLOW.md"
ARCHITECTURE = ROOT / "canon" / "narrative" / "SERIES_GLOBAL_ARCHITECTURE.md"
SEASON_ONE = ROOT / "canon" / "narrative" / "SEASON_1_ARC_PLAN.md"
DECISION_LOG = ROOT / "canon" / "DECISION_LOG.md"


class TestNarrativeQualityContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.standard = STANDARD.read_text(encoding="utf-8") if STANDARD.exists() else ""
        cls.scope = SCOPE.read_text(encoding="utf-8") if SCOPE.exists() else ""
        cls.workflow = WORKFLOW.read_text(encoding="utf-8") if WORKFLOW.exists() else ""
        cls.architecture = ARCHITECTURE.read_text(encoding="utf-8") if ARCHITECTURE.exists() else ""
        cls.season_one = SEASON_ONE.read_text(encoding="utf-8") if SEASON_ONE.exists() else ""
        cls.decision_log = DECISION_LOG.read_text(encoding="utf-8") if DECISION_LOG.exists() else ""

    def test_narrative_quality_standard_exists_and_has_required_sections(self):
        self.assertTrue(
            STANDARD.is_file(),
            "Create the durable narrative quality and character agency standard.",
        )
        required_sections = (
            "## 1. Objetivo e âmbito",
            "## 2. Lições comparativas de outras fanfics",
            "## 3. Contrato de agência das personagens",
            "### Nathan Callahan",
            "### Alex Dunphy",
            "### Haley Dunphy",
            "### Restantes personagens e famílias",
            "## 4. Antipadrões a evitar",
            "## 5. Integração causal das tramas",
            "## 6. Tecnologia como experiência vivida",
            "## 7. Romance, separação e consequências",
            "## 8. Protocolo de revisão",
            "## 9. Limites dos testes automáticos",
            "## 10. Fontes e limitações da comparação",
        )
        for heading in required_sections:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.standard)

    def test_standard_preserves_agency_for_nathan_alex_haley_and_ensemble(self):
        self.assertIn("Nathan Callahan", self.standard)
        self.assertIn("Alex Dunphy", self.standard)
        self.assertIn("Haley Dunphy", self.standard)
        self.assertIn("famílias Dunphy/Pritchett/Tucker", self.standard)
        self.assertIn("objetivos independentes", self.standard.lower())
        self.assertIn("não existe para validar nathan", self.standard.lower())
        self.assertIn("não é terapeuta", self.standard.lower())

    def test_comparative_fanfiction_notes_separate_reader_reviews_from_model_analysis(self):
        self.assertIn("The Eldest Delgado", self.standard)
        self.assertIn("A Fateful Encounter", self.standard)
        self.assertIn("Well I Said Maybe", self.standard)
        self.assertIn("Alex & Brendan", self.standard)
        self.assertIn("Well, There's No Going Back Now", self.standard)
        self.assertIn("não representam consenso", self.standard.lower())
        self.assertIn("observação textual", self.standard.lower())

    def test_existing_story_scope_links_to_the_new_standard(self):
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.scope)
        self.assertIn("goals", self.scope.lower())
        self.assertIn("personality", self.scope.lower())

    def test_writing_workflow_makes_agency_review_a_required_gate(self):
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.workflow)
        self.assertIn("agência", self.workflow.lower())
        self.assertIn("antes de redigir", self.workflow.lower())
        self.assertIn("depois de redigir", self.workflow.lower())

    def test_global_architecture_links_to_character_agency_constraints(self):
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.architecture)
        self.assertIn("autonomia", self.architecture.lower())
        self.assertIn("Alex", self.architecture)
        self.assertIn("Haley", self.architecture)

    def test_season_one_introductions_are_not_planned_as_a_praise_ladder(self):
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.season_one)
        self.assertIn("escada de elogios", self.season_one.lower())
        self.assertIn("fricção", self.season_one.lower())
        self.assertIn("reações próprias", self.season_one.lower())

    def test_standard_requires_plot_threads_to_change_each_other_causally(self):
        self.assertIn("consequências", self.standard.lower())
        self.assertIn("causal", self.standard.lower())
        self.assertIn("não basta coexistirem", self.standard.lower())
        self.assertIn("objetivos externos", self.standard.lower())

    def test_narrative_agency_standard_is_recorded_as_a_project_decision(self):
        self.assertTrue(DECISION_LOG.is_file())
        self.assertIn("DEC-016", self.decision_log)
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.decision_log)
        self.assertIn("PROJECT-WIDE NARRATIVE QUALITY STANDARD", self.decision_log)
        self.assertIn("not a new diegetic fact", self.decision_log.lower())

    def test_author_selected_inspirations_are_documented_with_power_systems_excluded(self):
        for title in ("Modern Family: Green Sun", "Re:Life With Karmic Gacha"):
            with self.subTest(title=title):
                self.assertIn(title, self.standard)
        self.assertIn("Apollo", self.standard)
        self.assertIn("Karmic Gacha", self.standard)
        self.assertIn("não importamos", self.standard.lower())
        self.assertIn("poderes", self.standard.lower())

    def test_similar_grounded_modern_family_fanfics_are_documented_as_comparators(self):
        for title in (
            "Reincarnated into Modern Family",
            "Modern Family: Adrian Delgado",
            "Modern Family: The Singer",
            "Modern Family: New Life",
        ):
            with self.subTest(title=title):
                self.assertIn(title, self.standard)

    def test_reincarnation_is_the_only_supernatural_exception_in_project_decisions(self):
        self.assertIn("DEC-017", self.decision_log)
        self.assertIn("única exceção sobrenatural", self.decision_log.lower())
        self.assertIn("NARRATIVE_QUALITY_AND_CHARACTER_AGENCY_STANDARD.md", self.decision_log)
        self.assertIn("renascimento", self.scope.lower())
        self.assertIn("única exceção sobrenatural", self.scope.lower())
        self.assertIn("única exceção sobrenatural", self.architecture.lower())
        self.assertIn("única exceção sobrenatural", self.workflow.lower())

    def test_slice_of_life_contract_excludes_systems_magic_and_supernatural_powers(self):
        for phrase in ("slice of life", "sem sistemas", "sem poderes sobrenaturais", "vida quotidiana"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.standard.lower())
        self.assertIn("único elemento sobrenatural", self.standard.lower())

    def test_automated_tests_do_not_claim_to_measure_subjective_literary_quality(self):
        self.assertIn("não conseguem avaliar", self.standard.lower())
        self.assertIn("revisão humana", self.standard.lower())
        self.assertIn("voz", self.standard.lower())


if __name__ == "__main__":
    unittest.main()
