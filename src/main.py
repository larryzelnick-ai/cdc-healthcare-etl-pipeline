# src/main.py
import logging
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data, log_message

def main():
    # Configure logging to console
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    # --- Extract ---
    df = extract_data()  # no arguments needed with updated extract.py
    logging.info(f"DataFrame shape: {df.shape}")

    # --- Transform ---
    df = transform_data(df)
    logging.info(f"DataFrame after transformation shape: {df.shape}")

    # --- Load ---
    load_data(df)
    logging.info(f"Saved CSV and SQLite database")

    # --- Optional: log message to pipeline log ---
    log_message(f"ETL pipeline completed for {df.shape[0]} rows")

if __name__ == "__main__":
    main()

