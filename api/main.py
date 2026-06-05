"""
main.py
FastAPI backend — REST endpoints for the dashboard.
TODO: implement in Week 5.
"""
from fastapi import FastAPI

app = FastAPI(title="Orbital Traffic Intelligence API", version="0.1.0")


@app.get("/")
def root():
    return {"status": "ok", "message": "Orbital Traffic API is running"}
