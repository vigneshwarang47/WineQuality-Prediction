import pandas as pd
import os
from src.Datascience import logger
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from urllib.parse import urlparse
import mlflow.sklearn
import numpy as np
import joblib
from src.Datascience.entity.config_entity import ModelEvaluationConfig
from src.Datascience.utils.common import save_json
from pathlib import Path

os.environ["MLFLOW_TRACKING_URI"] ="https://dagshub.com/vigneshwaran.g47/Datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "vigneshwaran.g47"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "57917e002cd9591437f542b42c7fa223292a6579"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evaluation_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def log_into_mlflow(self):
        
        test_data =pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]
        
        # Set MLflow tracking/registry URI
        mlflow.set_registry_uri(self.config.mlflow_uri)
        
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            
            # Prediction
            predicted_quality = model.predict(test_x)
            # Evaluation
            (rmse, mae, r2) = self.evaluation_metrics(test_y, predicted_quality)

            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/ml/model-registry.html#api-workflow

                mlflow.sklearn.log_model(
                    model,
                    name="model"
                )
            else:
                mlflow.sklearn.log_model(
                                    model,
                                    name="model"
                                )