import pandas as pd
import logging
from sqlalchemy.exc import IntegrityError

logger=logging.getLogger(__name__)

def load(df,engine,table):
    try:
        if df is None or df.empty:
            logger.info("There is no data to upload")
            return
        df.to_sql(con=engine,
                name=table,
                if_exists='append',
                index=False)
        logger.info(f'The data is loaded with {len(df)} rows')
    except IntegrityError as e:
        logger.warning(f'there was dublicates row skipped:{e}')
    except Exception as e:
        logger.error(f"there was an error loading the data:{e}")
        raise