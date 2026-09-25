from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline 
from src.Datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline 
from src.Datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline 
from src.Datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline 
from src.Datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline  


STAGE_NAME  = "Data Ingestion stage"
try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME  = "Data Validation stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME  = "Data Transformation stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.initiate_data_transformation()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME  = "Model Training stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        model_trainer = ModelTrainerTrainingPipeline()
        model_trainer.initiate_model_trainer()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation Stage" 
if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        model_evaluation = ModelEvaluationTrainingPipeline()
        model_evaluation.initiate_model_evaluation()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e