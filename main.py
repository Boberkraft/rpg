from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

skrypt = {"skrypt": """
        let div = document.getElementById('moj-hajs');
        div.innerHTML = parseInt(div.innerHTML) + 1;
    """}

    
@app.get("/odswierz")
def read_item():
    return skrypt

@app.get("/zwieksz_hajs")
def read_item():
    return skrypt