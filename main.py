import pathlib
import players_performance as pp

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
    plot_att_matchs = pp.attackers_perf_by_matchs()
    plot_att_global = pp.attackers_perf_global()
    plot_mid_matchs = pp.mid_perf_by_matchs()
    plot_mid_global = pp.mid_perf_global()
    plot_def_matchs = pp.defenders_perf_by_matchs()
    plot_def_global = pp.defenders_perf_global()

    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request, 
            "plot_att_matchs": plot_att_matchs,
            "plot_att_global": plot_att_global,
            "plot_mid_matchs": plot_mid_matchs,
            "plot_mid_global": plot_mid_global,
            "plot_def_matchs": plot_def_matchs,
            "plot_def_global": plot_def_global
        }
    )