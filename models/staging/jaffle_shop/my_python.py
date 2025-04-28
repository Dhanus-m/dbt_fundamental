import snowflake.snowpark.functions as F

def model(dbt, session):
    dbt.config(materialized = "incremental")
    df = dbt.ref("stg_customers")

    return df