# 📊 StreamPulse Crypto Data Platform

A beginner-to-intermediate data engineering project that ingests live cryptocurrency market data, stores it in PostgreSQL, transforms it using Python, and visualizes it through a Streamlit dashboard.

---

## 🏗️ Architecture

```
Crypto API (CoinGecko)
        ↓
  Python Ingestion
        ↓
  Transformation Layer
        ↓
  PostgreSQL Database
        ↓
  Streamlit Dashboard
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| PostgreSQL | Data persistence |
| Streamlit | Dashboard / visualization |
| SQLAlchemy | ORM / database interface |
| Pandas | Data transformation |
| Docker & Docker Compose | Containerized infrastructure |
| CoinGecko API | Live crypto market data |

---

## 📦 Project Structure

```
streampulse-data-platform/
│
├── dashboard/          # Streamlit dashboard
├── pipeline/           # ETL pipeline (ingest, transform, load)
├── sql/                # Database schema + queries
├── tests/              # Unit tests
├── .devcontainer/      # Dev environment setup
├── docker-compose.yml  # Multi-container setup
├── Dockerfile
└── requirements.txt
```

---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/Abiolabello/streampulse-data-platform.git
cd streampulse-data-platform
```

### 2. Create a `.env` file

```env
DB_HOST=postgres
DB_PORT=5432
DB_NAME=crypto_db
DB_USER=admin
DB_PASSWORD=password
```

### 3. Start services

```bash
docker compose up --build
```

### 4. Run the pipeline manually *(optional)*

```bash
docker compose exec dashboard python pipeline/main.py
```

### 5. Open the dashboard

```
http://localhost:8501
```

---

## 📊 Sample Output

The dashboard displays:

- 🥇 Top 10 cryptocurrencies by market cap
- 💵 Current price (USD)
- 📈 Market volume
- 🏅 Market cap ranking

<img width="1030" height="700" alt="image" src="https://github.com/user-attachments/assets/27cb3c9d-dca7-4934-9b2e-4e129dd0ab92" />


---

## Key Features

- **Live API ingestion** — pulls real-time data from CoinGecko
- **ETL pipeline** — Extract → Transform → Load
- **PostgreSQL persistence** — structured storage for historical data
- **Containerized architecture** — fully reproducible via Docker Compose
- **Interactive dashboard** — built with Streamlit for easy exploration

---

## 📄 License

MIT
