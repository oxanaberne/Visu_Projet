from data.results_matchs_subs_data import data
import plotly.graph_objects as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

def matchResultsPerPlayer():
    playerResults = countsResultsPerPlayer()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=list(playerResults.keys()),
        y=[value['W'] for value in playerResults.values()],
        base=0,
        hoverinfo='none',
        orientation='v',
        marker_color='#97B54A'
    ))
    fig.add_trace(go.Bar(
        x=list(playerResults.keys()),
        y=[value['L'] for value in playerResults.values()],
        base=0,
        hoverinfo='none',
        orientation='v',
        marker_color='#b54a4a'
    ))

    fig.update_layout(
        width=650,
        height=400,
        showlegend=False,
        barmode='stack',
        margin=dict(l=0, r=0, t=0, b=0)
    )
    fig.update_yaxes(tick0=0, dtick=1)

    return fig.to_html(full_html=False, config={'displayModeBar': False})

def countsResultsPerPlayer():
    playerResults = {}

    for matchInfo in data.values():
        result = matchInfo['Results']
        for player in matchInfo['Players']:
            if player not in playerResults:
                playerResults[player] = {'W': 0, 'L': 0}
            playerResults[player][result] += 1
    return dict(sorted(playerResults.items(), key=lambda item: item[1]['W'], reverse=True))