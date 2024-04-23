from data.results_matchs_subs_data import data
import plotly.graph_objects as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

def counts_results_per_player():
    player_results = {}

    for match_info in data.values():
        result = match_info['Results']
        for player in match_info['Players']:
            if player not in player_results:
                player_results[player] = {'W': 0, 'L': 0}
            player_results[player][result] += 1
    return dict(sorted(player_results.items(), key=lambda item: item[1]['W'], reverse=True))

def draw_results_per_player():
    player_results = counts_results_per_player()
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=list(player_results.keys()),
        y=[value['W'] for value in player_results.values()],
        base=0,
        hoverinfo='none',
        orientation='v',
        marker_color='#97B54A'
    ))
    fig.add_trace(go.Bar(
        x=list(player_results.keys()),
        y=[value['L'] for value in player_results.values()],
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