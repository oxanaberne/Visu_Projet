import os
import csv
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]

def getPlayersData():
    playersData = {}
    match_1 = getPlayersDataByMatch("Match 1 - Guinea-Bissau")
    match_2 = getPlayersDataByMatch("Match 2 - Nigeria")
    match_3 = getPlayersDataByMatch("Match 3 - Equatorial-Guinea")
    match_4 = getPlayersDataByMatch("Match 4 - Senegal")
    match_5 = getPlayersDataByMatch("Match 5 - Mali")
    match_6 = getPlayersDataByMatch("Match 6 - Congo DR")
    match_7 = getPlayersDataByMatch("Match 7 - Nigeria")

    matches = [match_1, match_2, match_3, match_4, match_5, match_6, match_7]

    for player in matches:
        for key, value in player.items():
            if key in playersData:
                playersData[key] += value
            else:
                playersData[key] = value
    return playersData


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
            }
        ]
    return players_stats