import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Connect to the database
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create connection engine with the database
engine = create_engine(DATABASE_URL)

# Query data from trusted_commodities table
def get_commodities_data():
    query = f"""
    SELECT
        date,
        symbol,
        closing_price,
        action,
        quantity,
        value,
        balance
    FROM
        public.trusted_commodities;
    """

    try:
        df_commodities = pd.read_sql(query, engine)
        return df_commodities
    except ProgrammingError as e:
        st.error(f"Error while trying to access the 'trusted_commodities' table in schema '{DB_SCHEMA}': {e}")
        return pd.DataFrame()  # Returns an empty Dataframe in case of error

# Setup Streamlit page
st.set_page_config(page_title='Commodities Dashboard', layout='wide')

# Título do Dashboard
st.title('Commodities Dashboard')

# Descrição
st.write("""
Commodities Dashboard with transactions values from last day.
""")

# Obter os dados
df = get_commodities_data()

# Verificar se o DataFrame está vazio
if df.empty:
    st.write("It was not possible to load the data. Check if the table 'trusted_commodities' exists in the schema.")
else:
    # Exibir os dados
    st.write("### Commodities Data")
    st.dataframe(df)

    # Resumo estatístico
    st.write("### Summary")
    st.write(df.describe())

    # Gráficos
    st.write("### Visuals")

    # Gráfico de barras para ganhos e perdas
    st.bar_chart(df[['date', 'balance']].set_index('date'))

    # Gráfico de linha para valores de fechamento
    st.line_chart(df[['date', 'closing_price']].set_index('date'))