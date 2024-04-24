import plotly.graph_objs as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

def draw_graph_attackers(data):
    rows = (len(data) + 2) // 3 
    cols = 3

    # Du plus foncé au plus claire
    colors = ['#fa7704', '#fcab5a', '#ffe45b']

    # Petit multiple avec Plotly pour chaque joueur
    subplot_titles = [f'{player}' for player in data.keys()]
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])

    for index, (player, stats) in enumerate(data.items()):
        row = index // cols + 1
        col = index % cols + 1
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

        fig.update_xaxes(range=[0, None], row=row, col=col, tickmode='linear', dtick=1)
        fig.update_yaxes(tickmode='array', tickvals=[i + 1 for i in range(len(stats))], row=row, col=col)


    fig.update_layout(
        width=650,
        showlegend=False,
        height=200 * rows,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0),
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def draw_graph_mid(data):
    rows = (len(data) + 2) // 3 
    cols = 3
    # Passe, Centres, Interception, Tacles
    colors = ['#244fa0', '#5b87da', '#97B54A', '#597318']
    fig_height = 200 * rows  # Adjust height based on the new bar thickness

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])

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
            
            fig.update_xaxes(range=[0, None], row=row, col=col, tickmode='linear', dtick=1)
            fig.update_yaxes(tickmode='array', tickvals=[i + 1 for i in range(len(stats))], row=row, col=col)

    fig.update_layout(
        width=650,
        height=fig_height,
        showlegend=False,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def draw_graph_defenders(data):
    rows = (len(data) + 2) // 3 
    cols = 3
    # Interception, Tacles
    colors = ['#97B54A', '#597318']
    fig_height = 200 * rows  # Adjust height based on the new bar thickness

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])

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
            
            fig.update_xaxes(range=[0, None], row=row, col=col, tickmode='linear', dtick=1)
            fig.update_yaxes(tickmode='array', tickvals=[i + 1 for i in range(len(stats))], row=row, col=col)

    fig.update_layout(
        width=650,
        height=fig_height,
        showlegend=False,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    return fig.to_html(full_html=False, config={'displayModeBar': False})