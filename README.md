### ✈️ Airline Market Demand Web App

A FastAPI-based interactive dashboard that fetches, processes, and visualizes real-time airline demand trends using the [AviationStack API](https://aviationstack.com/).

> Designed for hospitality and travel-related businesses (e.g., hostels, travel agencies) to analyze air travel market trends, identify high-demand routes, and understand price fluctuations.

---

## 🎥 Demo

A quick preview of the working dashboard:  
🚧 *(Insert screenshot or link to demo video)*

---

## 🔧 Features

- 🌍 **Live API Integration**: Fetches real-time flight data from AviationStack API  
- 📊 **Trend Visualization**: Displays estimated price trends over 10 days using Chart.js  
- 🛫 **Route Insights**: Identifies the most popular routes based on flight frequency  
- 📈 **Dynamic Charting**: Interactive line charts with tooltips for route-wise pricing  
- 🧼 **Data Cleaning & Processing**: Flight data filtered and sorted using `pandas`  
- 🎨 **Frontend with Jinja2**: Clean, responsive HTML dashboard styled with CSS  

---

## 📦 Tech Stack

| Layer      | Technologies                              |
|------------|-------------------------------------------|
| Backend    | FastAPI, Uvicorn                          |
| Frontend   | HTML, CSS, Jinja2, Chart.js, Vanilla JS   |
| Data/API   | AviationStack API, pandas, requests       |
| Utilities  | datetime, environment.yml                 |

---

## 🚀 Run Locally (with Conda & FastAPI)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/shashikanthshadow/airline-demand-dashboard.git
cd airline-demand-dashboard
2️⃣ Create and Activate the Conda Environment
bash
Copy
Edit
conda env create -f environment.yml
conda activate airlineapp
