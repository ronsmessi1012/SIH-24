# 🎯 AI-Based Time Slot Prediction & Route Optimization Model – Smart India Hackathon 2024

Welcome to our AI-powered solution developed for **Smart India Hackathon 2024** (Problem Statement ID: 1761), designed to optimize postal deliveries and predict delivery time slots. 

This project integrates machine learning, discrete-event simulation, GPS tracking, and route optimization algorithms to improve postal routing efficiency, predict successful delivery time slots, and minimize transit delays.

---

## 📂 Project Repository Structure

The project is split into three main modules:

1. **[Backend/](file:///Users/ronnie/Desktop/SIH/SIH-2024-PSID-1761/Backend)**: The core route optimization service.
   - Computes optimized postal delivery paths utilizing **Google OR-Tools** (solving the Traveling Salesman Problem).
   - Serves an Express API (`server.js`) on port 3000 to interact with the Python route optimizer.
   - Includes a discrete-event simulation tool (`fake_data.py`) to generate realistic historical delivery data.
   - Includes a public route visualizer (`public/index.html`).
   - Read more in the [Backend README](file:///Users/ronnie/Desktop/SIH/SIH-2024-PSID-1761/Backend/README.md).

2. **[Frontend_ClientSide/](file:///Users/ronnie/Desktop/SIH/SIH-2024-PSID-1761/Frontend_ClientSide)**: The React-based booking and analytics portal.
   - Configured with React, Vite, and Bootstrap.
   - Includes a user authentication backend server (`backend/index.js`) running on port 5000 that connects to a PostgreSQL database (`INDIAPOST`).
   - Features a Python analytics model (`backend/sta.py`) that analyzes user delivery history to predict the most successful delivery time slot.
   - Read more in the [Frontend_ClientSide README](file:///Users/ronnie/Desktop/SIH/SIH-2024-PSID-1761/Frontend_ClientSide/README.md).

3. **[Frontend_ServerSide/](file:///Users/ronnie/Desktop/SIH/SIH-2024-PSID-1761/Frontend_ServerSide)**: Mock Portal & Live Tracking Simulator.
   - A static web interface mimicking the India Post portal (`web.html`).
   - An interactive parcel tracking page (`nextpage.html`) using Leaflet.js maps.
   - A simulator script (`Frontend_files/locationupdate.py`) that periodically updates parcel locations (`locations.json`) in real-time to simulate moving packages.

---

## 🧠 System Architecture & Data Flow

```
                                    [START]
                                       |
                                       V
                          +-------------------------+
                          |  User-Facing Web Portal |
                          +-------------------------+
                                       |
                   +-------------------+-------------------+
                   |                                       |
    // --- SENDER's JOURNEY ---                        // --- RECIPIENT's JOURNEY ---
                   |                                       |
                   V                                       V
      +----------------------------+          +-----------------------------+
      | 1. Sender Enters Ref. No.  |          | 1a. Recipient Enters Ref. No|
      +----------------------------+          +-----------------------------+
                   |                                       |
                   V                                       V
      +----------------------------+          +-----------------------------+
      | 2. AI Model Predicts Time  |          | 2a. Track & View Time       |
      +----------------------------+          +-----------------------------+
                   |                                       |
                   V                                       V
      <   3. Sender Satisfied?   >          <   3a. Recipient Satisfied?  >
            |              |                      |               |
        YES  |              |  NO             YES  |               |  NO
            |              |                      |               |
            |       +---------------------+       |        +----------------------+
            |       | Proposes New Time   |       |        | Proposes New Time    |
            |       +---------------------+       |        +----------------------+
            |              |                      |               |
            |              V                      |               V
            |       < AI Re-evaluates >           |        < AI Re-evaluates >
            |              |                      |               |
            +--------------+----------------------)---------------+--------------+
                                       |
                                       V
                   +-----------------------------------------+
                   |  4. SCHEDULING & BACKEND CONFIRMATION   |
                   +-----------------------------------------+
                                       |
      <<============== Writes & Reads =============>>
     +-----------------------------------------------------+
     |                  D A T A B A S E                    |
     | (User Info, Historical Success Rates, Preferences)  |
     +-----------------------------------------------------+
       <<===============================================>>
                                       |
                                       V
                     // --- PORTAL OFFICE's WORKFLOW ---
 
                   +-----------------------------------------+
                   |  5. View Confirmed Schedule on Dashboard|
                   +-----------------------------------------+
                                       |
                                       V
         6. OPTIMIZE ROUTE (optimize_route.py using Google OR-Tools)             
                                       |
                                       V
                           +-------------------------+
                           |  7. Assign Route to Staff   |
                           +-------------------------+
                                       |
                                       V
                            < Can Delivery Be Made? >
                                 |         |
                            YES  |         | NO
                                 |         |
                                 V         +-----> (Reschedule Within Range)
                     +---------------------+
                     | 8. DELIVERY SUCCESSFUL|
                     +---------------------+
                                 |
                                 V
                     +---------------------+
                     | 9. Collect User Rating|-----> (Update Database w/ New Data)
                     +---------------------+
                                 |
                                 V
                               [STOP]
```

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ashmitasenroy/SIH-2024-PSID-1761.git
cd SIH-2024-PSID-1761
```

### 2. Configure & Run the Route Optimizer (`Backend`)
1. Navigate to the `Backend` directory:
   ```bash
   cd Backend
   ```
2. Install Node.js packages:
   ```bash
   npm install
   ```
3. Install Python dependencies:
   ```bash
   pip install simpy faker pandas numpy geopy ortools openpyxl
   ```
4. Generate the delivery simulation dataset:
   ```bash
   python fake_data.py
   ```
5. Start the Node.js API server:
   ```bash
   npm start
   ```
6. Access the route optimization visualization by opening `http://localhost:3000` in your web browser.

### 3. Configure & Run the Portal (`Frontend_ClientSide`)
1. Run the Frontend React app:
   ```bash
   cd Frontend_ClientSide
   npm install
   npm run dev
   ```
2. Setup the User & Booking Backend:
   - Configure a PostgreSQL database named `INDIAPOST` with database credentials matching your server settings (by default: user `postgres`, password `@123#`).
   - Run the backend:
     ```bash
     cd backend
     npm install
     node index.js
     ```
3. Analyze Time Slot Predictions:
   ```bash
   cd backend
   python sta.py
   ```

### 4. Run the Mock Portal & Live Tracking Simulator (`Frontend_ServerSide`)
1. Navigate to the tracking files:
   ```bash
   cd Frontend_ServerSide/Frontend_files
   ```
2. Start the coordinates simulator script (updates coordinates in `locations.json` every 5 seconds):
   ```bash
   python locationupdate.py
   ```
3. Open `web.html` in your browser to explore the landing page portal.
4. Open `nextpage.html` in your browser and search for reference IDs (e.g., `REF123`, `REF456`, `REF789`) to watch the pins update in real time on the Leaflet.js map.

---

## 👩🏻‍💻 Developed By (Team - The Ensembles)

- **Ritusree Das**
- **Mohak Das**
- **Rudranil Choudhary**
- **Surya Pratap Verma**
- **Anisha Singh**
- **Ashmita Sen Roy**

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more info.
© 2025 Ashmita Sen Roy
