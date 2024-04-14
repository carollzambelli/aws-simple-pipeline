import os
import pandas as pd
from datetime import datetime  
from io import StringIO 
import boto3
import uuid
from config import configs

class Saneamento:
    
    def __init__(self, data, configs):
        self.data = data
        self.colunas = configs["metadados"]['nome_original']
        self.colunas_new = configs["metadados"]['nome']
        self.tipos = configs["metadados"]['tipos']
        self.path_work = configs["bucket_work"]        

    def select_rename(self):
        self.data = self.data.loc[:, self.colunas] 
        for i in range(len(self.colunas)):
            self.data.rename(columns={self.colunas[i]:self.colunas_new[i]}, inplace = True)

    def tipagem(self):
        for col in self.colunas_new:
            tipo = self.tipos[col]
            if tipo == "int":
                tipo = self.data[col].astype(int)
            elif tipo == "float":
                self.data[col].replace(",", ".", regex=True, inplace = True)
                self.data[col] = self.data[col].astype(float)
            elif tipo == "date":
                self.data[col] = pd.to_datetime(self.data[col]).dt.strftime('%Y-%m-%d')
        return self.data


def save_bucket(df, configs, step):
    bucket = configs["bucket"]["name"]
    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket('name')
    file = f"{configs["bucket"][step]}cadastro_{step}_{str(uuid.uuid4())}.csv"
    s3_resource.Object(bucket, file).put(Body=csv_buffer.getvalue())


def error_handler(exception_error, stage):
    log = [stage, type(exception_error).__name__, exception_error,datetime.now()]
    logdf = pd.DataFrame(log).T
    save_bucket(logdf, configs, step="logs")
