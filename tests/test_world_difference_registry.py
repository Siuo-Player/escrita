"""Regression tests for the parallel-world difference registry.

These checks validate registry structure and explicit cross-references. They do not
claim to understand prose semantics or prove that every scene obeys the canon.
"""
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "canon" / "narrative" / "WORLD_DIFFERENCE_REGISTRY.md"

REQUIRED_FIELDS = {
    "Status",
    "Category",
    "Real-world baseline",
    "Parallel-world rule",
    "Scope",
    "Canon basis",
    "Dependent documents",
}
ALLOWED_STATUSES = {"CONFIRMED", "PROVISIONAL", "RETIRED"}
EXPECTED_FOUNDATIONAL_IDS = {"WD-001", "WD-002", "WD-003", "WD-004"}


def parse_world_difference_registry(content):
    """Parse WD headings and their bold-label metadata lines."""
    entries = []
    current = None

    for line in content.splitlines():
        heading = re.match(r"^###\s+(WD-\d{3})\s+—\s+(.+?)\s*$", line)
        if heading:
            current = {
                "id": heading.group(1),
                "title": heading.group(2),
                "fields": {},
            }
            entries.append(current)
            continue

        if current is None:
            continue

        field = re.match(r"^\s*-\s+\*\*(.+?):\*\*\s*(.*?)\s*$", line)
        if field:
            current["fields"][field.group(1)] = field.group(2)

    return entries


def document_paths(entry):
    raw = entry["fields"].get("Dependent documents", "")
    return [item.strip() for item in raw.split(";") if item.strip()]


class TestWorldDifferenceRegistry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = (
            REGISTRY_PATH.read_text(encoding="utf-8")
            if REGISTRY_PATH.exists()
            else ""
        )
        cls.entries = parse_world_difference_registry(cls.content)

    def test_world_difference_registry_exists(self):
        self.assertTrue(
            REGISTRY_PATH.is_file(),
            "Falta canon/narrative/WORLD_DIFFERENCE_REGISTRY.md: "
            "as diferenças entre o mundo real e o mundo paralelo têm de ter uma fonte canónica.",
        )

    def test_foundational_world_differences_are_registered(self):
        registered = {entry["id"] for entry in self.entries}
        self.assertTrue(
            EXPECTED_FOUNDATIONAL_IDS.issubset(registered),
            f"Faltam diferenças fundacionais: {sorted(EXPECTED_FOUNDATIONAL_IDS - registered)}.",
        )

    def test_registry_ids_are_unique_and_well_formed(self):
        ids = [entry["id"] for entry in self.entries]
        self.assertEqual(len(ids), len(set(ids)), "Há IDs WD duplicados.")
        for entry_id in ids:
            self.assertRegex(entry_id, r"^WD-\d{3}$")

    def test_every_entry_has_required_metadata_and_valid_status(self):
        for entry in self.entries:
            fields = entry["fields"]
            with self.subTest(entry=entry["id"]):
                missing = REQUIRED_FIELDS - fields.keys()
                self.assertFalse(missing, f"{entry['id']}: faltam campos {sorted(missing)}.")
                self.assertIn(
                    fields.get("Status"),
                    ALLOWED_STATUSES,
                    f"{entry['id']}: estado inválido {fields.get('Status')!r}.",
                )
                for field in REQUIRED_FIELDS:
                    self.assertTrue(fields.get(field, "").strip(), f"{entry['id']}: {field} está vazio.")

    def test_all_dependent_documents_exist_and_carry_their_registry_marker(self):
        for entry in self.entries:
            paths = document_paths(entry)
            with self.subTest(entry=entry["id"]):
                self.assertTrue(paths, f"{entry['id']}: não declara documentos dependentes.")
                for relative_path in paths:
                    path = REPO_ROOT / relative_path
                    self.assertTrue(path.is_file(), f"{entry['id']}: documento inexistente: {relative_path}.")
                    content = path.read_text(encoding="utf-8")
                    self.assertIn(
                        f"<!-- {entry['id']} -->",
                        content,
                        f"{relative_path}: falta a referência canónica <!-- {entry['id']} -->.",
                    )

    def test_world_difference_markers_never_point_to_unknown_ids(self):
        registered = {entry["id"] for entry in self.entries}
        found = set()
        for path in REPO_ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            found.update(re.findall(r"<!--\s*(WD-\d{3})\s*-->", path.read_text(encoding="utf-8")))
        self.assertEqual(
            found - registered,
            set(),
            f"Há marcadores sem entrada no registo: {sorted(found - registered)}.",
        )

    def test_every_episode_outline_and_draft_references_all_foundational_world_rules(self):
        episode_sources = sorted(
            path for path in (REPO_ROOT / "episodes").rglob("*.md")
            if path.name.endswith("_OUTLINE.md") or path.name.endswith("_DRAFT.md")
        )
        self.assertTrue(episode_sources, "Não foram encontrados outlines ou drafts de episódios.")
        for path in episode_sources:
            content = path.read_text(encoding="utf-8")
            for entry_id in EXPECTED_FOUNDATIONAL_IDS:
                with self.subTest(path=path.relative_to(REPO_ROOT), entry=entry_id):
                    self.assertIn(
                        f"<!-- {entry_id} -->",
                        content,
                        f"{path.relative_to(REPO_ROOT)} não referencia a regra global {entry_id}.",
                    )

    def test_supporting_planning_documents_reference_the_global_world_rules(self):
        required_markers = {
            "canon/STORY_DECISIONS_TO_MAKE.md": {"WD-001", "WD-002", "WD-004"},
            "canon/narrative/EPISODIC_PARALLEL_PLOTS.md": {"WD-001", "WD-004"},
            "canon/narrative/SEASON_1_ARC_PLAN.md": {"WD-001", "WD-004"},
            "canon/narrative/SERIES_GLOBAL_ARCHITECTURE.md": {"WD-001", "WD-004"},
            "canon/narrative/STORY_DEVELOPMENT_WORKFLOW.md": {"WD-001", "WD-004"},
            "canon/timeline/SEASON_1_OPENING_PLOT_BANK.md": {"WD-001", "WD-004"},
            "canon/timeline/SEASON_1_RECURRING_SCHEDULES.md": {"WD-001"},
        }
        for relative_path, expected_ids in required_markers.items():
            content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
            for entry_id in expected_ids:
                with self.subTest(path=relative_path, entry=entry_id):
                    self.assertIn(
                        f"<!-- {entry_id} -->",
                        content,
                        f"{relative_path} não referencia a regra global {entry_id}.",
                    )

    def test_story_decisions_do_not_treat_the_pilot_broadcast_as_a_parallel_world_event(self):
        content = (REPO_ROOT / "canon" / "STORY_DECISIONS_TO_MAKE.md").read_text(encoding="utf-8")
        forbidden_phrases = (
            "The Modern Family pilot aired on",
            "The pilot's broadcast date is",
            "its in-universe events are kept on that date",
            "the pilot's broadcast date",
        )
        for phrase in forbidden_phrases:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase.lower(), content.lower())

    def test_episode_outlines_do_not_use_the_unqualified_modern_family_au_shortcut(self):
        outlines = sorted((REPO_ROOT / "episodes").rglob("*_OUTLINE.md"))
        for path in outlines:
            content = path.read_text(encoding="utf-8")
            for forbidden_label in ("Modern Family AU", "Canon AU"):
                with self.subTest(path=path.relative_to(REPO_ROOT), label=forbidden_label):
                    self.assertNotIn(
                        forbidden_label,
                        content,
                        f"Usa-se {forbidden_label!r} sem distinguir série lembrada de pessoas reais no mundo paralelo.",
                    )

    def test_readme_identifies_the_parallel_world_registry(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("WORLD_DIFFERENCE_REGISTRY.md", readme)

    def test_drafts_do_not_describe_the_remembered_pilot_as_a_current_world_broadcast(self):
        forbidden_patterns = (
            r"\bthe pilot airs\b",
            r"\bpilot episode of\s+\*?Modern Family",
            r"\bsitcom reality\b",
        )
        for draft in sorted((REPO_ROOT / "episodes").rglob("*_DRAFT.md")):
            content = draft.read_text(encoding="utf-8")
            for pattern in forbidden_patterns:
                with self.subTest(draft=draft.name, pattern=pattern):
                    self.assertIsNone(
                        re.search(pattern, content, flags=re.IGNORECASE),
                        f"{draft.relative_to(REPO_ROOT)} trata um acontecimento vivido como transmissão televisiva.",
                    )


if __name__ == "__main__":
    unittest.main()
