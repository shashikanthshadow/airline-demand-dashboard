# ✈️ Airline Market Demand Web App

A FastAPI-based interactive dashboard that fetches, processes, and visualizes real-time airline demand trends using the AviationStack API.
This tool is designed to help hospitality and travel-related businesses (e.g., hostels, travel agencies) analyze air travel market trends, identify high-demand routes, and understand price fluctuations.

🎥 Demo Video
📺 Watch Demo on YouTube
(Replace with your actual video link)

🔧 Features
🌍 Live API Integration: Fetches real-time flight data from the AviationStack API

📊 Trend Visualization: Displays estimated price trends over 10 days using Chart.js

🛫 Route Insights: Identifies the most popular routes based on flight frequency

📈 Dynamic Charting: Interactive line charts with tooltips for route-wise pricing

🧼 Data Cleaning & Processing: Flight data is filtered and sorted using pandas

🎨 Frontend with Jinja2: Clean, responsive HTML dashboard styled with CSS

📦 Tech Stack
Backend	Frontend	Data/API
FastAPI	HTML/CSS	AviationStack API
Uvicorn	Chart.js	pandas
Jinja2	JS (fetch API)	datetime, requests

🖼️ Screenshots
(Add if you haven't already)

✅ Dashboard view with trend charts

✅ Popular routes section

✅ API response samples (optional)

🚀 Run Locally (with Conda & FastAPI)
bash
Copy
Edit
# 1️⃣ Clone the repository
git clone https://github.com/shashikanthshadow/airline-demand-dashboard.git
cd airline-demand-dashboard

# 2️⃣ Create and activate the Conda environment
conda env create -f environment.yml
conda activate airlineapp

# 3️⃣ Run the FastAPI server
uvicorn main:app --reload
Then open: http://127.0.0.1:8000/

📁 Project Structure
cpp
Copy
Edit
airline-demand-dashboard/
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── environment.yml
├── README.md
🧠 Author
Shashikanth Rao
GitHub: @shashikanthshadow

