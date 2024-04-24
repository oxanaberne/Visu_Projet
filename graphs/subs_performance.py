from .graph_performance import *
from data.preprocess_performance_data import *

def attackersSubPerformances():
    data = getDataByPlayerPositions('attackers', True)
    return drawGraphAttackers(data)

def midfieldersSubPerformances():
    data = getDataByPlayerPositions('midfielders', True)
    return drawGraphMid(data)

def defendersSubPerformances():
    data = getDataByPlayerPositions('defenders', True)
    return drawGraphDefenders(data)