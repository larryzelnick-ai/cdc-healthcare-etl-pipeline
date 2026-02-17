# scripts/query_cdc_db.py
from pathlib import Path
import sqlite3
import pandas as pd

if __name__ == "__main__":
    print("=== CDC Data SQLite Query ===")

    BASE_DIR = Path(__file__).resolve().parent.parent  # scripts/ → project root
    db_path = BASE_DIR / "data" / "cdc_data.db"

    conn = sqlite3.connect(db_path)

    print("\n=== Tables in database ===")
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    print(tables)

    print("\n=== First 5 rows of cdc_data table ===")
    df = pd.read_sql_query("SELECT * FROM cdc_data LIMIT 5;", conn)
    print(df)

    print("\n=== Columns in cdc_data table ===")
    print(df.columns.tolist())

    print("\n=== Number of rows in cdc_data table ===")
    count = pd.read_sql_query("SELECT COUNT(*) AS total FROM cdc_data;", conn)
    print(count)

    print("\n=== Example: Total administered dose 1 by state ===")
    state_summary = pd.read_sql_query("""
        SELECT recip_state AS state, SUM(administered_dose1_recip) AS total_administered
        FROM cdc_data
        GROUP BY recip_state
        ORDER BY total_administered DESC
        LIMIT 10;
    """, conn)
    print(state_summary)

    conn.close()

