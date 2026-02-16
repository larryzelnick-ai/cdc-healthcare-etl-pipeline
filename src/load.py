import logging
import sqlite3
import pandas as pd

def load_data(df, db_path="data/cdc_data.db", table_name="cdc_data"):
    """
    Load the transformed DataFrame into a SQLite database.
    """
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        logging.info(f"Loaded DataFrame into {db_path} table '{table_name}'")
        conn.close()
    except Exception as e:
        logging.error(f"Failed to load data into database: {e}")
        raise

