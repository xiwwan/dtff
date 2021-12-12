import requests
import datetime
import json
import pandas as pd
import datetime

def get_klines(date="2021-06-15", symbol="BTCUSDT"):
    root_url = "https://api.binance.com"
    endpoint = "api/v3/klines"
    interval = "1d"
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    # t should be in miliseconds, so we multiplied it by 1000
    startTime = (date - datetime.datetime(1970,1,1)).total_seconds() * 1000
    startTime = int(startTime)
    limit = 75
    reqt = f"{root_url}/{endpoint}?symbol={symbol}&interval={interval}&startTime={startTime}&limit={limit}"
    resp = requests.get(reqt)
    # convert to DataFrame
    data = pd.DataFrame.from_records(
        resp.json(),
        columns=["Open time","Open","High","Low","Close","Volume","Close time","Quote asset volume",
                 "Number of trades","Taker buy base asset volume","Taker buy quote asset volume","Ignore"]
    )
    data = data.drop(columns="Ignore")
    return data

# driver part
if __name__ == "__main__":
    df = get_klines()
    print(df)