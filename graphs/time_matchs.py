import plotly.graph_objects as go # type: ignore
import numpy as np # type: ignore
from data.time_matchs_data import data
import random

def decisivesActionsMatchs():
    # But pour, But contre, Changements, Cartons jaunes
    colors = ['#8ac000', '#c02300', '#5b87da', '#ffe100']
    symbols = ['circle', 'circle', 'arrow-bar-right', 'diamond']

    fig = go.Figure()
    for match, events in data.items():
        for idx, (eventType, times) in enumerate(events.items()):
            fig.add_trace(go.Scatter(
                x=times,
                y=[match] * len(times),
                mode='markers',
                name=eventType,
                marker=dict(
                    color=colors[idx],
                    symbol=symbols[idx],
                    size=10,
                    line=dict(
                        width=2,
                        color='DarkSlateGrey'
                    )
                ),
                legendgroup=eventType,
            ))

    fig.update_layout(
        width=650,
        showlegend=False,
        xaxis=dict(
            range=[-3, 123],
            title='Minutes',
            tickmode='linear',
            tick0=0,
            dtick=10
        ),
        yaxis=dict(
            categoryorder='array',
            categoryarray=[f'Match {i}' for i in range(1, 8)]
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig.to_html(full_html=False, config={'displayModeBar': False})
