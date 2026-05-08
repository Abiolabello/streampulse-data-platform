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