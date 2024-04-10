import plotly.graph_objs as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

def sub_attackers_perf_by_matchs():
    players_data = {
        'Joueur 1': [(2, 2, 0), (1, 0, 0), (2, 1, 1), (3, 2, 1), (3, 1, 1), (3, 2, 1), (1, 1, 0)],
        'Joueur 2': [(2, 2, 1), (2, 1, 0), (3, 2, 2), (2, 1, 1), (2, 1, 1), (2, 2, 0), (3, 2, 1)],
        'Joueur 3': [(1, 1, 1), (1, 1, 0), (2, 0, 0), (2, 1, 1), (3, 2, 2), (1, 1, 1), (1, 1, 0)],
        'Joueur 4': [(1, 0, 0), (2, 1, 1), (2, 1, 1), (1, 1, 1), (2, 1, 0), (1, 0, 0), (2, 2, 1)],
        'Joueur 5': [(3, 1, 1), (2, 1, 1), (2, 1, 1), (1, 1, 0), (2, 2, 0), (2, 3, 1), (3, 2, 1)],
        'Joueur 6': [(2, 1, 1), (2, 2, 1), (2, 2, 1), (1, 0, 0), (2, 1, 1), (2, 2, 1), (1, 1, 1)],
    }
    # du plus foncé au plus claire
    colors = ['#fa7704', '#fcab5a', '#ffe45b']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in players_data.keys()])

    for index, (player, stats) in enumerate(players_data.items()):
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
        height=800, width=1000,
        showlegend=False,
        barmode='stack'
    )

    return fig.to_html(full_html=False, config={'displayModeBar': False})

def sub_attackers_perf_global():
    return sub_attackers_perf_by_matchs()

def sub_mid_perf_by_matchs():
    players_data = {
        'Joueur 1': [(2, 1, 1, 0), (1, 1, 1, 0), (3, 2, 1, 0), (4, 2, 1, 0), (3, 3, 2, 0), (5, 3, 1, 1), (2, 2, 1, 1)],
        'Joueur 2': [(3, 2, 1, 1), (2, 2, 1, 1), (4, 3, 2, 0), (3, 1, 1, 1), (2, 2, 1, 0), (1, 1, 1, 0), (3, 3, 2, 1)],
        'Joueur 3': [(1, 1, 0, 0), (2, 1, 1, 0), (1, 0, 0, 1), (3, 2, 1, 0), (4, 3, 2, 1), (2, 2, 1, 0), (1, 1, 1, 2)],
        'Joueur 4': [(0, 0, 0, 1), (1, 1, 1, 0), (2, 1, 1, 1), (2, 2, 1, 0), (3, 1, 1, 0), (1, 0, 0, 1), (2, 1, 1, 0)],
        'Joueur 5': [(2, 2, 1, 0), (3, 2, 1, 0), (1, 1, 1, 2), (1, 1, 0, 2), (2, 2, 2, 1), (3, 3, 1, 1), (4, 4, 2, 0)],
        'Joueur 6': [(1, 1, 1, 1), (2, 2, 1, 0), (3, 2, 2, 1), (1, 1, 0, 2), (3, 2, 1, 0), (2, 2, 1, 2), (1, 1, 1, 0)],
    }
    # passe, centres, interception, tacles
    colors = ['#244fa0', '#5b87da', '#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in players_data.keys()])

    for index, (player, stats) in enumerate(players_data.items()):
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
        height=1000, width=1000,
        showlegend=False,
        barmode='stack'
    )
    #fig.update_yaxes(range=[0,6])
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def sub_mid_perf_global():
    return sub_mid_perf_by_matchs()

def sub_defenders_perf_by_matchs():
    players_data = {
        'Joueur 1': [(1, 0), (1, 0), (1, 0), (1, 0), (2, 0), (1, 1), (1, 1)],
        'Joueur 2': [(1, 1), (1, 1), (2, 0), (1, 1), (1, 0), (1, 0), (2, 1)],
        'Joueur 3': [(0, 0), (1, 0), (0, 1), (1, 0), (2, 1), (1, 0), (1, 2)],
        'Joueur 4': [(0, 1), (1, 0), (1, 1), (1, 0), (1, 0), (0, 1), (1, 0)],
        'Joueur 5': [(1, 0), (1, 0), (1, 2), (0, 2), (2, 1), (1, 1), (2, 0)],
        'Joueur 6': [(1, 1), (1, 0), (2, 1), (0, 2), (1, 0), (1, 2), (1, 0)],
    }
    # interception, tacles
    colors = ['#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=2, cols=3, subplot_titles=[f'{player}' for player in players_data.keys()])

    for index, (player, stats) in enumerate(players_data.items()):
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
        height=600, width=1000,
        showlegend=False,
        barmode='stack'
    )
    #fig.update_yaxes(range=[0,6])
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def sub_defenders_perf_global():
    return sub_defenders_perf_by_matchs()