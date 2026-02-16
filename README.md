# CDC Healthcare ETL Pipeline

This is a demo ETL pipeline that extracts, transforms, and loads CDC healthcare data into a CSV file and a SQLite database.  

## Features

- Extracts data from CDC public JSON API
- Transforms and cleans the data
- Saves timestamped CSV files in `data/`
- Loads transformed data into a SQLite database
- Logs pipeline runs to timestamped log files in `logs/`

## Requirements

- Python 3.10+
- pip

Install dependencies:

```bash
pip install -r requirements.txt

=======
# cdc-healthcare-etl-pipeline
Healthcare data ETL pipeline using Python and SQL.
