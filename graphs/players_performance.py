from .graph_performance import *
from data.preprocess_performance_data import *

def attackersPerformances():
    data = getDataByPlayerPositions('attackers', False)
    return drawGraphAttackers(data)

def midfieldersPerformances():
    data = getDataByPlayerPositions('midfielders', False)
    return drawGraphMid(data)

def defendersPerformances():
    data = getDataByPlayerPositions('defenders', False)
    return drawGraphDefenders(data)