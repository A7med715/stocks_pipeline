import requests
import logging
import time
from datetime import datetime


logger = logging.getLogger(__name__)

STOCKS = ["AAPL", "GOOGL", "MSFT", "AMZN", "META"]

def extract(water_mark):

    stock = []

    if water_mark is not None:
        water_mark = datetime.strptime(
            str(water_mark),
            "%Y-%m-%d"
        )

    for item in STOCKS:

        url =fr'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={item}&outputsize=compact&apikey=2DVPZIHCOUPO9RHH'

        try:
            response = requests.get(url,timeout=10)
            response.raise_for_status()
            data = response.json()

            symbol = data["Meta Data"]["2. Symbol"]
            time_series = data["Time Series (Daily)"]

            for date_str, values in time_series.items():

                date = datetime.strptime(
                    date_str,
                    "%Y-%m-%d"
                )

                if (
                    water_mark is None
                    or date > water_mark
                ):

                    record = {
                        "symbol": symbol,
                        "date": date_str,
                        "open": values["1. open"],
                        "high": values["2. high"],
                        "low": values["3. low"],
                        "close": values["4. close"],
                        "volume": values["5. volume"]
                    }

                    stock.append(record)
                    logger.info(f'the {item} stocks is flatened')
        
            time.sleep(12)
        except Exception as e:
                logger.error(
                    f"Error extracting {item}: {e}")
                raise
    return stock