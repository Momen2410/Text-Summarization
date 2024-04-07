from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.statge_01_data_ingestion import DataIngestionTrainigPipleine


statge_name = 'Data Ingestion'


try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainigPipleine()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e
