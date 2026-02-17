# src/load.py
from pathlib import Path
import sqlite3
from datetime import datetime
import pandas as pd

# --- Project directories ---
BASE_DIR = Path(__file__).resolve().parent.parent
data_dir = BASE_DIR / "data"
logs_dir = BASE_DIR / "logs"

# Ensure directories exist
data_dir.mkdir(exist_ok=True)
logs_dir.mkdir(exist_ok=True)

# Timestamp for files
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Default paths
csv_path = data_dir / f"cdc_raw_sample_{timestamp}.csv"
db_path = data_dir / "cdc_data.db"
log_path = logs_dir / f"pipeline_{timestamp}.log"

# --- Functions ---
def save_csv(df, path=None):
    if path is None:
        path = csv_path
    df.to_csv(path, index=False)
    print(f"CSV saved to {path}")

def save_sqlite(df, path=None):
    if path is None:
        path = db_path
    conn = sqlite3.connect(path)
    df.to_sql("cdc_data", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Database saved to {path}")

def log_message(message):
    """Append message to pipeline log"""
    with open(log_path, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

def load_data(df):
    """Wrapper for main pipeline: save CSV and SQLite DB"""
    save_csv(df)
    save_sqlite(df)

