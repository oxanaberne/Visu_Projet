import pathlib
import graphs.players_performance as pp
import graphs.subs_performance as sp
import graphs.statistiques_matchs as sm
import graphs.time_matchs as tm
import preprocess as pr
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
    plot_match1 = sm.stat_match1()
    plot_match2 = sm.stat_match2()
    plot_match3 = sm.stat_match3()
    plot_match4 = sm.stat_match4()
    plot_match5 = sm.stat_match5()
    plot_match6 = sm.stat_match6()
    plot_match7 = sm.stat_match7()

    get_players_data = pr.getPlayersData()
    get_players_global_performances = pr.getPlayersGlobalPerformances()

    # Partie 2 : Analyse des statistiques de l'ensemble des joueurs
    plot_att_matchs = pp.attackers_perf(get_players_data)
    plot_att_global = pp.attackers_perf(get_players_global_performances) 
    plot_mid_matchs = pp.mid_perf(get_players_data)
    plot_mid_global = pp.mid_perf(get_players_global_performances) 
    plot_def_matchs = pp.defenders_perf(get_players_data)
    plot_def_global = pp.defenders_perf(get_players_global_performances) 

    # Partie 3 : Analyse des statistiques des joueurs remplaçants
    plot_sub_att_matchs = sp.sub_attackers_perf_by_matchs()
    plot_sub_att_global = sp.sub_attackers_perf_global() #TODO
    plot_sub_mid_matchs = sp.sub_mid_perf_by_matchs()
    plot_sub_mid_global = sp.sub_mid_perf_global() #TODO
    plot_sub_def_matchs = sp.sub_defenders_perf_by_matchs()
    plot_sub_def_global = sp.sub_defenders_perf_global() #TODO

    # Partie 4 :Analyse des matchs dans le temps
    plot_times_matchs = tm.decisives_actions_matchs()
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            # Partie 1
            "plot_match1": plot_match1,
            "plot_match2": plot_match2,
            "plot_match3": plot_match3,
            "plot_match4": plot_match4,
            "plot_match5": plot_match5,
            "plot_match6": plot_match6,
            "plot_match7": plot_match7,
            # Partie 2 
            "plot_att_matchs": plot_att_matchs,
            "plot_att_global": plot_att_global,
            "plot_mid_matchs": plot_mid_matchs,
            "plot_mid_global": plot_mid_global,
            "plot_def_matchs": plot_def_matchs,
            "plot_def_global": plot_def_global,
            # Partie 3
            "plot_sub_att_matchs": plot_sub_att_matchs,
            "plot_sub_att_global": plot_sub_att_global,
            "plot_sub_mid_matchs": plot_sub_mid_matchs,
            "plot_sub_mid_global": plot_sub_mid_global,
            "plot_sub_def_matchs": plot_sub_def_matchs,
            "plot_sub_def_global": plot_sub_def_global,
            # Partie 4
            "plot_times_matchs": plot_times_matchs
        }
    )