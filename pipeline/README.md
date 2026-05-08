# StreamPulse Data Platform

A beginner-to-intermediate data engineering project that ingests live cryptocurrency market data from the CoinGecko API, transforms it with Python and Pandas, stores it in PostgreSQL, and exposes analytics dashboards with Streamlit.

---

## Project Architecture

```text
CoinGecko API
      ↓
Python ETL Pipeline
(ingest → transform → load)
      ↓
PostgreSQL Database
      ↓
Streamlit Dashboard