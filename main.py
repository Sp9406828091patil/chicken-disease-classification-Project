from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

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