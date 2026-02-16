# CDC Healthcare ETL Pipeline

[![Python](https://img.shields.io/badge/python-3.14-blue?logo=python)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/larryzelnick-ai/cdc-healthcare-etl-pipeline)](https://github.com/larryzelnick-ai/cdc-healthcare-etl-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Project Description

This project is an **ETL (Extract, Transform, Load) pipeline** for healthcare data sourced from the [CDC COVID-19 Vaccination Data](https://data.cdc.gov/). It demonstrates hands-on data engineering using **Python**, including:

- Extracting JSON data from a public API  
- Transforming and cleaning data using **pandas**  
- Logging pipeline operations  
- Saving transformed data to CSV files and a local SQLite database  

The pipeline is modular, with separate scripts for extraction, transformation, and loading, making it easy to extend to other datasets.

---

## Tech Stack

- Python 3.14  
- pandas  
- requests  
- SQLAlchemy  
- SQLite  

---

## Getting Started

### Clone the repo

```bash
git clone https://github.com/larryzelnick-ai/cdc-healthcare-etl-pipeline.git
cd cdc-healthcare-etl-pipeline


### Create a Virtual Environment

python -m venv venv
source venv/Scripts/activate   # Windows Git Bash
# or
# source venv/bin/activate     # Linux / Mac


### Install dependencies

pip install -r requirements.txt

### Run the ETL pipeline

python -m src.main

# Pipeline logs are saved to logs/pipeline.log

# CSV outputs are saved to data/cdc_raw_sample_<timestamp>.csv

### Project Structure

cdc-healthcare-etl-pipeline/
├── data/                   # CSV output files
├── logs/                   # Pipeline logs
├── src/
│   ├── extract.py          # Extract data from CDC API
│   ├── transform.py        # Clean & transform data
│   ├── load.py             # Save data to CSV/SQLite
│   └── main.py             # Main ETL pipeline runner
├── .gitignore
├── README.md
└── requirements.txt






