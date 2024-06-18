import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

# Gett the environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Create database url and create engine
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

def get_commodities_data(symbol, period='5d', interval='1d'):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['symbol'] = symbol  # Add ticket symbol column
    return data

def get_all_commodities_data(commodities):
    full_data = []
    for ticker in commodities:
        data = get_commodities_data(ticker)
        full_data.append(data)
    return pd.concat(full_data)

def write_to_postgres(df, schema='public'):
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)
    

if __name__ == "__main__":
    concat_data = get_all_commodities_data(commodities)
    write_to_postgres(concat_data, schema='public')