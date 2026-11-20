"""Season-wide regressions for decisions that must remain coherent across episodes.

These tests protect explicit continuity and documentation contracts. They do not
prove that a scene is dramatically effective or that the prose is factually perfect.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes" / "season-1"


class TestSeasonOneDecisionConsistency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.arc = (ROOT / "canon/narrative/SEASON_1_ARC_PLAN.md").read_text(encoding="utf-8")
        cls.continuity = (ROOT / "canon/timeline/SEASON_1_CONTINUITY.md").read_text(encoding="utf-8")
        cls.decisions = (ROOT / "canon/STORY_DECISIONS_TO_MAKE.md").read_text(encoding="utf-8")
        cls.register = (ROOT / "canon/narrative/SEASON_1_DECISION_AND_STATUS_REGISTER.md").read_text(encoding="utf-8")
        cls.ep01 = (EPISODES / "EP01_DRAFT.md").read_text(encoding="utf-8")
        cls.ep02 = (EPISODES / "EP02_DRAFT.md").read_text(encoding="utf-8")
        cls.ep02_outline = (EPISODES / "EP02_FINISH_THE_GAME_OUTLINE.md").read_text(encoding="utf-8")
        cls.ep03 = (EPISODES / "EP03_DRAFT.md").read_text(encoding="utf-8")
        cls.ep04_outline = (EPISODES / "EP04_MEMORY_PROFILES_OUTLINE.md").read_text(encoding="utf-8")
        cls.ep05_outline = (EPISODES / "EP05_LAUNCH_TRAJECTORY_OUTLINE.md").read_text(encoding="utf-8")
        cls.ep06_outline = (EPISODES / "EP06_WINTER_CONSTANTS_OUTLINE.md").read_text(encoding="utf-8")

    def test_grade_gap_is_preserved_through_the_end_of_season_one(self):
        self.assertIn("Nathan conclui o 8.º ano", self.arc)
        self.assertIn("Alex conclui o 7.º ano", self.arc)
        self.assertIn("prepara a entrada no High School", self.arc)
        self.assertIn("Alex conclui o 7.º ano e transita para o 8.º ano", self.arc)
        self.assertNotIn("Alex e Nathan partilham a distinção de honra com médias máximas", self.arc)
        self.assertNotIn("Nathan e Alex combinam rotinas de estudo conjunto e leitura para as férias antes da entrada no High School", self.arc)

    def test_october_15_is_an_internal_playable_milestone_not_publication(self):
        self.assertIn("first playable vertical slice", self.continuity.lower())
        self.assertIn("not a public release", self.continuity.lower())
        self.assertIn("vertical-slice milestone", self.ep02_outline.lower())
        self.assertIn("not yet a public app store release", self.ep02_outline.lower())
        self.assertIn("submissão do binário final", self.ep04_outline.lower())
        self.assertIn("03 de dezembro", self.ep05_outline.lower())
        self.assertNotIn("real playable release around 15 October", self.continuity)

    def test_opening_four_family_member_goal_is_not_silently_marked_complete(self):
        self.assertIn("UNRESOLVED CONFLICT", self.decisions)
        self.assertIn("four family members", self.decisions.lower())
        self.assertIn("18 September", self.decisions)
        self.assertIn("28 September", self.decisions)
        self.assertIn("four-family-member contact target", self.register.lower())

    def test_iphone_3gs_memory_is_not_described_as_a_fixed_128_mb_app_heap(self):
        self.assertNotIn("the OS eats almost half", self.ep01)
        self.assertNotIn("128 megabytes of usable heap", self.ep01)
        self.assertIn("available memory", self.ep01.lower())
        self.assertIn("measure", self.ep01.lower())

    def test_memory_metrics_distinguish_engine_data_from_application_heap(self):
        self.assertIn("ENGINE DATA: 4.2 MB", self.ep01)
        self.assertIn("LIVE HEAP: 28.4 MB", self.ep02)
        self.assertNotIn("RAM: 28.4 MB", self.ep02)

    def test_dialogue_does_not_repeat_the_daily_glucose_claim(self):
        self.assertNotIn("twenty percent of your daily glucose", self.ep02.lower())

    def test_ep03_luke_compass_directors_cut_is_not_duplicated(self):
        heading = "### Director's Cut 1 — October 16, 2009 (Friday Afternoon): The Glint by the Fence"
        self.assertEqual(self.ep03.count(heading), 1)


    def test_v11_reuses_the_spatial_grid_already_built_in_ep03(self):
        self.assertIn("reutiliza a grelha espacial", self.ep06_outline.lower())
        self.assertIn("ep03", self.ep06_outline.lower())
        self.assertNotIn("integração de uma grelha espacial de particionamento", self.ep06_outline.lower())

    def test_alex_schoolwork_does_not_assume_unestablished_organic_chemistry(self):
        self.assertNotIn("química orgânica", self.ep05_outline.lower())
        self.assertIn("teste de ciências", self.ep05_outline.lower())

    def test_ep06_does_not_claim_the_core_family_introduction_cycle_is_complete(self):
        self.assertNotIn("ciclo completo dos personagens canon concluído", self.ep06_outline.lower())
        self.assertIn("gloria", self.ep06_outline.lower())
        self.assertIn("ep07", self.ep06_outline.lower())


    def test_ep10_ipad_funding_does_not_assume_proceeds_are_nathans(self):
        ep10 = self.arc[self.arc.index("### EP10"):self.arc.index("### EP11")]
        self.assertIn("decisão explícita de Clifford e Heather", ep10)
        self.assertNotIn("Nathan adquire uma unidade com as receitas", ep10)

    def test_ep10_callahan_typo_does_not_rename_claire_dunphy(self):
        ep10 = self.arc[self.arc.index("### EP10"):self.arc.index("### EP11")]
        self.assertIn("Claire Dunphy & Heather Callahan", ep10)
        self.assertNotIn("Claire Callahan", ep10)

    def test_season_status_register_points_to_the_existing_decision_authority(self):
        self.assertIn("DECISION_LOG.md", self.register)
        self.assertIn("STORY_DECISIONS_TO_MAKE.md", self.register)
        self.assertIn("EVENT_REGISTRY.md", self.register)
        self.assertIn("Coverage status: partial", self.register)


if __name__ == "__main__":
    unittest.main()
