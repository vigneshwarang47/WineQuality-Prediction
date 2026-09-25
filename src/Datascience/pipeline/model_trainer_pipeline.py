from src.Datascience.config.configuration import ConfigurationManager
from src.Datascience.components.model_trainer import ModelTrainer
from src.Datascience import logger

STAGE_NAME = "Model Train Stage" 

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_model_trainer(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>{STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>>Stage: {STAGE_NAME} compeleted<<<<<<n\nx====x")
    except Exception as e:
        logger.exception(e)
        raise e