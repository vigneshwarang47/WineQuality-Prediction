from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline 


STAGE_NAME  = "Data Ingestion stage"
try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
except Exception as e:
    logger.exception(e)
    raise e