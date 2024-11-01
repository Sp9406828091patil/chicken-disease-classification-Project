from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_03_04_prepare_training_model import ModelTrainigPipeline
from src.cnnClassifier.pipeline.stage_05_prepare_evaluation_pipeline import EvaluationPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>>>> {STAGE_NAME} started >>>>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} end >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare baseline model"
try:
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training model"
try:
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<")
    model_training = ModelTrainigPipeline()
    model_training.main()
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e