import yfinance as yf
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

commodities = ['CL=F', 'GC=F', 'SI=F']

def get_commodities_data(ticker, period='5d', interval='1d'):
    ticker = yf.Ticker(ticker)
    data = ticker.history(period=period, interval=interval)[['Close']]
    data['simbolo'] = ticker  # Add ticket column
    return data

def get_all_commodities_data(commodities):
    full_data = []
    for simbolo in commodities:
        dados = get_commodities_data(simbolo)
        full_data.append(dados)
    return pd.concat(full_data)

if __name__ == "__main__":
    concat_data = get_all_commodities_data(commodities)
    print(concat_data)