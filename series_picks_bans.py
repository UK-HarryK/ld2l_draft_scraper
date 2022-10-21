# This needs refactoring so badly
# Combine ban pick aggregate into one function/init
# 
from base_object import BaseObject
import asyncio
class SeriesPicksBans(BaseObject):
# pass in match ids 
    def __init__(self, heroes_dict ,match_id_1, match_id_2):
        super().__init__(heroes_dict)
        self.match_id_1 = match_id_1
        self.match_id_2 = match_id_2
        self.loop = asyncio.get_event_loop()
        self.g1p, self.g1b = self.loop.run_until_complete(super().construct_game_pick_bans(match_id_1))
        self.g2p, self.g2b = self.loop.run_until_complete(super().construct_game_pick_bans(match_id_2))
        self.total_picks = {}
        self.total_bans = {}

    def create_series_total_picks(self):
        m = lambda a : a + 1
        for x, y in self.g1p.items():
            if x in self.g2p.keys():
                self.total_picks[x] = {
                    "picks": 2,
                    "order": [m(y), m(self.g2p[x])]
                }
            else:
                self.total_picks[x] = {
                    "picks": 1,
                    "order": [m(y)]
                }
        for x, y in self.g2p.items():
            if x in self.total_picks.keys():
                continue
            else:
                self.total_picks[x] = {
                    "picks": 1,
                    "order": [m(y)]
                }
    
    def create_series_total_bans(self):
        m = lambda a : a + 1
        for x, y in self.g1b.items():
            if x in self.g2b.keys():
                self.total_bans[x] = {
                    "bans": 2,
                    "order": [m(y), m(self.g2b[x])]
                }
            else:
                self.total_bans[x] = {
                    "bans": 1,
                    "order": [m(y)]
                }
        for x, y in self.g2b.items():
            if x in self.total_bans.keys():
                continue
            else:
                self.total_bans[x] = {
                    "picks": 1,
                    "order": [m(y)]
                }

                