# src/extract.py
import pandas as pd
import requests
import logging

def extract_data():
    """
    Extract JSON data from the CDC API and return a Pandas DataFrame.
    """
    url = "https://data.cdc.gov/resource/8xkx-amqh.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise error for bad status
        data = response.json()       # list of dictionaries
        df = pd.DataFrame(data)      # convert to DataFrame
        return df
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred: {e}")
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in extract_data: {e}")
        raise

