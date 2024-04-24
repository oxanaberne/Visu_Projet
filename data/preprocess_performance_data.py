import os
import csv
import pathlib
import data.results_matchs_subs_data as rm
from graphs.graph_performance import *

BASE_DIR = pathlib.Path(__file__).parent.parent
attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]

def getDataByPlayerPositions(position, IsSub):
    data = getPlayersData()
    if position == 'attackers':
        attackersData = filterDataByPosition(data, attackers, IsSub)
        return formatDataAttackers(attackersData)
    elif position == 'midfielders':
        midfieldersData = filterDataByPosition(data, midfielders, IsSub)
        return formatDataMidfielders(midfieldersData)
    else:
        defendersData = filterDataByPosition(data, defenders, IsSub)
        return formatDataDefenders(defendersData)

def filterDataByPosition(data, positionGroup, IsSubGraph):
    filteredData = {}
    for nbMatch, matchStat in data.items():
        filteredData[nbMatch] = {}
        for playerName, stats in matchStat.items():
            IsPlayerInPositionGroupe = any(pos in positionGroup for pos in stats["position"])
            IsPlayerASub = stats["isSub"]
                
            if IsSubGraph and IsPlayerInPositionGroupe and IsPlayerASub:
                if playerName not in filteredData:
                    filteredData[nbMatch][playerName] = {}
                filteredData[nbMatch][playerName].update(stats)
            if not IsSubGraph and IsPlayerInPositionGroupe and not IsPlayerASub:
                if playerName not in filteredData:
                    filteredData[nbMatch][playerName] = {}
                filteredData[nbMatch][playerName].update(stats)
    return filteredData

def formatDataAttackers(attackersData):
    allPlayers = set()
    for matchData in attackersData.values():
        allPlayers.update(matchData.keys())
    transformedData = {player: [] for player in allPlayers}

    for players in attackersData.values():
        for player in allPlayers:
            if player in players:
                shots = players[player]['shots']
                shotsOnTarget = players[player]['shots_on_target']
                goals = players[player]['goals']
                transformedData[player].append((shots, shotsOnTarget, goals))
            else:
                transformedData[player].append((0, 0, 0))
            if len(transformedData[player]) == 8 and isRecordEmpty(transformedData[player]):
                del transformedData[player]
            
    return transformedData

def formatDataMidfielders(midfieldersData):
    allPlayers = set()
    for matchData in midfieldersData.values():
        allPlayers.update(matchData.keys())
    transformedData = {player: [] for player in allPlayers}

    for players in midfieldersData.values():
        for player in allPlayers:
            if player in players:
                assists = players[player]['assists']
                crosses = players[player]['crosses']
                interceptions = players[player]['interceptions']
                tackles = players[player]['tackles_won']
                # Passe, Centres, Interception, Tacles
                transformedData[player].append((assists, crosses, interceptions, tackles))
            else:
                transformedData[player].append((0, 0, 0, 0))
            if len(transformedData[player]) == 8 and isRecordEmpty(transformedData[player]):
                del transformedData[player]
                
    return transformedData

def formatDataDefenders(defendersData):
    allPlayers = set()
    for matchData in defendersData.values():
        allPlayers.update(matchData.keys())

    transformedData = {player: [] for player in allPlayers}

    for players in defendersData.values():
        for player in allPlayers:
            if player in players:
                interceptions = players[player]['interceptions']
                tackles = players[player]['tackles_won']
                # Interception, Tacles
                transformedData[player].append((interceptions, tackles))
            else:
                transformedData[player].append((0, 0))
            if len(transformedData[player]) == 8 and isRecordEmpty(transformedData[player]):
                del transformedData[player]

    return transformedData


def isRecordEmpty(data):
    return all(all(valeur == 0 for valeur in tuple) for tuple in data)

def getPlayersData():
    playersData = {}
    match1 = getPlayersDataByMatch("Match 1 - Guinea-Bissau")
    playersData['Match 1'] = createDictForPlayersInMatch(match1)

    match2 = getPlayersDataByMatch("Match 2 - Nigeria")
    playersData['Match 2'] = createDictForPlayersInMatch(match2)

    match3 = getPlayersDataByMatch("Match 3 - Equatorial-Guinea")
    playersData['Match 3'] = createDictForPlayersInMatch(match3)

    match4 = getPlayersDataByMatch("Match 4 - Senegal")
    playersData['Match 4'] = createDictForPlayersInMatch(match4)

    match5 = getPlayersDataByMatch("Match 5 - Mali")
    playersData['Match 5'] = createDictForPlayersInMatch(match5)

    match6 = getPlayersDataByMatch("Match 6 - Congo DR")
    playersData['Match 6'] = createDictForPlayersInMatch(match6)

    match7 = getPlayersDataByMatch("Match 7 - Nigeria")
    playersData['Match 7'] = createDictForPlayersInMatch(match7)
    playersData['Global'] = getPlayersGlobalPerformances()
    return playersData

def getPlayersDataByMatch(match):
    filename = os.path.join(BASE_DIR, f"data/{match}/", "df3.csv")
    with open(filename, "r") as f:
        dataList = list(csv.reader(f, delimiter=";"))

    playersStats = {}
    for line in dataList[1:]:
        player = line[0]
        playersStats[player] = {
                "position": list(line[2].split(",")),
                "shots": int(line[9]),
                "shots_on_target": int(line[10]),
                "goals": int(line[5]),
                "assists": int(line[6]),
                "crosses": int(line[16]),
                "tackles_won": int(line[17]),
                "interceptions": int(line[18]),
                "isSub": isPlayerASub(match, player)
            }
    
    return playersStats

def getPlayersGlobalPerformances():
    filename = os.path.join(
        BASE_DIR, f"data/Global performances/", "standard_stats.csv"
    )

    with open(filename, "r") as f:
        dataList = list(csv.reader(f, delimiter=";"))

    playersStats = {}
    for line in dataList[1:25]:
        player = line[0]
        playersStats[player] = {
                "position": list(line[1].split(",")),
                "goals": int(float(line[4])),
                "assists": int(float(line[5])),
                "shots": int(float(line[9])),
                "shots_on_target": int(float(line[10])),
                "crosses": int(float(line[6])),
                "tackles_won": int(float(line[8])),
                "interceptions": int(float(line[7])),
                "isSub": False
            }
    
    return playersStats

def isPlayerASub(match, player):
    data = rm.data
    matchFormat = match.split(" - ")[0]
    for matchData, stats in data.items():
        isPlayerInStats = player in stats['Players']
        if matchData == matchFormat and isPlayerInStats:
            return True
    return False

def createDictForPlayersInMatch(match):
    dict = {}
    for name, stat in match.items():
        if name in dict:
            dict[name] += stat
        else:
            dict[name] = stat
    return dict