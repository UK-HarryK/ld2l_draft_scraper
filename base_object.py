import asyncio
import requests
class BaseObject:
    def __init__(self, hero_dict):
        self.b_endpoint = "https://api.opendota.com/api/"
        self.h_end = "https://api.opendota.co/api/heroes"
        self.hero_dict = hero_dict
        self.loop = asyncio.get_event_loop()

   
    async def call_match(self, match_id):
        url = "https://api.opendota.com/api/matches/{}".format(str(match_id))
        response = requests.get(url)
        body = response.json()
        return body["picks_bans"]

    def hero_id_to_name(self, id):
        for x, y in self.hero_dict.items():
            if x == id:
                return y

    async def construct_game_pick_bans(self, match_id, radient):
        draft_timings = await self.call_match(match_id)
        game_picks = {}
        game_bans = {}
        for x in draft_timings:
            pick = x["is_pick"]
            order = x["order"]
            hero = x["hero_id"]
            team = x["team"]
            hero = self.hero_id_to_name(str(x["hero_id"]))
            if team != radient:
                if pick:
                    game_picks.update({hero: order})
                else:
                    game_bans.update({hero: order})
        return game_picks, game_bans



