import pandas as pd
import awswrangler as wr


def lambda_handler(event, context):
    sql = "SELECT * FROM cadastro"
    df = wr.athena.read_sql_query(sql, database='database')
    print(df)
