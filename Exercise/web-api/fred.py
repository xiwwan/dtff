import requests
import datetime
import json
import pandas as pd
import datetime

root_url = "https://api.stlouisfed.org/fred"
api_key = "f39c886e59678164e4935fa92860e7e5"
limit = 20
observation_start = "2020-01-01"
file_type = "json"
reqt = root_url + f"/series/observations?series_id=UNRATE&api_key={api_key}&limit={limit}" \
                  f"&observation_start={observation_start}&file_type={file_type}"
resp = requests.get(reqt)
df = pd.DataFrame.from_dict(json.loads(resp.text)['observations'])
print(df)