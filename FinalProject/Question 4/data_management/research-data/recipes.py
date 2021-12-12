import json
import pandas as pd

# df is a pandas DataFrame
def df_transpose(df):
    return df.T

def df_to_json(df):
    result = df.to_json()
    parsed = json.loads(result)
    return json.dumps(parsed)

def json_to_df(_json):
    _json = json.loads(_json)
    result = pd.DataFrame.from_dict(_json)
    return result

