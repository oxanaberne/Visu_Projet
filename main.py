import pathlib
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=[
    BASE_DIR / "templates",
])
app.mount("/static", StaticFiles(directory="static"), name="static")