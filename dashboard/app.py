import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
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

st.subheader("Latest Crypto Market Data")
st.dataframe(df)

st.subheader("Market Cap Overview")
st.bar_chart(df.set_index("coin_name")["market_cap"])