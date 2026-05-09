# StreamPulse Data Platform

An end-to-end beginner-friendly data engineering project that ingests live cryptocurrency data, transforms it using Python, stores it in PostgreSQL, and visualizes it with Streamlit.

---

# Architecture

```text
CoinGecko API
      ↓
Python ETL Pipeline
(ingest → transform → load)
      ↓
PostgreSQL Database
      ↓
Streamlit Dashboard
```

---

# Tech Stack

- Python 3.12
- PostgreSQL
- Pandas
- SQLAlchemy
- Streamlit
- Docker & Docker Compose
- CoinGecko API
- GitHub Codespaces

---

# Project Structure

```text
streampulse-data-platform/
│
├── .devcontainer/
│   └── devcontainer.json
│
├── dashboard/
│   └── app.py
│
├── pipeline/
│   ├── ingest.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── tests/
│   └── test_pipeline.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

# Dev Container Setup

Create:

```text
.devcontainer/devcontainer.json
```

Add:

```json
{
  "name": "StreamPulse",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",

  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {
      "moby": false
    }
  },

  "postCreateCommand": "pip install -r requirements.txt"
}
```

---

# Install Dependencies

Create:

```text
requirements.txt
```

Add:

```text
pandas
requests
sqlalchemy
psycopg2-binary
streamlit
python-dotenv
```

---

# Environment Variables

Create:

```text
.env
```

Add:

```env
DB_HOST=postgres
DB_PORT=5432
DB_NAME=crypto_db
DB_USER=admin
DB_PASSWORD=password
```

---

# Docker Compose Configuration

Create:

```text
docker-compose.yml
```

Add:

```yaml
services:
  postgres:
    image: postgres:15
    container_name: streampulse_postgres
    restart: always

    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: password
      POSTGRES_DB: crypto_db

    ports:
      - "5432:5432"

    volumes:
      - postgres_data:/var/lib/postgresql/data

  dashboard:
    build: .

    command: streamlit run dashboard/app.py --server.port=8501 --server.address=0.0.0.0

    ports:
      - "8501:8501"

    depends_on:
      - postgres

    env_file:
      - .env

volumes:
  postgres_data:
```

---

# Root Dockerfile

Create:

```text
Dockerfile
```

Add:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501
```

---

# 📡 Ingestion Layer

Create:

```text
pipeline/ingest.py
```

Add:

```python
import requests
import pandas as pd

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}


def fetch_crypto_data():
    response = requests.get(URL, params=PARAMS)
    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data)
```

---

# Transformation Layer

Create:

```text
pipeline/transform.py
```

Add:

```python
import pandas as pd


def transform_data(df: pd.DataFrame):
    columns = [
        "name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume"
    ]

    df = df[columns]

    df.columns = [
        "coin_name",
        "symbol",
        "current_price",
        "market_cap",
        "total_volume"
    ]

    return df
```

---

# 🗄️ Load Layer

Create:

```text
pipeline/load.py
```

Add:

```python
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


def load_data(df):
    df.to_sql(
        "crypto_prices",
        engine,
        if_exists="append",
        index=False
    )
```

---

# Pipeline Runner

Create:

```text
pipeline/main.py
```

Add:

```python
from ingest import fetch_crypto_data
from transform import transform_data
from load import load_data


def run_pipeline():
    raw_df = fetch_crypto_data()
    transformed_df = transform_data(raw_df)
    load_data(transformed_df)

    print("Pipeline executed successfully")


if __name__ == "__main__":
    run_pipeline()
```

---

# Streamlit Dashboard

Create:

```text
dashboard/app.py
```

Add:

```python
import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

st.title("📈 StreamPulse Crypto Dashboard")

query = "SELECT * FROM crypto_prices"

df = pd.read_sql(query, engine)

st.dataframe(df)

st.bar_chart(df.set_index("coin_name")["market_cap"])
```

---

# ▶️ Start Docker Services

Run:

```bash
docker compose up --build -d
```

---

# Execute Pipeline

Run:

```bash
docker compose exec dashboard python pipeline/main.py
```

Expected output:

```text
Pipeline executed successfully
```

---

# Open Dashboard

In GitHub Codespaces:

1. Open the **Ports** tab
2. Open port `8501`

You should now see:

- Crypto data table
- Market cap chart

---

# Common Errors & Fixes

## ❌ `DB_PORT=None`

### Cause
Environment variables not loaded.

### Fix

Add:

```yaml
env_file:
  - .env
```

under the `dashboard` service.

---

## ❌ `relation "crypto_prices" does not exist`

### Cause
Pipeline not executed yet.

### Fix

Run:

```bash
docker compose exec dashboard python pipeline/main.py
```

---

## ❌ Docker permission issues

### Fix

Use:

```json
"moby": false
```

inside `devcontainer.json`.

---

# 📤 Push to GitHub

```bash
git add .
git commit -m "Initial working StreamPulse data platform"
git push origin main
```

---

# Future Improvements

Potential upgrades:

- Apache Airflow scheduling
- Historical crypto tracking
- Redis caching
- Kafka streaming
- GitHub Actions CI/CD
- AWS deployment
- Data warehouse integration

---

# What You will Learn

By completing this project, you practiced:

- ETL pipelines  
- Docker Compose  
- PostgreSQL integration  
- Environment variables  
- Streamlit dashboards  
- API ingestion  
- SQLAlchemy  
- Debugging containerized systems  
- Git + GitHub workflows

---

# Author

Built by Abiolabello as a hands-on data engineering learning project.