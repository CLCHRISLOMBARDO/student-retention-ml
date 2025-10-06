import pandas as pd
from src.config import INPUT_DATA_PATH
import logging

logger=logging.getLogger(__name__)

def cargar_datos(file_name:str)-> pd.DataFrame:
    logger.info("Comienzo de carga de datos")
    try:
        file_path = INPUT_DATA_PATH + file_name
        df=pd.read_csv(file_path)
        logger.info(f"Datos Cargados : df shape -> {df.shape}")
        print(df.head())
    except Exception as e:
        logger.error(f"Error al cargar los datos : {e}")
        raise
    return df