import plotly.graph_objs as go # type: ignore
from plotly.subplots import make_subplots # type: ignore

y_label = ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7'] 

def drawGraphAttackers(data):
    rows = (len(data) + 1) // 2 
    cols = 2
    # Du plus foncé au plus claire
    colors = ['#fa7704', '#fcab5a', '#ffe45b']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])
    maxVal = 0
    for index, (player, stats) in enumerate(data.items()):
        row = index // cols + 1
        col = index % cols + 1
        for match_index, (tirs_tentes, tirs_cadres, tirs_marques) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[tirs_marques],
                marker=dict(color=colors[2]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[tirs_cadres - tirs_marques],
                marker=dict(color=colors[1]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[tirs_tentes - tirs_cadres],
                marker=dict(color=colors[0]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            maxVal = max(maxVal, tirs_tentes)

    fig.update_layout(
        width=400 * cols,
        showlegend=False,
        height=250 * rows,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0),
    )
    fig.update_xaxes(tickmode='array', tickvals=[i + 1 for i in range(maxVal)], tickangle=45)
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def drawGraphMid(data):
    rows = (len(data) + 1) // 2 
    cols = 2
    # Passe, Centres, Interception, Tacles
    colors = ['#244fa0', '#5b87da', '#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])
    maxVal = 0
    for index, (player, stats) in enumerate(data.items()):
        row = index // cols + 1
        col = index % cols + 1
        for match_index, (passe, centres, tacles, interception) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[passe],
                marker=dict(color=colors[0]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[centres],
                marker=dict(color=colors[1]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[interception],
                marker=dict(color=colors[2]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[tacles],
                marker=dict(color=colors[3]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            maxVal = max(maxVal, passe + centres + tacles + interception)            
    fig.update_layout(
        width=400 * cols,
        height=200 * rows,
        showlegend=False,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig.update_xaxes(tickmode='array', tickvals=[i + 1 for i in range(maxVal)], tickangle=45)
    return fig.to_html(full_html=False, config={'displayModeBar': False})

def drawGraphDefenders(data):
    rows = (len(data) + 1) // 2 
    cols = 2
    # Interception, Tacles
    colors = ['#97B54A', '#597318']

    # Petit multiple avec Plotly pour chaque joueur
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f'{player}' for player in data.keys()])
    maxVal = 0
    for index, (player, stats) in enumerate(data.items()):
        row = index // cols + 1
        col = index % cols + 1
        for match_index, (tacles, interception) in enumerate(stats):
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[interception],
                marker=dict(color=colors[0]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            fig.add_trace(go.Bar(
                y=[y_label[match_index]],
                x=[tacles],
                marker=dict(color=colors[1]),
                orientation='h',
                hoverinfo='none',
            ), row=row, col=col)
            maxVal = max(maxVal, tacles + interception)

    fig.update_layout(
        width=400 * cols,
        height=200 * rows,
        showlegend=False,
        barmode='stack',
        margin=dict(l=0, r=0, t=40, b=0)
    )
    fig.update_xaxes(tickmode='array', tickvals=[i + 1 for i in range(maxVal)], tickangle=45)
    return fig.to_html(full_html=False, config={'displayModeBar': False})