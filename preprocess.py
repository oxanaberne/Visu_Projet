import os
import csv
import pathlib
import data.results_matchs_subs_data as rm

BASE_DIR = pathlib.Path(__file__).parent
attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]

def getPlayersData():
    playersData = {}
    match_1 = getPlayersDataByMatch("Match 1 - Guinea-Bissau")
    playersData['Match 1'] = createDictForPlayersInMatch(match_1)

    match_2 = getPlayersDataByMatch("Match 2 - Nigeria")
    playersData['Match 2'] = createDictForPlayersInMatch(match_2)

    match_3 = getPlayersDataByMatch("Match 3 - Equatorial-Guinea")
    playersData['Match 3'] = createDictForPlayersInMatch(match_3)

    match_4 = getPlayersDataByMatch("Match 4 - Senegal")
    playersData['Match 4'] = createDictForPlayersInMatch(match_4)

    match_5 = getPlayersDataByMatch("Match 5 - Mali")
    playersData['Match 5'] = createDictForPlayersInMatch(match_5)

    match_6 = getPlayersDataByMatch("Match 6 - Congo DR")
    playersData['Match 6'] = createDictForPlayersInMatch(match_6)

    match_7 = getPlayersDataByMatch("Match 7 - Nigeria")
    playersData['Match 7'] = createDictForPlayersInMatch(match_7)
    return playersData

def createDictForPlayersInMatch(match):
    dict = {}
    for name, stat in match.items():
        if name in dict:
            dict[name] += stat
        else:
            dict[name] = stat
    return dict

def getPlayersDataByMatch(match):
    filename = os.path.join(BASE_DIR, f"data/{match}/", "df3.csv")

    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=";")
        data_list = list(reader)

    players_stats = {}
    for line in data_list[1:]:  # Skip the header
        player = line[0]

        players_stats[player] = [
            {
                "position": list(line[2].split(",")),
                "shots": int(line[9]),
                "shots_on_target": int(line[10]),
                "goals": int(line[5]),
                "assists": int(line[6]),
                "crosses": int(line[16]),
                "tackles_won": int(line[17]),
                "interceptions": int(line[18]),
                "isSub": ifPlayerSub(match, player)

            }
        ]

    return players_stats


def getPlayersGlobalPerformances():
    filename = os.path.join(
        BASE_DIR, f"data/Global performances/", "standard_stats.csv"
    )

    with open(filename, "r") as f:
        reader = csv.reader(f, delimiter=";")
        standard_data_list = list(reader)

    players_stats = {}
    for line in standard_data_list[1:25]:  # Skip the header
        player = line[0]

        players_stats[player] = [
            {
                "position": list(line[1].split(",")),
                "goals": int(float(line[4])),
                "assists": int(float(line[5])),
                "shots": int(float(line[9])),
                "shots_on_target": int(float(line[10])),
                "crosses": int(float(line[6])),
                "tackles_won": int(float(line[8])),
                "interceptions": int(float(line[7])),
                "isSub": True
            }
        ]
    return {'Global': players_stats}

def ifPlayerSub(match, player):
    data = rm.data
    format_match = match.split(" - ")[0]
    for data_match, stats in data.items():
        if data_match == format_match:
            if(player in stats['Players']):
                return True
    return False
