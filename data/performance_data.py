from graphs.graph_performance import *

def process_attackers_perf(attackers_data):
    all_players = set()
    for match_data in attackers_data.values():
        all_players.update(match_data.keys())
    transformed_data = {player: [] for player in all_players}

    for match_number, players in attackers_data.items():
        for player in all_players:
            if player in players:
                shots = players[player]['shots']
                shots_on_target = players[player]['shots_on_target']
                goals = players[player]['goals']
                transformed_data[player].append((shots, shots_on_target, goals))
            else:
                transformed_data[player].append((0, 0, 0))
            if len(transformed_data[player]) == 8 and isRecordEmpty(transformed_data[player]):
                del transformed_data[player]
            
    return transformed_data

def process_mid_perf(midfielders_data):
    all_players = set()
    for match_data in midfielders_data.values():
        all_players.update(match_data.keys())
    transformed_data = {player: [] for player in all_players}

    for match_number, players in midfielders_data.items():
        for player in all_players:
            if player in players:
                crosses = players[player]['crosses']
                tackles = players[player]['tackles_won']
                interceptions = players[player]['interceptions']
                assists = players[player]['assists']
                # Passe, Centres, Interception, Tacles
                transformed_data[player].append((assists, crosses, interceptions, tackles))
            else:
                transformed_data[player].append((0, 0, 0, 0))
            if len(transformed_data[player]) == 8 and isRecordEmpty(transformed_data[player]):
                del transformed_data[player]
                
    return transformed_data

def process_defenders_perf(defenders_data):
    all_players = set()
    for match_data in defenders_data.values():
        all_players.update(match_data.keys())

    transformed_data = {player: [] for player in all_players}

    for match_number, players in defenders_data.items():
        for player in all_players:
            if player in players:
                tackles = players[player]['tackles_won']
                interceptions = players[player]['interceptions']
                # Interception, Tacles
                transformed_data[player].append((interceptions, tackles))
            else:
                transformed_data[player].append((0, 0))
            if len(transformed_data[player]) == 8 and isRecordEmpty(transformed_data[player]):
                del transformed_data[player]

    return transformed_data

def filter_players_by_position(players_data, position_group, IsSub):
    filtered_data = {}
    for nbMatch, matchStat in players_data.items():
        filtered_data[nbMatch] = {}
        for playerName, stats in matchStat.items():
            if IsSub and any(pos in position_group for pos in stats["position"]) and stats["isSub"]:
                if playerName not in filtered_data:
                    filtered_data[nbMatch][playerName] = {}
                filtered_data[nbMatch][playerName].update(stats)
            if not IsSub and any(pos in position_group for pos in stats["position"]) and not stats["isSub"]:
                if playerName not in filtered_data:
                    filtered_data[nbMatch][playerName] = {}
                filtered_data[nbMatch][playerName].update(stats)
    return filtered_data

def isRecordEmpty(data):
    return all(all(valeur == 0 for valeur in tuple) for tuple in data)