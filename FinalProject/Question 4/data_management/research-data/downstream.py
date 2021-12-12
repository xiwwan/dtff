from connect import mysql_connect, mysql_connect_db
import pandas as pd
from joblib import Memory
from recipes import df_transpose, df_to_json, json_to_df

cachedir = "./datacache"  # set up cache directory
memory = Memory(cachedir) # initialize Memory object

# define and decorate function
@memory.cache
def get_csv_from_sql(sql_statement, conn):
  return pd.read_sql(sql_statement, conn)


if __name__ == "__main__":
  conn = mysql_connect()
  cur = conn.cursor()
  fxCurrency = pd.read_sql("SELECT * FROM fx.currency", conn)
  print(fxCurrency)
  print(df_transpose(fxCurrency))
  fxCurrency_json = df_to_json(fxCurrency)
  print(fxCurrency_json)
  fxCurrency_df = json_to_df(fxCurrency_json)
  print(fxCurrency_df)
  conn.close()