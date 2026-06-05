import os
from pathlib import Path

# ── Folder structure ──────────────────────────────────────────────────────────
FOLDERS = [
    "data",                      # raw TLE files, SQLite DB, CSVs
    "ingestion",                 # fetch + parse TLE data
    "propagation",               # SGP4 orbit propagation
    "analytics",                 # conjunction engine, congestion mapper
    "ml",                        # risk classifier, anomaly detector
    "api",                       # FastAPI backend
    "dashboard",                 # Streamlit app
    "dashboard/pages",           # multi-page Streamlit pages
    "dashboard/assets",          # logos, CSS overrides
    "notebooks",                 # Jupyter research notebooks
    "tests",                     # unit + integration tests
]

# Files to create (path → content)
FILES = {
    # ── requirements ──────────────────────────────────────────────────────────
    "requirements.txt": """\
sgp4==2.22
requests==2.31.0
pandas==2.1.0
numpy==1.26.0
scikit-learn==1.3.0
plotly==5.17.0
streamlit==1.28.0
fastapi==0.104.0
uvicorn==0.24.0
scipy==1.11.0
python-dotenv==1.0.0
apscheduler==3.10.4
joblib==1.3.2
matplotlib==3.8.0
""",

    # ── env template ──────────────────────────────────────────────────────────
    ".env.example": """\
# Copy this file to .env and fill in your credentials

# Space-Track.org account (free signup at space-track.org)
SPACETRACK_USER=your_email@example.com
SPACETRACK_PASS=your_password

# App settings
TLE_REFRESH_HOURS=6
CONJUNCTION_SCAN_HOURS=24
CONJUNCTION_THRESHOLD_KM=50
HIGH_RISK_THRESHOLD_KM=5
""",

    # ── gitignore ─────────────────────────────────────────────────────────────
    ".gitignore": """\
# Python
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/
dist/
build/

# Environment
.env

# Data files (too large for git)
data/*.json
data/*.db
data/*.csv
data/*.parquet

# ML models
ml/models/*.pkl
ml/models/*.joblib

# Jupyter
.ipynb_checkpoints/
notebooks/.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
""",

    # ── README ────────────────────────────────────────────────────────────────
    "README.md": """\
# 🛰️ Orbital Traffic Intelligence System

An AI-powered orbital monitoring platform that tracks satellites,
predicts collision risks, detects anomalies, and visualizes
orbital traffic around Earth.

## Quick start
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\\Scripts\\activate
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
""",

    # ── module init files ─────────────────────────────────────────────────────
    "ingestion/__init__.py":   '"""TLE data ingestion — fetch and parse satellite data."""\n',
    "propagation/__init__.py": '"""Orbit propagation using SGP4."""\n',
    "analytics/__init__.py":   '"""Orbital analytics — conjunction and congestion analysis."""\n',
    "ml/__init__.py":          '"""Machine learning — risk classifier and anomaly detector."""\n',
    "api/__init__.py":         '"""FastAPI backend."""\n',
    "dashboard/__init__.py":   '"""Streamlit dashboard."""\n',
    "tests/__init__.py":       '"""Test suite."""\n',

    # ── placeholder source files ───────────────────────────────────────────────
    "ingestion/fetch_tle.py": '''\
"""
fetch_tle.py
Fetches TLE data from CelesTrak and saves it locally.
TODO: implement in Week 1 Day 2.
"""


def fetch_satellites(group: str = "active"):
    raise NotImplementedError("Coming in Week 1 Day 2")
''',

    "ingestion/parse_tle.py": '''\
"""
parse_tle.py
Parses raw TLE JSON and stores orbital parameters in SQLite.
TODO: implement in Week 1 Day 3.
"""


def parse_and_store(json_path: str, db_path: str = "data/satellites.db"):
    raise NotImplementedError("Coming in Week 1 Day 3")
''',

    "propagation/propagator.py": '''\
"""
propagator.py
SGP4 orbit propagation — converts TLEs to lat/lon/altitude.
TODO: implement in Week 1 Day 4.
"""


def get_position(line1: str, line2: str, dt=None):
    raise NotImplementedError("Coming in Week 1 Day 4")


def get_all_positions(satellites_df, dt=None):
    raise NotImplementedError("Coming in Week 1 Day 4")
''',

    "analytics/conjunction.py": '''\
"""
conjunction.py
KD-Tree based conjunction analysis engine.
TODO: implement in Week 3.
"""


def find_conjunctions(positions_df, threshold_km: float = 50.0):
    raise NotImplementedError("Coming in Week 3")
''',

    "analytics/congestion.py": '''\
"""
congestion.py
Orbital shell congestion mapper.
TODO: implement in Week 3.
"""


def compute_congestion(positions_df, shell_width_km: float = 50.0):
    raise NotImplementedError("Coming in Week 3")
''',

    "ml/risk_classifier.py": '''\
"""
risk_classifier.py
Random Forest collision risk classifier.
TODO: implement in Week 4.
"""


def train(features_df, labels):
    raise NotImplementedError("Coming in Week 4")


def predict(model, features_df):
    raise NotImplementedError("Coming in Week 4")
''',

    "ml/anomaly_detector.py": '''\
"""
anomaly_detector.py
Isolation Forest anomaly detector for unusual orbital behaviour.
TODO: implement in Week 4.
"""


def detect(satellites_df):
    raise NotImplementedError("Coming in Week 4")
''',

    "api/main.py": '''\
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
''',

    "dashboard/app.py": '''\
"""
app.py
Main Streamlit dashboard entry point.
TODO: implement globe in Week 1 Day 5.
"""
import streamlit as st

st.set_page_config(
    page_title="Orbital Traffic Intelligence System",
    page_icon="🛰️",
    layout="wide",
)

st.title("🛰️ Orbital Traffic Intelligence System")
st.info("Week 1 in progress — globe visualization coming Day 5.")
''',

    "tests/test_pipeline.py": '''\
"""
test_pipeline.py
End-to-end pipeline tests.
TODO: fill in as each module is built.
"""


def test_placeholder():
    """Placeholder — real tests added each week."""
    assert True
''',

    "notebooks/01_data_exploration.ipynb": """\
{
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
 "cells": [
  {"cell_type": "markdown", "metadata": {}, "source": ["# Week 1 — Data Exploration\\n", "Explore the raw TLE data from CelesTrak."]},
  {"cell_type": "code", "execution_count": null, "metadata": {}, "outputs": [], "source": ["import pandas as pd\\nimport json\\n\\n# Load fetched satellite data\\n# with open('../data/active_YYYYMMDD.json') as f:\\n#     sats = json.load(f)\\n# df = pd.DataFrame(sats)\\n# df.head()\\n"]}
 ]
}
""",
}


# ── Scaffold function ──────────────────────────────────────────────────────────

def scaffold(root: str = "."):
    root = Path(root)
    created_dirs = 0
    created_files = 0

    print("\n🛰️  Orbital Traffic AI — project scaffold\n" + "─" * 45)

    # Create folders
    for folder in FOLDERS:
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)
        status = "✅ created" if not path.exists() else "📁 exists "
        print(f"  {status}  {folder}/")
        created_dirs += 1

    print()

    # Create files
    for rel_path, content in FILES.items():
        path = root / rel_path
        if path.exists():
            print(f"  ⏭️  exists   {rel_path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"  ✅ created  {rel_path}")
            created_files += 1

    # data/.gitkeep so the empty data/ folder is tracked by git
    gitkeep = root / "data" / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.touch()
        print(f"  ✅ created  data/.gitkeep")

    print("\n" + "─" * 45)
    print(f"  📁  {created_dirs} folders  |  📄  {created_files} files created")
    print("\n  Next steps:")
    print("  1.  python -m venv venv && source venv/bin/activate")
    print("  2.  pip install -r requirements.txt")
    print("  3.  cp .env.example .env")
    print("  4.  git init && git add . && git commit -m 'feat: initial scaffold'")
    print("  5.  python ingestion/fetch_tle.py  (Day 2)\n")


if __name__ == "__main__":
    scaffold()