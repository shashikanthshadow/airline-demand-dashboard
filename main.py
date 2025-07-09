from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import requests
import pandas as pd
from datetime import datetime
import random
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# AviationStack API Configuration
API_KEY = "your_actual_api_key_here"
BASE_URL = "http://api.aviationstack.com/v1/flights"

def fetch_aviationstack_data():
    params = {
        "access_key": API_KEY,
        "limit": 100
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data", [])

        route_counts = {}
        for flight in data:
            dep = flight.get("departure", {}).get("airport")
            arr = flight.get("arrival", {}).get("airport")
            if dep and arr:
                route = f"{dep} ➜ {arr}"
                route_counts[route] = route_counts.get(route, 0) + 1

        # Convert to DataFrame and get top 5 routes
        df = pd.DataFrame({
            "route": list(route_counts.keys()),
            "demand": list(route_counts.values())
        }).sort_values(by="demand", ascending=False).head(5)

        popular_routes = df["route"].tolist()
        demand = df["demand"].tolist()

        # Generate date range
        dates = pd.date_range(datetime.today(), periods=10).strftime('%Y-%m-%d').tolist()

        # Generate simulated price trends for each route
        route_prices = {}
        for route in popular_routes:
            base_price = random.randint(250, 350)
            route_prices[route] = [
                base_price + random.randint(-10, 15) + i * 5 for i in range(10)
            ]

        return {
            "dates": dates,
            "route_prices": route_prices,
            "popular_routes": popular_routes,
            "demand": demand
        }

    else:
        return {
            "dates": [datetime.today().strftime('%Y-%m-%d')],
            "route_prices": {},
            "popular_routes": ["No Data"],
            "demand": [0]
        }

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/data", response_class=JSONResponse)
async def api_data():
    return fetch_aviationstack_data()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
