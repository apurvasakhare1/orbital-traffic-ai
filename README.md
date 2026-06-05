# 🛰️ Orbital Traffic Intelligence System

An AI-powered orbital monitoring platform that tracks satellites,
predicts collision risks, detects anomalies, and visualizes
orbital traffic around Earth.

## Quick start
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # fill in credentials
python ingestion/fetch_tle.py # fetch satellite data
streamlit run dashboard/app.py
```

## Project structure
```
orbital-traffic-ai/
├── data/           raw TLE files, SQLite DB
├── ingestion/      fetch + parse TLE data
├── propagation/    SGP4 orbit propagation
├── analytics/      conjunction + congestion analysis
├── ml/             risk classifier, anomaly detector
├── api/            FastAPI backend
├── dashboard/      Streamlit UI
└── notebooks/      research notebooks
```
