import os
import pandas as pd
from datetime import datetime
import awswrangler as wr   
import uuid


class Saneamento:
    
    def __init__(self, data, configs):
        self.data = data
        self.colunas = configs["metadados"]['nome_original']
        self.colunas_new = configs["metadados"]['nome']
        self.tipos = configs["metadados"]['tipos']  

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
    
def save_bucket(df, configs, step, hdr):
    bucket = configs["bucket"][step]
    file = f"cadastro_{step}_{str(uuid.uuid4())}.csv"
    wr.s3.to_csv(
        df=df,
        path=f"{bucket}{file}",
        header=hdr,
        sep=";",
        index=False,
    )

def error_handler(exception_error, stage, path):
    
    log = [stage, type(exception_error).__name__, exception_error,datetime.now()]
    logdf = pd.DataFrame(log).T
    
    if not os.path.exists(path):
        logdf.columns = ['stage', 'type', 'error', 'datetime']
        logdf.to_csv(path, index=False,sep = ";")
    else:
        logdf.to_csv(path, index=False, mode='a', header=False, sep = ";")
