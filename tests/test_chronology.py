"""
Testes de linearidade temporal, cronologia estrita e conformidade com o calendário de 2009/2010.
"""

import unittest
from datetime import datetime
from pathlib import Path
from tests.parser import REPO_ROOT, extract_episode_metadata, DAYS_OF_WEEK_EN, DAYS_OF_WEEK_PT

class TestStoryChronology(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.episodes_dir = REPO_ROOT / "episodes" / "season-1"
        cls.episode_files = sorted(list(cls.episodes_dir.glob("EP*_OUTLINE.md")))
        cls.parsed_episodes = [extract_episode_metadata(f) for f in cls.episode_files]

    def test_canonical_anchor_dates_2009(self):
        """Verifica se as datas canónicas e feriados/início de aulas de 2009 estão corretas no calendário."""
        # 07-09-2009: Segunda-feira (Labor Day)
        d_bday = datetime(2009, 9, 7)
        self.assertEqual(d_bday.weekday(), 0, "07/09/2009 deve ser uma Segunda-feira (Labor Day)")
        
        # 09-09-2009: Quarta-feira (Abertura do ano letivo LAUSD/Seattle)
        d_school = datetime(2009, 9, 9)
        self.assertEqual(d_school.weekday(), 2, "09/09/2009 deve ser uma Quarta-feira (Abertura oficial)")
        
        # 16-09-2009: Quarta-feira (Transferência de Nathan para a Califórnia)
        d_transfer = datetime(2009, 9, 16)
        self.assertEqual(d_transfer.weekday(), 2, "16/09/2009 deve ser Quarta-feira (Transferência)")
        
        # 23-09-2009: Quarta-feira (Episódio Piloto Modern Family)
        d_pilot = datetime(2009, 9, 23)
        self.assertEqual(d_pilot.weekday(), 2, "23/09/2009 deve ser Quarta-feira (Pilot)")

        # 30-09-2009: Quarta-feira (The Bicycle Thief)
        d_bike = datetime(2009, 9, 30)
        self.assertEqual(d_bike.weekday(), 2, "30/09/2009 deve ser Quarta-feira (The Bicycle Thief)")

    def test_episodes_chronological_ordering(self):
        """Verifica se os episódios avançam no tempo de forma linear e contínua sem saltos no passado."""
        self.assertTrue(len(self.parsed_episodes) >= 1, "Devem existir episódios registados")
        
        prev_end = None
        for ep in self.parsed_episodes:
            if ep["start_date"] and ep["end_date"]:
                self.assertLessEqual(ep["start_date"], ep["end_date"], 
                    f"No ficheiro {ep['file']}, a data de início ({ep['start_date']}) não pode ser posterior à de fim ({ep['end_date']})")
                if prev_end:
                    self.assertGreaterEqual(ep["start_date"], prev_end, 
                        f"O episódio {ep['file']} inicia em {ep['start_date']}, antes do final do anterior em {prev_end}")
                prev_end = ep["end_date"]

    def test_internal_scenes_monotonic_order(self):
        """Verifica se as cenas com datas dentro de cada outline de episódio avançam cronologicamente."""
        for ep in self.parsed_episodes:
            dates = ep["dates_in_file"]
            if len(dates) < 2:
                continue
            prev_dt, prev_raw = dates[0]
            for current_dt, current_raw in dates[1:]:
                self.assertGreaterEqual(current_dt, prev_dt, 
                    f"Regressão temporal encontrada em {ep['file']}: '{current_raw}' surge depois de '{prev_raw}'")
                prev_dt, prev_raw = current_dt, current_raw

if __name__ == '__main__':
    unittest.main()
