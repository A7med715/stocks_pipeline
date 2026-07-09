from dotenv import load_dotenv
from pathlib import Path
import os 
import logging
from sqlalchemy import create_engine,text

load_dotenv(Path(__file__).parent.parent / ".env")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger=logging.getLogger(__name__)

STOCKS = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]

def get_engine():
    host=os.getenv('DB_HOST')
    print(repr(host))
    user=os.getenv('DB_USER')
    password=os.getenv('DB_PASSWORD')
    db_name=os.getenv('DB_NAME')

    try:
        engine=create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}",echo=False)
        logger.info('The engine is connectted')
        return engine
    except Exception as e:
        logger.error(f'there was an error in hte connection:{e}')
        raise

def water_mark(engine):
    check_query=text("""SELECT COUNT(*)
                     FROM stock""")
    latest_date=text("""SELECT MAX(trade_date)
                     FROM stock""")
    with engine.connect() as conn:
        count=conn.execute(check_query).scalar()
        date=conn.execute(latest_date).scalar()
        
    if count>0:
        return date
    else:
        return None