"""
Testes de alinhamento entre EVENT_REGISTRY.md e os documentos que este declara como dependentes.

A suite não tenta inferir semântica literária: valida integridade estrutural,
referências, datas e associação dos eventos às janelas temporais dos episódios.
"""

import re
import unittest

from tests.parser import REPO_ROOT, extract_episode_metadata, extract_events_from_registry


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
