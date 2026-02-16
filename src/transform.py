import pandas as pd

def transform_data(df):
    """
    Perform basic transformations on the raw CDC data.

    Steps:
    - Convert 'date' column to datetime
    - Sort by date
    - Drop any columns that are completely empty
    """
    # Convert 'date' column to datetime if it exists
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # Sort by date
    if 'date' in df.columns:
        df = df.sort_values('date')

    # Drop columns that are completely empty
    df = df.dropna(axis=1, how='all')

    return df


