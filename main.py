import pathlib
import graphs.players_performance as pp
import graphs.statistiques_match as sm
import graphs.time_matchs as tm
from fastapi import FastAPI, Request # type: ignore
from fastapi.responses import HTMLResponse # type: ignore
from fastapi.templating import Jinja2Templates # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore

app = FastAPI()

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=[
    BASE_DIR / "templates",
])
app.mount(
    "/static",
    StaticFiles(directory= BASE_DIR / "static"),
    name="static")

@app.get("/", response_class=HTMLResponse)
async def get_charts(request: Request):
    # Partie 1 : Analyse statistiques global des matchs
    stat_matchs = sm.plot_totals()

    # Partie 2 : Analyse des statistiques de l'ensemble des joueurs
    plot_att_matchs = pp.attackers_perf_by_matchs()
    plot_att_global = pp.attackers_perf_global()
    plot_mid_matchs = pp.mid_perf_by_matchs()
    plot_mid_global = pp.mid_perf_global()
    plot_def_matchs = pp.defenders_perf_by_matchs()
    plot_def_global = pp.defenders_perf_global()

    # Partie 3 : Analyse des statistiques des joueurs remplaçants

    # Partie 4 :Analyse des matchs dans le temps
    plot_times_matchs = tm.decisives_actions_matchs()
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            # Partie 1
            "stat_matchs": stat_matchs,
            # Partie 2 
            "plot_att_matchs": plot_att_matchs,
            "plot_att_global": plot_att_global,
            "plot_mid_matchs": plot_mid_matchs,
            "plot_mid_global": plot_mid_global,
            "plot_def_matchs": plot_def_matchs,
            "plot_def_global": plot_def_global,
            # Partie 3 
            # Partie 4
            "plot_times_matchs": plot_times_matchs
        }
    )