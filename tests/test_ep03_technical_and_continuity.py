"""Targeted regressions for factual and continuity errors in EP03.

These tests protect explicit, researched constraints; they do not evaluate literary quality.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFT_PATH = ROOT / "episodes" / "season-1" / "EP03_DRAFT.md"


def between(text, start, end):
    start_at = text.index(start)
    end_at = text.index(end, start_at + len(start))
    return text[start_at:end_at]


class TestEpisode3TechnicalAndSourceContinuity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.draft = DRAFT_PATH.read_text(encoding="utf-8")

    def test_pairwise_collision_rate_uses_seconds_not_minutes(self):
        self.assertIn("1.2 million", self.draft)
        self.assertRegex(self.draft, r"1\.2 million[^.\n]*per second")
        self.assertNotRegex(self.draft, r"1\.2 million[^.\n]*per minute")

    def test_cortex_a8_is_not_described_as_lacking_vector_simd_hardware(self):
        self.assertIn("NEON", self.draft)
        self.assertNotRegex(
            self.draft,
            r"without a dedicated hardware vector coprocessor",
        )

    def test_coal_digger_pool_memory_attributes_the_jump_to_claire(self):
        scene = between(
            self.draft,
            "### Scene 3 — October 21, 2009",
            "## MOVEMENT II:",
        )
        self.assertIn("Claire", scene)
        self.assertRegex(scene, r"Claire[^.\n]{0,180}(?:jump|pool)")
        self.assertNotIn("Gloria jumping into the swimming pool", scene)

    def test_run_for_your_wife_footrace_is_marked_as_an_original_parallel_event(self):
        scene = between(
            self.draft,
            "### Scene 6 — October 28, 2009",
            "### Scene 7 — October 29, 2009",
        )
        self.assertRegex(
            scene,
            r"(?i)(?:not|isn't) (?:a scene|part) from .*Run for Your Wife|"
            r"original (?:parallel-world|neighbourhood) event",
        )

    def test_running_advice_does_not_repeat_the_lactic_acid_pooling_myth(self):
        self.assertNotIn("before the lactic acid pools", self.draft)

    def test_old_compass_is_not_found_in_the_wrong_family_member_memory(self):
        scene = between(
            self.draft,
            "### Scene 3 — October 21, 2009",
            "## MOVEMENT II:",
        )
        self.assertNotIn(
            "Gloria jumping into the swimming pool",
            scene,
        )


if __name__ == "__main__":
    unittest.main()
