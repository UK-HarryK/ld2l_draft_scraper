from series_picks_bans import SeriesPicksBans
import requests
from combine_games import combine_games
match_id_1 = 6765358371
match_id_2 = 6765415313
match_id_3 = 6776639740
match_id_4 = 6776690997

def call_heroes_list():
     url = "https://api.opendota.com/api/heroes"
     response = requests.get(url)
     heroes_dict = {}
     for x in response.json():
         heroes_dict.update({str(x["id"]): x["localized_name"]})
     return heroes_dict
heroes = call_heroes_list()


week1 = SeriesPicksBans(heroes, match_id_1, match_id_2, False, False)
week2 = SeriesPicksBans(heroes, match_id_3, match_id_4, True, True)
week1.create_series_total_picks()
week1.create_series_total_bans()
week2.create_series_total_picks()
week2.create_series_total_bans()
gotham_picks = combine_games(week1, week2)
print(gotham_picks)