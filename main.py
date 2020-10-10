from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

js_zwiekszajacy_hajs = { "skrypt": """
    let div = document.getElementById('moj-hajs');
    div.innerHTML = parseInt(div.innerHTML) + 1;
"""}

    
@app.get("/odswierz")
def odswierz():
    return js_zwiekszajacy_hajs

@app.get("/zwieksz_hajs")
def zwieksz_hajs():
    return js_zwiekszajacy_hajs

@app.get("/daj_zart")
def daj_zart():
    zarty = [
        'Wiesz jak ma na imie moja mama? Andrzej!',
        'Wiesz czemu nie ma mnie w domu? Bo sram!',
        'Wiesz za co kain zabił abla? Za ciągniecie kabla!',
        'Hehehehe'
    ]
    return { "zart": random.sample(zarty, 1) }