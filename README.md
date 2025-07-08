# ✈️ Airline Market Demand Web App

A FastAPI-based interactive dashboard that fetches, processes, and visualizes real-time airline demand trends using the **AviationStack API**.

This tool is designed to help hospitality and travel-related businesses (e.g., hostels, travel agencies) analyze air travel market trends, identify high-demand routes, and understand price fluctuations.

---

### 🎥 Demo

> A quick preview of the working dashboard:

![Airline Dashboard Demo](assets/demo.gif)

*(Make sure you place your `demo.gif` inside an `assets/` folder in the root of your project.)*

---

## 🔧 Features

- 🌍 **Live API Integration**: Fetches real-time flight data from the AviationStack API
- 📊 **Trend Visualization**: Displays estimated price trends over 10 days using Chart.js
- 🛫 **Route Insights**: Identifies the most popular routes based on flight frequency
- 📈 **Dynamic Charting**: Interactive line charts with tooltips for route-wise pricing
- 🧼 **Data Cleaning & Processing**: Flight data is filtered and sorted using pandas
- 🎨 **Frontend with Jinja2**: Clean, responsive HTML dashboard styled with CSS

---

## 📦 Tech Stack

| Backend   | Frontend     | Data/API           |
|-----------|--------------|--------------------|
| FastAPI   | HTML, CSS    | AviationStack API  |
| Uvicorn   | Chart.js     | pandas             |
| Jinja2    | Vanilla JS   | datetime, requests |

---

## 🚀 Run Locally (with Conda & FastAPI)

```bash
# 1️⃣ Clone the repository
git clone https://github.com/shashikanthshadow/airline-demand-dashboard.git
cd airline-demand-dashboard

# 2️⃣ Create and activate the Conda environment
conda env create -f environment.yml
conda activate airlineapp

# 3️⃣ Run the FastAPI server
uvicorn main:app --reload
