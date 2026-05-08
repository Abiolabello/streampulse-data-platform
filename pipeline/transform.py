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