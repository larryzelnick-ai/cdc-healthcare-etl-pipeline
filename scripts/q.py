import sqlite3
import pandas as pd

conn = sqlite3.connect("data/cdc_data.db")
df = pd.read_sql_query("SELECT * FROM cdc_data LIMIT 5;", conn)

print(df.columns.tolist())

conn.close()

