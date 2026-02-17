# CDC Healthcare ETL Pipeline

[![Python](https://img.shields.io/badge/python-3.14+-blue?logo=python)](https://www.python.org/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/larryzelnick-ai/cdc-healthcare-etl-pipeline)](https://github.com/larryzelnick-ai/cdc-healthcare-etl-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Project Description

This project is a modular **ETL (Extract, Transform, Load) pipeline** built using real-world healthcare data from the [CDC COVID-19 Vaccination Data API](https://data.cdc.gov/).

It demonstrates practical data engineering skills including API ingestion, data transformation, structured logging, and relational database loading.

The pipeline is structured using separate modules for extraction, transformation, and loading to promote maintainability and scalability.

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

---

## Output

- **Logs:** `logs/pipeline_<YYYYMMDD_HHMMSS>.log`
- **CSV Output:** `data/cdc_raw_sample_<YYYYMMDD_HHMMSS>.csv`
- **SQLite Database:** stored locally (see configuration in source code)


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






