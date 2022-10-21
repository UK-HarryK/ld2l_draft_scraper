import asyncio
import requests
class BaseObject:
    def __init__(self, hero_dict, team_id):
        self.b_endpoint = "https://api.opendota.com/api/"
        self.h_end = "https://api.opendota.co/api/heroes"
        self.hero_dict = hero_dict
        self.loop = asyncio.get_event_loop()
        self.team_id = team_id

   
    async def call_match(self, match_id):
        url = "https://api.opendota.com/api/matches/{}".format(str(match_id))
        response = requests.get(url)
        body = response.json()
        return body

    def hero_id_to_name(self, id):
        for x, y in self.hero_dict.items():
            if x == id:
                return y

    def determine_side(self, body):
        for x, y in body.items():
            if y == self.team_id:
                return self.parse_side(x)

    def parse_side(self, string):
        if string == "radiant_team_id":
            return 0
        elif string == "dire_team_id":
            return 1
        else:
            print(string)
            return

    async def construct_game_pick_bans(self, match_id):
        body = await self.call_match(match_id)
        draft_timings = body["picks_bans"]
        side = self.determine_side(body)
        game_picks = {}
        game_bans = {}
        for x in draft_timings:
            pick = x["is_pick"]
            order = x["order"]
            hero = x["hero_id"]
            team = x["team"]
            hero = self.hero_id_to_name(str(x["hero_id"]))
            if team == side:
                if pick:
                    game_picks.update({hero: order})
                else:
                    game_bans.update({hero: order})
        return game_picks, game_bans



