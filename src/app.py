
from datetime import datetime
import requests
import pandas as pd
import logging
from config import configs
import utils

config_file = configs

logging.basicConfig(level=logging.INFO)

def ingestion():
    """
    Função de ingestão dos dados
    Outputs: Salva base raw em local específico e retorna o nome do arquivo
    """
    
    logging.info("Iniciando a ingestão")
    api_url = configs['URL']

    try:
        response = requests.get(api_url, timeout=10).json()
        data = response['results']
    except Exception as exception_error:
         utils.error_handler(exception_error, 'read_api')

    df = pd.json_normalize(data)
    df['load_date'] = datetime.now().strftime("%H:%M:%S")

    utils.save_bucket(df, configs, step="raw")


def preparation(file):
    """
    Função de preparação dos dados: renomeia, tipagem, normaliza strings
    Arguments: file -> nome do arquivo raw
    Outputs: Salva base limpa em local específico
    """

    logging.info("Iniciando a preparação")
    df = pd.read_csv(file, sep=";")
    san = utils.Saneamento(df, config_file)
    san.select_rename()
    logging.info("Dados renomeados e selecionados")
    san.tipagem()
    logging.info("Dados tipados")
    san.save_work()
    logging.info("Dados salvos")


def handler(event, context):

    step = event.get('step')

    if step == "ingestion": ingestion()
    else: 
        file_name = event.get('file_name')
        preparation(file_name)
    
