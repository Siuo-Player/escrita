"""
Testes de alinhamento entre EVENT_REGISTRY.md e os documentos que este declara como dependentes.

A suite não tenta inferir semântica literária: valida integridade estrutural,
referências, datas e associação dos eventos às janelas temporais dos episódios.
"""

import re
import unittest

from tests.parser import (
    REPO_ROOT,
    extract_episode_metadata,
    extract_events_from_registry,
    parse_event_registry_content,
)


class TestEventRegistryAlignment(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.events = extract_events_from_registry()
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.outlines = {}
        for path in sorted(cls.episodes_dir.glob("EP*_OUTLINE.md")):
            match = re.match(r"^(EP\d{2})_", path.name)
            if match:
                cls.outlines[match.group(1)] = extract_episode_metadata(path)

    def test_event_ids_are_unique_and_contiguous(self):
        """Impede IDs duplicados, saltos e linhas do registo que não sejam interpretadas."""
        self.assertTrue(self.events, "EVENT_REGISTRY.md não pode estar vazio.")
        event_ids = [event["id"] for event in self.events]
        self.assertEqual(
            len(event_ids),
            len(set(event_ids)),
            "EVENT_REGISTRY.md contém Event IDs duplicados.",
        )
        expected = [f"EVT-{number:03d}" for number in range(1, len(event_ids) + 1)]
        self.assertEqual(
            event_ids,
            expected,
            "Os Event IDs devem estar ordenados e ser contíguos; uma linha malformada também pode ter sido ignorada pelo parser.",
        )

    def test_every_event_maps_to_a_real_episode_and_valid_date_interval(self):
        """Cada evento tem de pertencer a um outline existente e caber na respetiva story window."""
        for event in self.events:
            event_id = event["id"]
            episode = event["episode"].strip()
            self.assertRegex(episode, r"^EP\d{2}$", f"{event_id}: código de episódio inválido: {episode!r}.")
            self.assertIn(episode, self.outlines, f"{event_id}: não existe outline para {episode}.")
            self.assertIsNotNone(event["date"], f"{event_id}: data inicial inválida: {event['date_raw']!r}.")
            self.assertIsNotNone(event["date_end"], f"{event_id}: data final inválida: {event['date_raw']!r}.")

            start = event["date"]
            end = event["date_end"]
            self.assertLessEqual(start, end, f"{event_id}: intervalo invertido ({start} > {end}).")

            episode_data = self.outlines[episode]
            self.assertIsNotNone(episode_data["start_date"], f"{episode}: story window sem início interpretável.")
            self.assertIsNotNone(episode_data["end_date"], f"{episode}: story window sem fim interpretável.")
            self.assertLessEqual(
                episode_data["start_date"],
                start,
                f"{event_id}: começa em {start.date()}, antes da story window de {episode} ({episode_data['story_window']}).",
            )
            self.assertLessEqual(
                end,
                episode_data["end_date"],
                f"{event_id}: termina em {end.date()}, depois da story window de {episode} ({episode_data['story_window']}).",
            )

    def test_declared_weekdays_match_both_ends_of_date_ranges(self):
        """Verifica o dia da semana real também na segunda data dos intervalos abreviados."""
        for event in self.events:
            for key, declared_key in (
                ("date", "declared_weekday"),
                ("date_end", "declared_weekday_end"),
            ):
                dt = event[key]
                declared = event[declared_key]
                if dt and declared:
                    actual = dt.strftime("%a")
                    self.assertEqual(
                        actual,
                        declared,
                        f"{event['id']}: {dt.date()} é {actual}, não {declared}.",
                    )

    def test_all_declared_dependent_documents_exist_exactly_once(self):
        """Cada nome em Dependent Documents tem de resolver para um único ficheiro real."""
        for event in self.events:
            self.assertTrue(event["dependent_docs"], f"{event['id']}: não declara documentos dependentes.")
            for document_name in event["dependent_docs"]:
                matches = [
                    path for path in REPO_ROOT.rglob(document_name)
                    if path.is_file()
                ]
                self.assertEqual(
                    len(matches),
                    1,
                    f"{event['id']}: {document_name!r} devia resolver para um ficheiro único; encontrados: {matches}.",
                )

            episode = event["episode"]
            has_episode_anchor = any(
                name.startswith(episode + "_")
                and (name.endswith("_OUTLINE.md") or name.endswith("_DRAFT.md"))
                for name in event["dependent_docs"]
            )
            self.assertTrue(
                has_episode_anchor,
                f"{event['id']}: os documentos dependentes não incluem outline nem draft de {episode}.",
            )

    def test_every_registered_event_has_one_exact_anchor_in_its_primary_outline(self):
        """Cada evento tem uma âncora explícita no outline do episódio e a data copiada coincide com o registo."""
        anchor_pattern = re.compile(
            r"<!--\s*(EVT-\d{3})\s*\|\s*(20\d{2}-\d{2}-\d{2})"
            r"\s*\|\s*(20\d{2}-\d{2}-\d{2})\s*-->"
        )
        anchors_by_id = {}
        for episode, outline in self.outlines.items():
            content = outline["path"].read_text(encoding="utf-8")
            for line_number, line in enumerate(content.splitlines(), start=1):
                for match in anchor_pattern.finditer(line):
                    self.assertRegex(
                        line,
                        r"^\s*#{1,6}\s",
                        f"{episode}:{line_number}: a âncora do evento tem de estar associada a um heading Markdown.",
                    )
                    event_id, date_start, date_end = match.groups()
                    anchors_by_id.setdefault(event_id, []).append(
                        (episode, date_start, date_end)
                    )

        registered_ids = {event["id"] for event in self.events}
        self.assertEqual(
            set(anchors_by_id),
            registered_ids,
            "As âncoras nos outlines têm de corresponder exatamente aos eventos do EVENT_REGISTRY.md.",
        )

        for event in self.events:
            event_id = event["id"]
            anchors = anchors_by_id.get(event_id, [])
            self.assertEqual(
                len(anchors),
                1,
                f"{event_id}: esperado exatamente um anchor nos outlines; encontrados {anchors}.",
            )
            episode, date_start, date_end = anchors[0]
            self.assertEqual(
                episode,
                event["episode"],
                f"{event_id}: a âncora está em {episode}, mas o registo associa-a a {event['episode']}.",
            )
            self.assertEqual(
                date_start,
                event["date"].strftime("%Y-%m-%d"),
                f"{event_id}: a data inicial da âncora diverge do EVENT_REGISTRY.md.",
            )
            self.assertEqual(
                date_end,
                event["date_end"].strftime("%Y-%m-%d"),
                f"{event_id}: a data final da âncora diverge do EVENT_REGISTRY.md.",
            )

    def test_parser_reports_invalid_gregorian_dates(self):
        """Datas impossíveis têm de produzir um diagnóstico e não podem ser aceites como eventos válidos."""
        malformed_registry = """
| Event ID | Date | Episode | Location | Characters | Trigger | Action | Result | Dependent Documents |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **EVT-001** | **2009-02-30 (Mon)** | **EP01** | Seattle | Nathan | Birthday | Opens game | Flow field started | `EP01_BEFORE_AND_AFTER_OUTLINE.md` |
"""
        parsed_events, issues = parse_event_registry_content(malformed_registry)
        self.assertEqual(len(parsed_events), 1)
        self.assertIsNone(parsed_events[0]["date"])
        self.assertTrue(
            any("data ISO inválida" in issue for issue in issues),
            f"A data impossível devia produzir um diagnóstico; recebido: {issues}",
        )

    def test_canonical_registry_contains_no_malformed_event_rows(self):
        """Nenhuma linha com EVT- pode desaparecer silenciosamente durante o parsing."""
        registry_path = REPO_ROOT / "canon" / "narrative" / "EVENT_REGISTRY.md"
        registry_content = registry_path.read_text(encoding="utf-8")
        parsed_events, issues = parse_event_registry_content(registry_content)
        self.assertEqual(issues, [], "EVENT_REGISTRY.md contém linhas malformadas.")
        self.assertEqual(
            len(parsed_events),
            len(self.events),
            "O número de linhas de evento parseadas tem de coincidir com os eventos expostos pelo parser.",
        )

    def test_parser_reports_a_malformed_final_event_row(self):
        """Uma última linha truncada também tem de ser detetada, mesmo sem um ID seguinte que revele o salto."""
        malformed_registry = """
| Event ID | Date | Episode | Location | Characters | Trigger | Action | Result | Dependent Documents |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **EVT-001** | **2009-09-07 (Mon)** | **EP01** | Seattle | Nathan | Birthday | Opens game | Flow field started |
"""
        parsed_events, issues = parse_event_registry_content(malformed_registry)
        self.assertEqual(parsed_events, [])
        self.assertTrue(
            any("9 colunas" in issue for issue in issues),
            f"A linha incompleta devia gerar um erro explícito; recebido: {issues}",
        )

    def test_every_outline_has_at_least_one_registered_event(self):
        """Evita outlines de episódios que não aparecem na cronologia canónica."""
        represented_episodes = {event["episode"] for event in self.events}
        for episode in self.outlines:
            self.assertIn(
                episode,
                represented_episodes,
                f"{episode} existe como outline, mas não tem qualquer evento em EVENT_REGISTRY.md.",
            )


if __name__ == "__main__":
    unittest.main()
