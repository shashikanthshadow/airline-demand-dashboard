# ✈️ Airline Market Demand Web App

A FastAPI-based dashboard that fetches and visualizes real-time airline demand trends using the OpenSky API.

## 🔧 Features

- Fetches flight data via OpenSky Network API
- Shows popular flight routes based on real-time state data
- Displays mock price trend for upcoming days
- Interactive charts using Chart.js
- Jinja2 templated frontend with HTML/CSS

## 📦 Tech Stack

- FastAPI + Jinja2
- Chart.js + HTML/CSS
- OpenSky API (requires credentials for extended usage)

## 🚀 Run Locally

```bash
git clone <repo_url>
cd airline-demand-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
