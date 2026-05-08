CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    coin_name VARCHAR(50),
    symbol VARCHAR(20),
    current_price NUMERIC,
    market_cap NUMERIC,
    total_volume NUMERIC,
    captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);