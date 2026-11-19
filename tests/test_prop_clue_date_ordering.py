"""
Date-level causal checks for the prop/clue registry.

Episode ordering alone is insufficient: a clue can be planted and paid off
inside the same episode, so explicit Gregorian dates must also be compared.
"""

import re
import unittest
from datetime import date
from pathlib import Path

from tests.parser import REPO_ROOT


DATE_RE = re.compile(r"\\b(\\d{1,2})/(\\d{1,2})/(20\\d{2})\\b")


def parse_registry_dates(value: str):
    """Return all explicit DD/MM/YYYY dates found in a registry cell."""
    return [
        date(int(year), int(month), int(day))
        for day, month, year in DATE_RE.findall(value)
    ]


def is_causally_ordered(genesis: date, payoff: date) -> bool:
    """A payoff cannot precede the item's genesis."""
    return genesis <= payoff


def parse_prop_rows(path: Path):
    """Read prop/clue table rows without depending on episode-number ordering."""
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or not re.search(r"\\b(?:PROP|CLUE)-\\d+\\b", line):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        match = re.search(r"\\b(?:PROP|CLUE)-\\d+\\b", cells[0])
        if match:
            rows.append({
                "id": match.group(0),
                "genesis": cells[2],
                "background": cells[3],
                "payoff": cells[4],
            })
    return rows


class TestPropClueDateOrdering(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = REPO_ROOT / "canon" / "narrative" / "PROP_AND_CLUE_REGISTRY.md"
        cls.rows = parse_prop_rows(cls.registry) if cls.registry.exists() else []

    def test_registry_contains_dated_genesis_and_payoff(self):
        self.assertTrue(self.registry.exists(), "Prop/clue registry is missing.")
        self.assertGreater(len(self.rows), 0, "No prop/clue rows were parsed.")
        for row in self.rows:
            with self.subTest(item=row["id"]):
                genesis_dates = parse_registry_dates(row["genesis"])
                payoff_dates = parse_registry_dates(row["payoff"])
                self.assertTrue(genesis_dates, f"{row['id']} needs an explicit Gregorian genesis date.")
                self.assertTrue(payoff_dates, f"{row['id']} needs at least one explicit Gregorian payoff date.")
                self.assertEqual(len(genesis_dates), 1, f"{row['id']} should have exactly one genesis date.")
                for payoff in payoff_dates:
                    self.assertTrue(
                        is_causally_ordered(genesis_dates[0], payoff),
                        f"{row['id']} has a payoff dated before its genesis: "
                        f"{payoff} < {genesis_dates[0]}."
                    )

    def test_date_parser_rejects_impossible_calendar_dates(self):
        with self.assertRaises(ValueError):
            parse_registry_dates("31/02/2009")

    def test_same_episode_can_still_have_invalid_causal_order(self):
        genesis = parse_registry_dates("EP02 (08/10/2009)")[0]
        earlier_payoff = parse_registry_dates("EP02 (07/10/2009)")[0]
        self.assertFalse(is_causally_ordered(genesis, earlier_payoff))


if __name__ == "__main__":
    unittest.main()
