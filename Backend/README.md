# 📦 Intelligent Postal Delivery Route Optimization System

A **Smart India Hackathon 2024** module that simulates and optimizes postal delivery routes across Kolkata using real-world parameters like traffic congestion, regional delivery patterns, historical success rates, and geospatial distances. 

This component combines:
- 🔁 **Python discrete-event delivery simulation** using `SimPy`
- 📍 **OpenStreetMap coordinates** for geospatial routing
- 🧠 **Route optimization** using Google's Operations Research Tools (OR-Tools)
- 🌐 **Node.js Express API server** to integrate the Python-based routing logic with client frontends

---

## 📁 Directory Structure

```
Backend/
├── fake_data.py           # Generates 180 days of delivery data using SimPy + Faker
├── optimize_route.py      # Solves Traveling Salesman Problem (TSP) via Google OR-Tools
├── server.js              # Node.js API server bridging HTTP requests to Python optimizer
├── delivery_data.csv      # Output simulated dataset (generated on run)
├── ipsdata.xlsx           # Reference postal/PIN coordinates database
├── public/                # Static frontend UI for route visualization
│   ├── index.html         # Leaflet map container
│   └── main.js            # Map renderer and API client logic
├── package.json           # Node.js dependencies configuration
└── README.md              # Documentation
```

---

## 🎯 What it Solves

Traditional postal route planning struggles with dynamic urban challenges. This system optimizes delivery paths dynamically by combining:
- **Geospatial coordinates** representing delivery locations.
- **Haversine great-circle formula** to compute distances.
- **Traffic levels** (Peak, Heavy, Moderate, Light) based on time of day.
- **Google OR-Tools** to calculate the shortest path.

---

## 🧪 1. Simulated Dataset Generation

### `fake_data.py`
This script simulates 180 days of parcel delivery events across various zones in Kolkata.

#### Features modeled:
- **Pincodes**: Map real-world post codes (e.g., 700017, 700001, etc.) to geographic coordinates.
- **Traffic Patterns**: Set dynamically based on the delivery time slot.
- **Success Criteria**: Realistic retry logic and success/failure distribution based on region and time slot.
- **User Feedback**: Feedback ratings generated dynamically based on success/failure outcomes.

#### Running the simulation:
```bash
python fake_data.py
```
*Output*: Generates `delivery_data.csv` in the same directory.

#### Sample entry:
| Timestamp        | UserID    | Customer Name | Area Pincode | Distance | Time Slot   | Traffic | Region | Success | Rating |
| ---------------- | --------- | ------------- | ------------ | -------- | ----------- | ------- | ------ | ------- | ------ |
| 2024-04-01 09:00 | UID000012 | Ravi Verma    | 700017       | 6.0      | 09:00–10:00 | Peak    | East   | 1       | 5      |

---

## 🧭 2. Route Optimization

### `optimize_route.py`
This script accepts **OpenStreetMap coordinates** as input and outputs the index sequence of the optimal route.

#### Command syntax:
```bash
python optimize_route.py "[[22.5726, 88.3639], [22.5853, 88.4028], [22.5769, 88.3741]]"
```

#### Output JSON:
```json
{
  "routes": [[0, 2, 1, 0]]
}
```
*Interpretation*: Start at depot (Point 0) → Visit Point 2 → Visit Point 1 → Return to depot (Point 0).

---

## 🌐 3. API Backend (Node.js + Python)

### `server.js`
A lightweight Node.js Express server exposes an endpoint to trigger the optimizer from the frontend.

#### API Endpoint:
`GET /optimize-route?waypoints=[URL-encoded JSON coordinate array]`

- **Example Query:**
  ```http
  GET http://localhost:3000/optimize-route?waypoints=%5B%5B22.5726%2C88.3639%5D%2C%5B22.5853%2C88.4028%5D%2C%5B22.5769%2C88.3741%5D%5D
  ```
- **Example Response:**
  ```json
  {
    "routes": [[0, 2, 1, 0]]
  }
  ```

#### Running the server:
```bash
npm start
```
By default, the server runs on `http://localhost:3000`.

---

## 📦 Setup & Installation

### 1. Python Environment Setup
Install required packages:
```bash
pip install simpy faker pandas numpy geopy ortools openpyxl
```

### 2. Node.js Environment Setup
Install project dependencies:
```bash
npm install
```

### 3. Running the Visualization UI
Once the Node.js server is running (`npm start`), open your browser and navigate to:
`http://localhost:3000`

The UI allows you to select nodes and view the Leaflet.js map path optimized in real-time.

---

## 👨‍💻 Developed By

**Anisha Singh**
🔗 [GitHub Profile](https://github.com/anisha-singh-2004)
🎓 Smart India Hackathon 2024 Participant (Team - The Ensembles)

---

## 📜 License

This project is licensed under the **MIT License**.
© 2025 Ashmita Sen Roy
