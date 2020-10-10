from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import random

app = FastAPI()

gracze = []

app.mount("/static", StaticFiles(directory="static"), name="static")

js_zwiekszajacy_hajs = { "skrypt": """
    let div = document.getElementById('moj-hajs');
    div.innerHTML = parseInt(div.innerHTML) + 1;
""" }

    
@app.get("/odswierz")
def odswierz():
    js_zwiekszajacy_hajs["odpowiedz"] =  random.sample(["🤩","🥳","🥰"], 1)
    return js_zwiekszajacy_hajs 

@app.get("/zwieksz_hajs")
def zwieksz_hajs():
    return js_zwiekszajacy_hajs

@app.post("/dodaj_gracza")
def dodaj_gracza(body: dict):
    gracze.append(body['imie'])
    return { "gracze": gracze }