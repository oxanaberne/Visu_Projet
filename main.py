import pathlib
import graphs.players_performance as pp
import graphs.subs_performance as sp
import graphs.results_matchs_subs as rm
import graphs.statistiques_matchs as sm
import graphs.time_matchs as tm
import data.preprocess_performance_data as pr
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
    plotMatch1 = sm.plotStatMatch1()
    plotMatch2 = sm.plotStatMatch2()
    plotMatch3 = sm.plotStatMatch3()
    plotMatch4 = sm.plotStatMatch4()
    plotMatch5 = sm.plotStatMatch5()
    plotMatch6 = sm.plotStatMatch6()
    plotMatch7 = sm.plotStatMatch7()

    # Partie 2 : Analyse des statistiques de l'ensemble des joueurs
    plotAttMatchs = pp.attackersPerformances()
    plotMidMatchs = pp.midfieldersPerformances()
    plotDefMatchs = pp.defendersPerformances()

    # Partie 3 : Analyse des statistiques des joueurs remplaçants
    plotSubAttMatchs = sp.attackersSubPerformances()
    plotSubMidMatchs = sp.midfieldersSubPerformances()
    plotSubDefMatchs = sp.defendersSubPerformances()
    plotResultsSubs = rm.matchResultsPerPlayer()

    # Partie 4 :Analyse des matchs dans le temps
    plotTimesMatchs = tm.decisivesActionsMatchs()
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            # Partie 1
            "plotMatch1": plotMatch1,
            "plotMatch2": plotMatch2,
            "plotMatch3": plotMatch3,
            "plotMatch4": plotMatch4,
            "plotMatch5": plotMatch5,
            "plotMatch6": plotMatch6,
            "plotMatch7": plotMatch7,
            # Partie 2 
            "plotAttMatchs": plotAttMatchs,
            "plotMidMatchs": plotMidMatchs,
            "plotDefMatchs": plotDefMatchs,
            # Partie 3
            "plotSubAttMatchs": plotSubAttMatchs,
            "plotSubMidMatchs": plotSubMidMatchs,
            "plotSubDefMatchs": plotSubDefMatchs,
            "plotResultsSubs": plotResultsSubs,
            # Partie 4
            "plotTimesMatchs": plotTimesMatchs
        }
    )