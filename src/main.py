from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import logging
from datetime import datetime
import os

# Create logs folder
os.makedirs("logs", exist_ok=True)

# Timestamp for the log file
log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"logs/pipeline_{log_timestamp}.log"

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def main():
    url = "https://data.cdc.gov/resource/unsk-b7fc.json?$limit=500"
    
    # Extract
    df = extract_data(url)
    logging.info(f"DataFrame shape: {df.shape}")

    # Transform
    df = transform_data(df)
    logging.info(f"DataFrame after transformation shape: {df.shape}")

    # Save CSV with timestamp
    os.makedirs("data", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"data/cdc_raw_sample_{timestamp}.csv"
    df.to_csv(csv_path, index=False)
    logging.info(f"Saved CSV as {csv_path}")

    # Load into database
    db_path = "data/cdc_data.db"
    load_data(df, db_path=db_path)

if __name__ == "__main__":
    main()

