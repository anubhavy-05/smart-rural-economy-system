# 🌾 Smart Rural Economy Dashboard

An intelligent, full-stack data analytics and machine learning platform built to bridge the digital divide in rural sectors. The system predicts agricultural commodity prices using advanced machine learning models, automates live localized weather aggregation, offers responsive time-series visualizations, and includes an interactive client-side AI virtual assistant.


## 🚀 Key Features

- **Microservices Architecture:** Completely decoupled systems with a high-performance FastAPI server managing ML inferences and a robust Django web framework driving the user ecosystem.
- **Smart Weather Automation:** Automated real-time extraction of localized temperature and precipitation via integration with the Open-Meteo Geocoding and Weather APIs.
- **Dynamic Trend Analytics:** Responsive time-series line graphs powered by Chart.js, allowing immediate client-side filtering (7 Days, 1 Month, 1 Year) without database or page reloads.
- **Kisan Mitra AI Chatbot:** A lightweight, responsive floating virtual assistant capable of parsing contextual token streams and delivering instant natural language price insights from backend records.
- **Localization Ready:** Built-in dynamic multi-language support (English & Hindi) utilizing automated DOM translation workflows for rural accessibility.
- **Master Process Orchestration:** Custom python automation script (`start.py`) to handle dual-server lifecycles, background port mapping, and graceful system shutdowns.

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (ES6+), Chart.js
- **Backend Framework:** Django 5.x (Port 8001)
- **ML Engine API:** FastAPI, Uvicorn (Port 8000)
- **Machine Learning:** Scikit-Learn, Pandas, Joblib
- **Database / ORM:** SQLite / SQLAlchemy

## 📐 System Architecture

The dashboard implements a modern distributed systems pipeline:
1. User submits localized data or triggers the **Open-Meteo API** to auto-fill current weather attributes via asynchronous JavaScript (`fetch`).
2. Django captures the payload securely (protected via **CSRF tokens**), provisions user access authentication blocks, and routes data pipelines to the ML server.
3. FastAPI loads the serialized Scikit-Learn pipeline (`crop_price_model.joblib`), validates streaming payloads using **Pydantic Schemas**, calculates the localized inference, and persists the data transaction.

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Virtual Environment tool (`venv`)

### 1. Clone the Repository
```bash
git clone [https://github.com/anubhavy-05/rural-django-portal.git](https://github.com/anubhavy-05/rural-django-portal.git)
cd rural-django-portal



## 📂 Project Directory Structure
A quick look at how the Microservices are structured within the main repository:

```text
rural-django-portal/
│
├── core/                       # Django project settings and routing
├── dashboard/                  # Django app (Views, Templates, Frontend logic)
│   └── templates/
│       └── dashboard/
│           └── home.html       # Main UI with Chart.js, Weather Fetch, and AI Chatbot
│
├── venv/                       # Isolated Python virtual environment
├── crop_price_model.joblib     # Pre-trained Scikit-Learn Machine Learning Pipeline
├── db.sqlite3                  # Django's default database
├── rural_economy.db            # FastAPI/SQLAlchemy database for prediction history
│
├── models.py                   # SQLAlchemy Database models for FastAPI
├── main.py                     # FastAPI application (ML Endpoints)
├── manage.py                   # Django command-line utility
└── start.py                    # Master automation script to boot both servers