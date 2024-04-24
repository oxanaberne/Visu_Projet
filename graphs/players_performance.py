from .graph_performance import *

attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]


def attackers_perf(players_data):
    attackers_data = filter_players_by_position(players_data, attackers)

    all_players = set()
    for match_data in attackers_data.values():
        all_players.update(match_data.keys())

    transformed_data = {player: [] for player in all_players}

    for match_number in range(1, len(attackers_data) + 1):
        match_key = f'Match {match_number}'
        match_data = attackers_data.get(match_key, {})
        
        for player in all_players:
            stats = match_data.get(player, [{}])[0]
            shots = stats.get('shots', 0)
            shots_on_target = stats.get('shots_on_target', 0)
            goals = stats.get('goals', 0)
            
            transformed_data[player].append((shots, shots_on_target, goals))
    return draw_graph_attackers(transformed_data)

def mid_perf(players_data):
    midfielders_data = filter_players_by_position(players_data, midfielders)
    all_players = set()
    for match_data in midfielders_data.values():
        all_players.update(match_data.keys())

    transformed_data = {player: [] for player in all_players}

    for match_number in range(1, len(midfielders_data) + 1):
        match_key = f'Match {match_number}'
        match_data = midfielders_data.get(match_key, {})
        
        for player in all_players:
            stats = match_data.get(player, [{}])[0]
            crosses = stats.get('crosses', 0)
            tackles = stats.get('tackles_won', 0)
            interceptions = stats.get('interceptions', 0)
            assists = stats.get('assists', 0)
            # Passe, Centres, Interception, Tacles
            transformed_data[player].append((assists, crosses, interceptions, tackles))
    return draw_graph_mid(transformed_data)


def defenders_perf(players_data):
    defenders_data = filter_players_by_position(players_data, defenders)
    all_players = set()
    for match_data in defenders_data.values():
        all_players.update(match_data.keys())

    transformed_data = {player: [] for player in all_players}

    for match_number in range(1, len(defenders_data) + 1):
        match_key = f'Match {match_number}'
        match_data = defenders_data.get(match_key, {})
        
        for player in all_players:
            stats = match_data.get(player, [{}])[0]
            tackles = stats.get('tackles_won', 0)
            interceptions = stats.get('interceptions', 0)
            # Interception, Tacles
            transformed_data[player].append((interceptions, tackles))
    return draw_graph_defenders(transformed_data)


def filter_players_by_position(players_data, position_group):
    filtered_data = {}
    for nbMatch, matchStat in players_data.items():
        filtered_data[nbMatch] = {}
        for playerName, stats in matchStat.items():
            for stat in stats:
                if any(pos in position_group for pos in stat["position"]):
                    if playerName not in filtered_data:
                        filtered_data[nbMatch][playerName] = []
                    filtered_data[nbMatch][playerName].append(stat)
    return filtered_data
