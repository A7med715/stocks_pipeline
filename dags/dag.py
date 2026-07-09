
import textwrap
from datetime import datetime, timedelta
from airflow.decorators import task
from airflow.sdk import DAG
from pipeline.utils import get_engine,water_mark
from pipeline.extract import extract
from pipeline.transfrom import transform
from pipeline.load import load

with DAG(
    "stock_airflow",
    default_args={
        "depends_on_past": False,
        "retries": 5,
        "retry_delay": timedelta(minutes=2),
    },
    description="A stock data pipeline",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["pipeline"],
) as dag:
    @task
    def watermark_task():
        engine = get_engine()
        return water_mark(engine)

    @task
    def extract_task(last_date):
        return extract(last_date)

    @task
    def transform_task(data):
        return transform(data)

    @task
    def load_task(df):
        engine = get_engine()
        load(df, engine,table='stock')

    last_date = watermark_task()
    raw_data = extract_task(last_date)
    clean_df = transform_task(raw_data)
    load_task(clean_df)
