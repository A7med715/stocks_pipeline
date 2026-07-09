import pandas as pd
import numpy as np
from datetime import datetime
import logging

logger=logging.getLogger(__name__)

def transform(stock):
    try:
        df=pd.DataFrame(stock)

        df=df.rename(columns={'date':'trade_date',
                        'open':'open_price',
                        'high':'high_price',
                        'low':'low_price',
                        'close':'close_price',
                        })
        df["trade_date"] = pd.to_datetime(df["trade_date"]).dt.date
        numeric_cols = [
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume"
        ]

        df[numeric_cols] = df[numeric_cols].apply(
            pd.to_numeric
        )
        df['ingested_at']=datetime.now()

        df=df.sort_values(by=['symbol','trade_date'],ascending=[True,True])

        df["pct_change"] = ((df["close_price"] - df["open_price"])/ df["open_price"]) * 100

        logger.info(f'the date is transformed with {df.shape[0]} rows , {df.shape[1]} columns and in a {df['trade_date'].max()-df['trade_date'].min()} range')

        return df
    except Exception as e:
        logger.error(f"there was an error transforming:{e}")
        raise





