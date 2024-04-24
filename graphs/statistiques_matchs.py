import pathlib
import pandas as pd # type: ignore
import plotly.graph_objects as go # type: ignore
import os
import csv

BASE_DIR = pathlib.Path(__file__).parent.parent

def plot_totals(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        data_list = list(reader)
    data_dict = {}

    for row in data_list[1:]:
        country_data = {data_list[0][i]: int(row[i]) for i in range(1, len(data_list[0]))}
        data_dict[row[0]] = country_data

    for country, stat in data_dict.items():
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
            xref="paper", x=0.5,  # Positionne l'annotation au centre en largeur
            yref="paper", y=1.01,  # Positionne l'annotation en hauteur
            xanchor='center',  # Centre le texte par rapport à sa position en x
            yanchor='bottom',  # Align le texte par le bas par rapport à sa position en y
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

def stat_match1():
    filename = os.path.join(BASE_DIR, 'data/Match 1 - Guinea-Bissau/', 'df2.csv')
    return plot_totals(filename)

def stat_match2():
    filename = os.path.join(BASE_DIR, 'data/Match 2 - Nigeria/', 'df2.csv')
    return plot_totals(filename)

def stat_match3():
    filename = os.path.join(BASE_DIR, 'data/Match 3 - Equatorial-Guinea/', 'df2.csv')
    return plot_totals(filename)

def stat_match4():
    filename = os.path.join(BASE_DIR, 'data/Match 4 - Senegal/', 'df2.csv')
    return plot_totals(filename)

def stat_match5():
    filename = os.path.join(BASE_DIR, 'data/Match 5 - Mali/', 'df2.csv')
    return plot_totals(filename)

def stat_match6():
    filename = os.path.join(BASE_DIR, 'data/Match 6 - Congo DR/', 'df2.csv')
    return plot_totals(filename)

def stat_match7():
    filename = os.path.join(BASE_DIR, 'data/Match 7 - Nigeria/', 'df2.csv')
    return plot_totals(filename)