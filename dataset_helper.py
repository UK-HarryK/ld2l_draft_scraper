import pandas as pd

def pull_num_picks_bans(tpicks, tbans):
    picks = []
    p_order = []
    bans = []
    b_order = []
    for y in tpicks.values():
        picks.append(y["picks"])
        p_order.append(y["order"])
    for y in tbans.values():
        bans.append(y["bans"])
        b_order.append(y["order"])
        
    return picks, p_order, bans, b_order


def build_df(list, heroes_list, order, picks):
    if picks == True:
        df = pd.DataFrame({"Picks": list, "DraftOrder": order}, index=heroes_list)
        df_sorted = df.sort_values("Picks", ascending=False)
    else:
        df = pd.DataFrame({"Bans": list, "DraftOrder": order}, index=heroes_list)
        df_sorted = df.sort_values("Bans", ascending=False)
    return df_sorted


def compile_and_export(picks, bans):
    
    heroes_p = list(picks.keys())
    heroes_b = list(bans.keys())
    values_p, orders_p, values_b, orders_b = pull_num_picks_bans(picks, bans)

    p_data = build_df(values_p, heroes_p, orders_p, True)
    b_data = build_df(values_b, heroes_b, orders_b, False)

    p_data.to_csv(r'~/Documents/export_picks.csv', header=True)
    b_data.to_csv(r'~/Documents/export_bans.csv', header=True)





