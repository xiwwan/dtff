# web-api

## Binance API:
### What is the root URL?

It is "https://api.binance.com"

### What is the endpoint to retrieve klines (open-high-low-close data) for a specific cryptocurrency?

It is "/api/v3/klines"

### Specify a request string to retrieve 75 observations of klines data for BTCUSDT since 2021-06-15.
"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&startTime=1623715200000&limit=75"

### Write a function (in Python, R or Julia) that retrieves 75 observations of klines data for a generic currency pair since a generic date. The function should take the currency pair and start date as input parameters.
See *binance.py*

## FRED API:
### Read how authentication with API keys works. Create an account and obtain your own key.
See fred_api.txt

FRED API Key:
f39c886e59678164e4935fa92860e7e5

### What is the root URL?
It is "https://api.stlouisfed.org/fred"

### What is the endpoint to retrieve time series observations?
It is "/series/observations"

### Construct a query string to retrieve the series of the monthly unemployment rate (seasonally adjusted) since 2020-01. Use the fake API key abc123 in the query string.
"https://api.stlouisfed.org/fred/series/observations?series_id=UNRATE&api_key=abc123&limit=20&observation_start=2020-01-01&file_type=json"

For more details, see fred.py


