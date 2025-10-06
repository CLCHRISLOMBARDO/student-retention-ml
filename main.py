import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import logging
import datetime
import os

from src.config import *
from src.loader import cargar_datos

os.makedirs(LOGS_PATH,exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(OUTPUT_MODELS_PATH, exist_ok=True)

fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
comentario=input(f"Agregue un comentario: ")
name_log=fecha+"_log_"+comentario

# CONFIGURACION LOG
logging.basicConfig(
    level=logging.INFO, #Puede ser INFO o ERROR
    format='%(asctime)s - %(levelname)s - %(name)s %(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_PATH+name_log, mode="w", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Comienzo del flujo")

    # 0.Cargar los datos
    file_name='datos_TP1_2025.csv'
    df=cargar_datos()



    logger.info(f">>> Ejecucion finalizada. Revisar logs para mas detalles. {name_log}")




if __name__=="__main__":
    main()



