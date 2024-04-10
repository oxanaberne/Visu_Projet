#Heure du match
#TODO#Nombre de buts
#TODO#% de possession
#TODO#Nombre de centres
#TODO#Nombre de tirs cadrés
#TODO#Nombre de fautes
#TODO#Nombre d'interceptions
#TODO#Nombre de tacles réussis
#CANTDO#Nombre de corners
import pathlib
import pandas as pd
import plotly.graph_objects as go
import os
import csv

BASE_DIR = pathlib.Path(__file__).parent.parent

def calculate_totals(df):
    return [
        df['Gls'].sum(),
        df['TklW'].sum(),
        df['Int'].sum(),
        df['Fls'].sum(),
        df['Crs'].sum(),
        df['SoT'].sum()
    ]

def plot_totals():
    base_dir = os.path.join(BASE_DIR, 'donne_match')
    dirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

    plots = {}

    for d in dirs:
        home = os.path.join(base_dir, d,'df5.csv')
        opponent = os.path.join(base_dir, d,'df3.csv')
        match_info = os.path.join(base_dir,d, 'df2.csv')

        df_home = pd.read_csv(home, delimiter=';', header=1)
        df_opponent = pd.read_csv(opponent, delimiter=';', header=1)

        totals_home = calculate_totals(df_home)
        totals_opponent = calculate_totals(df_opponent)

        with open(match_info, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            data = list(reader)

        home_team, opponent_team = data[0]

        possession_home = float(data[2][0].strip('%'))
        possession_opponent = float(data[2][1].strip('%'))

        totals_home.append(possession_home)
        totals_opponent.append(possession_opponent)

        fig = go.Figure(data=[
            go.Bar(name=f'{home_team}', y=['Goals', 'Tacles', 'Interceptions', 'Fautes', 'Possession %', 'Tirs cadrés', 'Centres'], 
                x=totals_home, 
                text=totals_home, textposition='auto', orientation='h'),
            go.Bar(name=f'{opponent_team}', y=['Goals', 'Tacles', 'Interceptions', 'Fautes', 'Possession %', 'Tirs cadrés', 'Centres'], 
                x=[value*-1 for value in totals_opponent], 
                text=[value*-1 for value in totals_opponent], textposition='auto', orientation='h')
        ])

        fig.update_layout(
            barmode='relative', 
            # title='Statistiques du match',
            xaxis=dict(showticklabels=False)
        )

        plots[d] = fig.to_html(full_html=False)

    return plots