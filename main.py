from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pathlib
app = FastAPI()
HTML = pathlib.Path(__file__).parent.joinpath("index.html").read_text(encoding="utf-8")
@app.get("/")
def home():
    return HTMLResponse(HTML)
