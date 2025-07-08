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

```
3️⃣ Get Your Free API Key
Visit: https://aviationstack.com/

Click Sign Up Free

After signing in, go to your Dashboard

Copy your API Key

✍️ 4️⃣ Add Your API Key
Open the main.py file and find this line:

python
Copy
Edit
API_KEY = "your_actual_api_key_here"
Replace it with your real key:

python
Copy
Edit
API_KEY = "your_real_api_key"
🚀 5️⃣ Run the FastAPI Server
bash
Copy
Edit
uvicorn main:app --reload
Then open your browser and navigate to:

cpp
Copy
Edit
http://127.0.0.1:8000/
You’ll see the dashboard displaying live route demand and price trend charts! ✅



