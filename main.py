from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.statge_01_data_ingestion import DataIngestionTrainigPipleine
from src.textSummarizer.pipeline.statge_02_data_validation import DataValidationTrainigPipleine
from src.textSummarizer.pipeline.statge_03_data_transformation import DataTransformationTrainingPipeline
from src.textSummarizer.pipeline.statge_04_model_trainer import ModelTrainingPipeline
from src.textSummarizer.pipeline.statge_05_model_evaluation import ModelEvaluationPipeline


statge_name = 'Data Ingestion'
try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainigPipleine()
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e



statge_name = 'Data Validation'
try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    data_validation = DataValidationTrainigPipleine()
    data_validation.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e

statge_name = 'Data Transformation'
try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    data_tranformation = DataTransformationTrainingPipeline()
    data_tranformation.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e


statge_name = 'Model Training'
try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    model_train = ModelTrainingPipeline()
    model_train.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e

statge_name = 'Model Evaluation'
try: 
    logger.info(f'>>>>>>>>>> statge {statge_name} started <<<<<<<<<<<<<')
    model_train = ModelEvaluationPipeline()
    model_train.main()
    logger.info(f'>>>>>>>>>> statge {statge_name} compleated <<<<<<<<<<<<<  \n\nx=============x')
except Exception as e:
    logger.exception(e)
    raise e