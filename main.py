from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f">>>>>>>> {STAGE_NAME} started >>>>>>>>>>")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> {STAGE_NAME} end >>>>>>>>>>")
except Exception as e:
    logger.exception(e)
    raise e