# src/transform.py
import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic transformations on the raw CDC data.

    Steps:
    - Convert 'date' column to datetime
    - Sort by date
    - Drop any columns that are completely empty
    - Convert numeric columns to fill missing values with 0
    """
    # Convert 'date' column to datetime if it exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Sort by date
    if 'date' in df.columns:
        df = df.sort_values('date')

    # Drop columns that are completely empty
    df = df.dropna(axis=1, how='all')

    # Fill missing numeric columns with 0
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    return df

