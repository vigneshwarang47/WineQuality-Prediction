from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.model_evaluation import ModelEvaluation
from src.Datascience import logger

STAGE_NAME = "Model Evaluation Stage" 

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e