import plotly.graph_objs as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

def draw_graph_attackers(data):
    # du plus foncé au plus claire
    colors = ['#fa7704', '#fcab5a', '#ffe45b']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in data.keys()])

    for index, (player, stats) in enumerate(data.items()):
        row = index // 3 + 1
        col = index % 3 + 1
        for match_index, (tirs_tentes, tirs_cadres, tirs_marques) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[tirs_tentes - tirs_cadres],
                marker=dict(color=colors[0]),
                orientation='h'
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[tirs_cadres - tirs_marques],
                marker=dict(color=colors[1]),
                orientation='h'
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[tirs_marques],
                marker=dict(color=colors[2]),
                orientation='h'
            ), row=row, col=col)

    fig.update_layout(
        height=800, width=900,
        showlegend=False,
        barmode='stack'
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def draw_graph_mid(data):
    # passe, centres, interception, tacles
    colors = ['#244fa0', '#5b87da', '#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in data.keys()])

    for index, (player, stats) in enumerate(data.items()):
        row = index // 3 + 1
        col = index % 3 + 1
        for match_index, (passe, centres, tacles, interception) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[passe],
                marker=dict(color=colors[0]),
                orientation='h',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[centres],
                marker=dict(color=colors[1]),
                orientation='h',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[interception],
                marker=dict(color=colors[2]),
                orientation='h',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[tacles],
                marker=dict(color=colors[3]),
                orientation='h',
            ), row=row, col=col)

    fig.update_layout(
        height=1000, width=900,
        showlegend=False,
        barmode='stack'
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def draw_graph_defenders(data):
    # interception, tacles
    colors = ['#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in data.keys()])

    for index, (player, stats) in enumerate(data.items()):
        row = index // 3 + 1
        col = index % 3 + 1
        for match_index, (tacles, interception) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[interception],
                marker=dict(color=colors[0]),
                orientation='h',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[match_index + 1],
                x=[tacles],
                marker=dict(color=colors[1]),
                orientation='h',
            ), row=row, col=col)

    fig.update_layout(
        height=600, width=900,
        showlegend=False,
        barmode='stack'
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})