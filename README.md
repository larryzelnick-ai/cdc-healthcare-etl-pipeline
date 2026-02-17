# CDC Healthcare ETL Pipeline
A modular, production-style ETL pipeline that ingests, transforms, and stores CDC vaccination data using Python and SQLite.

[![Python](https://img.shields.io/badge/python-3.14+-blue?logo=python)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/larryzelnick-ai/cdc-healthcare-etl-pipeline)](https://github.com/larryzelnick-ai/cdc-healthcare-etl-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Project Description

This project is a modular **ETL (Extract, Transform, Load) pipeline** built using real-world healthcare data from the [CDC COVID-19 Vaccination Data API](https://data.cdc.gov/).

It demonstrates practical data engineering concepts including API ingestion, data transformation, structured logging, and relational database loading within a reproducible local development environment.

The project simulates a real-world healthcare data pipeline and reflects production-oriented engineering practices.

The codebase is organized into dedicated extract, transform, and load modules to promote maintainability and scalability.

---

## Architecture Overview

The pipeline follows a modular ETL design pattern:

- **Extract** → Retrieves vaccination data from the CDC public API  
- **Transform** → Cleans, validates, and structures the dataset using pandas  
- **Load** → Writes processed data to timestamped CSV files and a local SQLite database  

This separation of concerns improves maintainability, scalability, and testability.

---

## Key Features

- Modular ETL architecture (separate `extract`, `transform`, `load` layers)
- JSON data ingestion from a public REST API
- Data cleaning and transformation using **pandas**
- Structured logging to file
- CSV output with timestamped filenames
- SQLite database loading using **SQLAlchemy**
- Virtual environment setup for reproducibility

---

## Tech Stack

- Python 3.14+
- pandas
- requests
- SQLAlchemy
- SQLite

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/larryzelnick-ai/cdc-healthcare-etl-pipeline.git
cd cdc-healthcare-etl-pipeline
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
# or
source venv/bin/activate      # Linux / macOS
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the ETL Pipeline

```bash
python -m src.main
```

This command performs the full ETL workflow:

1. **Extract** the latest CDC vaccination data  
2. **Transform** and clean the data  
3. **Load** results to CSV and SQLite database  
4. **Log** pipeline progress to a timestamped log file

---

## Output

- **Logs:** `logs/pipeline_<YYYYMMDD_HHMMSS>.log`
- **CSV Output:** `data/cdc_raw_sample_<YYYYMMDD_HHMMSS>.csv`
- **SQLite Database:** `data/cdc_data.db`

Each pipeline run creates a new timestamped CSV and log file.  
The SQLite database is updated on each run.


---

## Project Structure

```
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
```

## Querying the SQLite Database

After running the ETL pipeline, the processed data is stored locally at:

data/cdc_data.db

You can explore the database using Python and pandas:

Connect using sqlite3.connect("data/cdc_data.db")

Load data with pd.read_sql_query("SELECT * FROM cdc_data;", conn)

Preview rows with df.head()

Inspect available columns with df.columns.tolist()

This allows you to perform further SQL queries and analytical exploration directly from Python.

---

## Future Improvements

- Containerization with Docker
- Workflow orchestration with Apache Airflow
- Unit testing with pytest
- Cloud storage integration (AWS S3)
- Deployment to cloud-based relational databases (PostgreSQL / RDS)

---

## License

This project is licensed under the MIT License.
