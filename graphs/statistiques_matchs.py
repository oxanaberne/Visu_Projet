import pathlib
import pandas as pd # type: ignore
import plotly.graph_objects as go # type: ignore
import os
import csv

BASE_DIR = pathlib.Path(__file__).parent.parent

def plotStatMatch1():
    filename = os.path.join(BASE_DIR, 'data/Match 1 - Guinea-Bissau/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch2():
    filename = os.path.join(BASE_DIR, 'data/Match 2 - Nigeria/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch3():
    filename = os.path.join(BASE_DIR, 'data/Match 3 - Equatorial-Guinea/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch4():
    filename = os.path.join(BASE_DIR, 'data/Match 4 - Senegal/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch5():
    filename = os.path.join(BASE_DIR, 'data/Match 5 - Mali/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch6():
    filename = os.path.join(BASE_DIR, 'data/Match 6 - Congo DR/', 'df2.csv')
    return plotMatch(filename)

def plotStatMatch7():
    filename = os.path.join(BASE_DIR, 'data/Match 7 - Nigeria/', 'df2.csv')
    return plotMatch(filename)

def plotMatch(filename):
    dataDict = {}

    with open(filename, 'r') as f:
        dataList = list(csv.reader(f, delimiter=';'))

    for row in dataList[1:]:
        dataDict[row[0]] = {dataList[0][i]: int(row[i]) for i in range(1, len(dataList[0]))}

    for country, stat in dataDict.items():
        if country == 'Côte d\'Ivoire':
            homeName = country
            homeGoal = stat['Goals']
            homeDict = stat
            del homeDict['Goals']
            del homeDict['Cards']
        else :
            opponentName = country
            opponentGoal = stat['Goals']
            opponentDict = stat
            del opponentDict['Goals']
            del opponentDict['Cards']

    fig = go.Figure()
    fig.add_annotation(
        go.layout.Annotation(
            text=f"{homeGoal} - {opponentGoal}",
            xref="paper", x=0.5,
            yref="paper", y=1.01,
            xanchor='center',
            yanchor='bottom',
            showarrow=False,
            font=dict(size=30),
        ),
    )

    fig.add_trace(go.Bar(
        name=homeName,
        y=list(homeDict.keys()),
        x=[-value for value in homeDict.values()],
        base=0,
        text=[value for value in homeDict.values()],
        textposition='auto',
        hoverinfo='none',
        orientation='h',
        marker_color='green'
    ))

    fig.add_trace(go.Bar(
        name=opponentName,
        y=list(opponentDict.keys()),
        x=list(opponentDict.values()),
        base=0,
        text=list(opponentDict.values()),
        textposition='auto',
        hoverinfo='none',
        orientation='h',
        marker_color='orange'
    ))

    fig.update_layout(
        barmode='relative',
        xaxis=dict(
            showticklabels=False,
            showgrid=False,
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black'
        ),
        yaxis=dict(
            automargin=True
        ),
        plot_bgcolor='white',
        width=650,
        height=350,
        margin=dict(l=0, r=0, t=80, b=0),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.2,
            xanchor="center",
            x=0.5
        ),
    )

    return fig.to_html(full_html=False, config={'displayModeBar': False})