import plotly.graph_objects as go # type: ignore
import numpy as np # type: ignore
import random

def decisives_actions_matchs():
    # Données de matchs supposés
    data = {
        'Buts pour': {'Match 1': [41, 59], 'Match 2': [34, 79], 'Match 3': [24], 'Match 4': [], 'Match 5': [81], 'Match 6': [88], 'Match 7': [46, 95]},
        'Buts contre': {'Match 1': [32], 'Match 2': [64], 'Match 3': [82, 90], 'Match 4': [], 'Match 5': [40], 'Match 6': [], 'Match 7': [44, 72]},
        'Changements': {'Match 1': [38, 69, 90], 'Match 2': [35, 51, 88], 'Match 3': [61, 65, 69], 'Match 4': [69, 81], 'Match 5': [63, 80], 'Match 6': [30, 51, 73], 'Match 7': [36, 61]},
        'Cartons jaunes': {'Match 1': [42], 'Match 2': [51, 68], 'Match 3': [], 'Match 4': [15, 85], 'Match 5': [30, 68], 'Match 6': [56, 68], 'Match 7': [45]}
        }
    colors = ['#8ac000', '#c02300', '#5b87da', '#ffe100']
    symbols = ['circle', 'circle', 'arrow-bar-right', 'diamond']

    fig = go.Figure()
    for i, (event, match_events) in enumerate(data.items()):
        for nb_match, times in match_events.items():
            fig.add_trace(
                go.Scatter(
                    x=times,
                    y=[nb_match] * len(times),
                    mode='markers',
                    marker=dict(
                        color=colors[i],
                        symbol=symbols[i],
                        size=10,
                        line=dict(width=2)
                    ),
                )
            )

    fig.update_layout(
        width=1200,
        showlegend=False,
        xaxis=dict(
            range=[-5, 100],
            title='Minutes',
            tickmode='linear',
            tick0=0,
            dtick=10
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=list(range(1, 8)),
            ticktext=[f"Match {i}" for i in range(1, 8)],
            range=[0.5, 8]
        ),
    )

    return fig.to_html(full_html=False, config={'displayModeBar': False})
