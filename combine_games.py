def combine_games(*games):
    hero_p = []
    hero_b = []
    picks = {}
    bans = {}
    
    for x in games:
        for y in x.total_picks:
            if y not in hero_p:
                hero_p.append(y)

    # for x in games:
    #     for y in x.total_bans:
    #         if y not in hero_b:
    #             hero_b.append(y)

    for x in hero_p:
        picks[x] = {
            "picks": 0,
            "order": []
        }

    # for x in hero_b:
    #     bans[x] = {
    #         "bans": 0,
    #         "order": []
    #     }

    for a in games:
        for x, y in a.total_picks.items():
            picks[x]["picks"] = picks[x]["picks"] + y["picks"]
            picks[x]["order"].extend(y["order"])
    
    # for a in games:
    #     for x, y in a.total_bans.items():
    #         bans[x]["bans"] = bans[x]["bans"] + y["bans"]
    #         bans[x]["order"].extend(y["order"])

    return picks