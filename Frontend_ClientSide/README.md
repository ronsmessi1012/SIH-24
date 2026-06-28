# 💻 Client-Side Booking & Time Slot Prediction Portal

This directory houses the client-facing booking interface and user-profile analytics dashboard for the Smart India Hackathon 2024 system. 

It is divided into:
1. **React Frontend**: Developed using React, Vite, and Bootstrap.
2. **Express API Server (`backend/index.js`)**: An authentication and booking backend that runs on port 5000 and connects to a local PostgreSQL instance.
3. **Time Slot Prediction Tool (`backend/sta.py`)**: A Python analytics module that calculates delivery success rates per time slot to predict optimal delivery windows for specific customers.

---

## 📁 Directory Structure

```
Frontend_ClientSide/
├── backend/
│   ├── index.js                     # Node/Express API server for user registration & authentication
│   ├── sta.py                       # Python time slot success rate analytics & prediction script
│   ├── user_dataset_india_with...2.csv  # Customer delivery history dataset
│   ├── package.json                 # Backend Node.js dependencies
│   └── .env                         # Environment configurations
├── index.html                       # Frontend application HTML root
├── package.json                     # Frontend React & Vite dependencies
├── vite.config.js                   # Vite server settings
├── eslint.config.js                 # Linter configuration
└── README.md                        # Documentation
```

---

## 🛠️ 1. React Frontend Setup

The frontend is a single-page application built on top of **React** and **Vite**, using **Bootstrap** for responsive styling and layout.

### Commands:
1. Navigate to the frontend directory:
   ```bash
   cd Frontend_ClientSide
   ```
2. Install frontend dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
4. Access the frontend app by visiting the URL shown in your terminal (typically `http://localhost:5173`).

---

## 🌐 2. Express Backend Setup (`backend/`)

The local Express server acts as an API gateway for user signups, logins, and bookings. It uses Passport.js for local database authentication.

### Database Setup (PostgreSQL):
To run this backend successfully, you need a running **PostgreSQL** server:
1. Create a database named `INDIAPOST`.
2. Create a table named `userdetail` with columns matching your authentication model:
   - `email` (primary key / text)
   - `password` (text)
3. The server connects by default to:
   - Host: `localhost`
   - Port: `5432`
   - User: `postgres`
   - Password: `@123#` (Ensure your Postgres password matches, or update line 17 of `backend/index.js` to match your credentials).

### Commands:
1. Navigate to the backend directory:
   ```bash
   cd Frontend_ClientSide/backend
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Run the backend server:
   ```bash
   node index.js
   ```
The server will start running on `http://localhost:5000`.

---

## 📊 3. Python Time Slot Analytics (`sta.py`)

The `sta.py` script analyzes the historical delivery dataset to identify when a customer is most likely to receive a package successfully. 

### Dependencies:
Install the required data science libraries:
```bash
pip install pandas scikit-learn
```

### Run the Script:
1. Navigate to the backend directory:
   ```bash
   cd Frontend_ClientSide/backend
   ```
2. **Important Note on File Path:** Line 6 of `sta.py` contains a hardcoded absolute file path:
   ```python
   file_path = r"C:\Users\HP\Desktop\SIH APP\indiapostapp\backend\user_dataset_india_with_timeslots_2.csv"
   ```
   To run this script locally on your machine, update line 6 to point to the local CSV:
   ```python
   file_path = "user_dataset_india_with_timeslots_2.csv"
   ```
3. Execute the script:
   ```bash
   python sta.py
   ```
4. When prompted, enter a customer name (e.g. `Anisha Singh` or other name in the dataset) to view their delivery success breakdown and get their predicted optimal time slot (ETA).

---

## 📄 License
This module is licensed under the **ISC License**.
© 2025 Ashmita Sen Roy
