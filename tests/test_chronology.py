"""
Testes de cronologia não decrescente e conformidade com o calendário gregoriano real.
Valida o EVENT_REGISTRY.md e os intervalos temporais declarados nos outlines. Os drafts não são atualmente analisados por este módulo.
"""

import unittest
from datetime import datetime
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata, extract_events_from_registry

class TestStoryChronology(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*_OUTLINE.md")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episode_files]
        cls.events = extract_events_from_registry()

    def test_event_registry_gregorian_accuracy(self):
        """Verifica se todos os eventos registados em EVENT_REGISTRY.md possuem datas gregorianas válidas e dias da semana corretos."""
        self.assertGreaterEqual(len(self.events), 25, "EVENT_REGISTRY.md deve conter os eventos estruturados da temporada.")
        
        for evt in self.events:
            evt_id = evt["id"]
            dt = evt["date"]
            declared_day = evt["declared_weekday"]
            
            self.assertIsNotNone(dt, f"O evento {evt_id} deve conter uma data válida interpretável (recebeu '{evt['date_raw']}').")
            
            if declared_day:
                actual_day = dt.strftime('%a')
                self.assertEqual(
                    actual_day, declared_day,
                    f"Incoerência no calendário gregoriano em {evt_id}: {dt.strftime('%Y-%m-%d')} é {actual_day}, mas foi declarado {declared_day}."
                )

    def test_event_registry_monotonic_ordering(self):
        """Verifica se os eventos no Single Source of Truth (EVENT_REGISTRY.md) avançam cronologicamente de forma monótona sem regressões temporais."""
        prev_dt = None
        prev_id = None
        for evt in self.events:
            dt = evt["date"]
            if dt and prev_dt:
                self.assertGreaterEqual(
                    dt, prev_dt,
                    f"Regressão temporal detetada em EVENT_REGISTRY.md: {evt['id']} ({dt}) ocorre antes de {prev_id} ({prev_dt})."
                )
            if dt:
                prev_dt = dt
                prev_id = evt["id"]

    def test_registered_events_fit_their_episode_story_windows(self):
        """Cada evento e o seu intervalo completo têm de caber na janela temporal do outline correspondente."""
        episodes_by_number = {}
        for episode in self.parsed_episodes:
            match = __import__("re").match(r"^(EP\\d{2})_", episode["file"])
            if match:
                episodes_by_number[match.group(1)] = episode

        self.assertTrue(episodes_by_number, "Não foram encontrados outlines de episódios.")

        for event in self.events:
            episode = episodes_by_number.get(event["episode"])
            self.assertIsNotNone(
                episode,
                f"{event['id']}: não existe outline para {event['episode']}.",
            )
            self.assertIsNotNone(
                episode["start_date"],
                f"{event['episode']}: o outline não declara um início de story window interpretável.",
            )
            self.assertIsNotNone(
                episode["end_date"],
                f"{event['episode']}: o outline não declara um fim de story window interpretável.",
            )
            self.assertIsNotNone(event["date"], f"{event['id']}: data inicial inválida.")
            self.assertIsNotNone(event["date_end"], f"{event['id']}: data final inválida.")
            self.assertLessEqual(
                episode["start_date"],
                event["date"],
                f"{event['id']}: começa antes da story window de {event['episode']}.",
            )
            self.assertLessEqual(
                event["date_end"],
                episode["end_date"],
                f"{event['id']}: termina depois da story window de {event['episode']}.",
            )

    def test_episodes_chronological_ordering(self):
        """Verifica se os episódios avançam no tempo de forma linear e contínua sem saltos no passado."""
        self.assertTrue(len(self.parsed_episodes) >= 1, "Devem existir episódios registados")
        
        prev_end = None
        for ep in self.parsed_episodes:
            if ep["start_date"] and ep["end_date"]:
                self.assertLessEqual(
                    ep["start_date"], ep["end_date"], 
                    f"No ficheiro {ep['file']}, a data de início ({ep['start_date']}) não pode ser posterior à de fim ({ep['end_date']})"
                )
                if prev_end:
                    self.assertGreaterEqual(
                        ep["start_date"], prev_end, 
                        f"O episódio {ep['file']} inicia em {ep['start_date']}, antes do final do anterior em {prev_end}"
                    )
                prev_end = ep["end_date"]

    def test_internal_scenes_monotonic_order(self):
        """Verifica se as cenas com datas dentro de cada outline de episódio avançam cronologicamente."""
        for ep in self.parsed_episodes:
            dates = ep["dates_in_file"]
            if len(dates) < 2:
                continue
            prev_dt, prev_raw = dates[0]
            for current_dt, current_raw in dates[1:]:
                self.assertGreaterEqual(
                    current_dt, prev_dt, 
                    f"Regressão temporal encontrada em {ep['file']}: '{current_raw}' surge depois de '{prev_raw}'"
                )
                prev_dt, prev_raw = current_dt, current_raw

if __name__ == '__main__':
    unittest.main()
