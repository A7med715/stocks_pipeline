# Stock Market ETL Pipeline with Apache Airflow

A production-style ETL pipeline that extracts daily stock market data from the Alpha Vantage API, transforms it using Pandas, and loads it into a MySQL database. The entire workflow is orchestrated with Apache Airflow and containerized using Docker.

---

## Project Overview

This project demonstrates how to build an automated data engineering pipeline using modern tools commonly found in industry.

The pipeline performs the following steps:

1. Extracts stock market data from the Alpha Vantage API.
2. Uses a watermark to retrieve only newly available records.
3. Cleans and transforms the extracted data.
4. Loads the transformed data into MySQL.
5. Schedules and orchestrates the workflow using Apache Airflow.

---

## Architecture

```
                Alpha Vantage API
                        │
                        ▼
                 Extract Task
                        │
                        ▼
              Data Transformation
                        │
                        ▼
                 Load into MySQL
                        │
                        ▼
             Apache Airflow Scheduler
```

---

## Tech Stack

- Python 3
- Apache Airflow 3
- Docker
- Docker Compose
- MySQL
- Pandas
- SQLAlchemy
- PyMySQL
- python-dotenv
- Requests

---

## Project Structure

```
.
├── dags/
│   └── dag.py
├── config/
│   └── airflow.cfg
├── logs/
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
├── .env
└── README.md
```

---

## Pipeline Workflow

### 1. Watermark

Retrieves the latest loaded trade date from the database.

This allows the pipeline to perform **incremental loading** instead of downloading all historical data every time.

---

### 2. Extract

Downloads stock data from the Alpha Vantage API.

The pipeline currently processes multiple stock symbols and converts the API response into a flat structure suitable for loading.

---

### 3. Transform

Performs data cleaning and preprocessing including:

- Date formatting
- Data type conversion
- Column renaming
- Removing unnecessary fields
- Preparing the dataset for database insertion

---

### 4. Load

Loads the transformed data into MySQL using SQLAlchemy.

Duplicate records are prevented using database constraints.

---

## Features

- Incremental loading using watermarks
- Dockerized environment
- Apache Airflow orchestration
- Automatic scheduling
- Modular ETL design
- Environment variable support
- MySQL integration
- Logging
- Easy deployment

---

## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/stock-airflow-pipeline.git

cd stock-airflow-pipeline
```

---

### Configure Environment Variables

Create a `.env` file.

Example:

```env
AIRFLOW_IMAGE_NAME=apache/airflow:3.2.2
AIRFLOW_UID=50000

MYSQL_ROOT_PASSWORD=your_password
MYSQL_DATABASE=stock_db
MYSQL_USER=airflow_user
MYSQL_PASSWORD=your_password

API_KEY=YOUR_ALPHA_VANTAGE_KEY
```

---

### Build the Docker Image

```bash
docker compose build
```

---

### Start Airflow

```bash
docker compose up -d
```

---

### Open Airflow

```
http://localhost:8080
```

Default credentials

```
Username: airflow

Password: airflow
```

---

## Airflow DAG

The DAG consists of the following tasks:

```
Watermark
     │
     ▼
Extract
     │
     ▼
Transform
     │
     ▼
Load
```

Each task executes only after the previous one has completed successfully.

---

## Database

The processed data is stored in a MySQL database.

The table uses a unique constraint to prevent duplicate records during incremental loads.

---

## Docker

The project runs entirely inside Docker containers.

Containers include:

- Apache Airflow Webserver
- Apache Airflow Scheduler
- MySQL
- Airflow Initialization

This makes the project portable and easy to deploy on any machine with Docker installed.


---

## Author

Ahmed Hassan

Computer Science Student
67

GitHub: https://github.com/A7med715