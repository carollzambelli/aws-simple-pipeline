import pandas as pd
import awswrangler as wr

sql = "SELECT * FROM cadastro"
df = wr.athena.read_sql_query(sql, database='database')

print(df)