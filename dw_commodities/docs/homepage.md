{% docs __overview__ %}

### DBT-Core Project README

# DBT-Core Project for Commodities Data Warehouse

This project uses DBT (Data Build Tool) to manage and transform data from a commodity Data Warehouse (DW). The goal is to create a robust and efficient data pipeline that processes and organizes commodity data and its movements for analysis.

## Project Structure

### 1. Seeds

Seeds are static data that are loaded into the Data Warehouse from CSV files. In this project, we use seeds to load commodity transaction data.

### 2. Models

Models define data transformations using SQL. They are divided into two main layers: raw and trusted.

#### Raw

The raw layer is responsible for preparing and cleaning data before it is loaded into the final analysis tables.

- **raw_commodities.sql**: Treats and formats commodity data extracted from the API.
- **raw_commodities_sell.sql**: Treats and formats commodity transaction data.

#### Trusted

The trusted layer is where the final analysis data is stored. They are based on the data prepared by the staging layer.

- **trusted_commodities.sql**: Integrates the processed commodity and transaction data, creating a final data model for analysis.

### 3. Sources

Sources are the data source tables or files that DBT uses to perform transformations.

### 4. Snapshots

Snapshots are used to keep a history of how data changes over time.

## Directory Structure

```plaintext
├── models
│ ├── raw
│ │ ├── raw_commodities.sql
│ │ └── raw_commodities_sell.sql
│ └── trusted
│ └── trusted_commodities.sql
├── seeds
│ └── commodities_sell.csv
├── dbt_project.yml
└── README.md
```

## Running the Project

### Requirements

- Python 3.7+
- DBT

### Steps for Execution

1. **Clone the Repository**:
    ```bash
    git clone <Repository-URL>
    cd <Repository-Name>
    ```

2. **Install DBT**:
    ```bash
    pip install dbt-core dbt-postgres
    ```

3. **Configure DBT**:
    - Configure the `profiles.yml` file to connect to your Data Warehouse. The file must be in the `~/.dbt/` directory or in the directory specified by the `DBT_PROFILES_DIR` environment variable.

    `profiles.yml` example:
    ```yaml
    databasesales:
    target: dev
    outputs:
    dev:
    type: postgres
    host: <DB_HOST_PROD>
    user: <DB_USER_PROD>
    password: <DB_PASS_PROD>
    port: <DB_PORT_PROD>
    dbname: <DB_NAME_PROD>
    schema: <DB_SCHEMA_PROD>
    threads: 1
    ```

4. **Run DBT Seeds**:
    ```bash
    dbt seed
    ```

5. **Run the DBT Transformations**:
    ```bash
    dbt run
    ```

6. **Check Project Status**:
    ```bash
    dbt test
    ```

## Contribution

To contribute to the project, please fork the repository and submit a pull request with your changes.

---

### Description of Models

#### raw_commodities.sql

This model is responsible for processing and formatting the commodity data extracted from the API. It does the necessary cleaning and transformation to prepare the data for the trusted stage.

#### raw_commodities_sell.sql

This model is responsible for processing and formatting commodity transaction data. It does the necessary cleaning and transformation to prepare the data for the trusted stage.

#### dm_commodities.sql

This model integrates the processed commodity and transaction data, creating a final data model for analysis. It calculates metrics and aggregates data to facilitate analysis on the dashboard.

{% enddocs %}