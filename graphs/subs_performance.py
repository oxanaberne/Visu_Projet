from .graph_performance import *
from data.performance_data import *

attackers = ["LW", "RW", "FW"]
defenders = ["CB", "FB", "LB", "RB", "DF"]
midfielders = ["DM", "CM", "LM", "RM", "WM", "AM", "MF"]

def attackers_perf(players_data):
    attackers_data = filter_players_by_position(players_data, attackers, True)
    transformed_data = process_attackers_perf(attackers_data)
    return draw_graph_attackers(transformed_data)

def mid_perf(players_data):
    midfielders_data = filter_players_by_position(players_data, midfielders, True)
    transformed_data = process_mid_perf(midfielders_data)
    return draw_graph_mid(transformed_data)

def defenders_perf(players_data):
    defenders_data = filter_players_by_position(players_data, defenders, True)
    transformed_data = process_defenders_perf(defenders_data)
    return draw_graph_defenders(transformed_data)