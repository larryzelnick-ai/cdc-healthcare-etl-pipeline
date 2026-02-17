import sqlite3
import pandas as pd

conn = sqlite3.connect("data/cdc_data.db")

# Preview first 5 rows
df = pd.read_sql_query("SELECT * FROM cdc_data LIMIT 5;", conn)
print(df)

# Count total rows
count = pd.read_sql_query("SELECT COUNT(*) FROM cdc_data;", conn)
print(count)

conn.close()

