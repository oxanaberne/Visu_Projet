from .graph_performance import *
import os
import csv
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]


def attackers_perf(players_data):
    attackers_data = filter_players_by_position(players_data, attackers)
    processed_data = {
        player: [
            (stat["shots"], stat["shots_on_target"], stat["goals"]) for stat in stats
        ]
        for player, stats in attackers_data.items()
    }
    return draw_graph_attackers(processed_data)

def mid_perf(players_data):
    midfielders_data = filter_players_by_position(players_data, midfielders)
    processed_data = {
        player: [
            (
                stat["crosses"],
                stat["tackles_won"],
                stat["interceptions"],
                stat["assists"],
            )
            for stat in stats
        ]
        for player, stats in midfielders_data.items()
    }
    return draw_graph_mid(processed_data)


def defenders_perf(players_data):
    defenders_data = filter_players_by_position(players_data, defenders)
    processed_data = {
        player: [(stat["tackles_won"], stat["interceptions"]) for stat in stats]
        for player, stats in defenders_data.items()
    }
    return draw_graph_defenders(processed_data)


def filter_players_by_position(players_data, position_group):
    filtered_data = {}
    for player, stats in players_data.items():
        for stat in stats:
            if any(pos in position_group for pos in stat["position"]):
                if player not in filtered_data:
                    filtered_data[player] = []
                filtered_data[player].append(stat)
    return filtered_data
