from series_picks_bans import SeriesPicksBans
import requests
from combine_games import combine_games
from dataset_helper import compile_and_export
match_id_1 = 6765358371
match_id_2 = 6765415313
match_id_3 = 6776639740
match_id_4 = 6776690997
match_id_5 = 6787702053
match_id_6 = 6787780025
match_id_7 = 6798618459
match_id_8 = 6798673814
match_id_9 = 6809242014
match_id_10 = 6809293511

# 8820557 team id

def call_heroes_list():
     url = "https://api.opendota.com/api/heroes"
     response = requests.get(url)
     heroes_dict = {}
     for x in response.json():
         heroes_dict.update({str(x["id"]): x["localized_name"]})
     return heroes_dict
heroes = call_heroes_list()


week1 = SeriesPicksBans(heroes, match_id_1, match_id_2, 8820557)
week2 = SeriesPicksBans(heroes, match_id_3, match_id_4, 8820557)
week3 = SeriesPicksBans(heroes, match_id_5, match_id_6, 8820557)
week4 = SeriesPicksBans(heroes, match_id_7, match_id_8, 8820557)
week5 = SeriesPicksBans(heroes, match_id_9, match_id_10, 8820557)
week1.create_series_total_picks()
week1.create_series_total_bans()
week2.create_series_total_picks()
week2.create_series_total_bans()
week3.create_series_total_picks()
week3.create_series_total_bans()
week4.create_series_total_picks()
week4.create_series_total_bans()
week5.create_series_total_picks()
week5.create_series_total_bans()
gotham_picks, gotham_bans = combine_games(week1, week2, week3, week4, week5)

compile_and_export(gotham_picks, gotham_bans)