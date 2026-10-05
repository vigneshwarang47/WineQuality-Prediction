# Wine Quality Prediction — End-to-End MLOps Pipeline

An end-to-end Machine Learning project for predicting **wine quality** from physicochemical properties of red wine.

The project is organized as a modular ML pipeline covering **data ingestion, data validation, data transformation, model training, model evaluation, experiment tracking with MLflow/DagsHub, and Flask-based prediction**.

## Project Overview

The objective is to build a regression model that predicts the `quality` score of red wine using measurable physicochemical features.

The project follows a structured pipeline instead of keeping the complete workflow inside a single notebook. Configuration, parameters, schema definitions, pipeline stages, model artifacts, and prediction logic are separated into dedicated modules.

### Target

**Target variable:** `quality`

### Input features

- Fixed acidity
- Volatile acidity
- Citric acid
- Residual sugar
- Chlorides
- Free sulfur dioxide
- Total sulfur dioxide
- Density
- pH
- Sulphates
- Alcohol

## Machine Learning Workflow

```text
Wine Quality Dataset
        │
        ▼
┌──────────────────────┐
│   Data Ingestion     │
│ Download ZIP Dataset │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│   Data Validation    │
│ Schema Verification  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Data Transformation  │
│ Train/Test Split     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│    Model Training    │
│      ElasticNet      │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  Model Evaluation    │
│ RMSE / MAE / R²      │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ MLflow + DagsHub     │
│ Experiment Tracking  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Flask Prediction API │
│   Wine Quality App   │
└──────────────────────┘
```

## Project Structure

```text
Datascienceproject/
│
├── .github/
│   └── workflows/
│
├── config/
│   └── config.yaml
│
├── research/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_validation.ipynb
│   ├── 03_data_transformation.ipynb
│   ├── 04_model_trainer.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── research.ipynb
│
├── src/
│   └── Datascience/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       │
│       ├── config/
│       │   ├── common.py
│       │   └── configuration.py
│       │
│       ├── constants/
│       │   └── __init__.py
│       │
│       ├── entity/
│       │   └── config_entity.py
│       │
│       ├── pipeline/
│       │   ├── data_ingestion_pipeline.py
│       │   ├── data_validation_pipeline.py
│       │   ├── data_transformation_pipeline.py
│       │   ├── model_trainer_pipeline.py
│       │   ├── model_evaluation_pipeline.py
│       │   └── prediction_pipeline.py
│       │
│       └── utils/
│           └── common.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── app.py
├── config/
├── main.py
├── params.yaml
├── schema.yaml
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| ElasticNet | Regression model |
| MLflow | Experiment tracking and model logging |
| DagsHub | Remote MLflow tracking |
| Flask | Prediction web application |
| Joblib | Model serialization |
| PyYAML | Configuration management |
| Python Box | Configuration access |
| Jupyter Notebook | Experimentation and research |
| Git/GitHub | Version control |

## Dataset

The project uses the **Wine Quality dataset** containing physicochemical measurements of red wine.

Dataset source:

`https://github.com/krishnaik06/datasets/raw/refs/heads/main/winequality-data.zip`

The dataset contains the following columns:

```text
fixed acidity
volatile acidity
citric acid
residual sugar
chlorides
free sulfur dioxide
total sulfur dioxide
density
pH
sulphates
alcohol
quality
```

The `quality` column is used as the regression target.

## Model

The current implementation uses **ElasticNet Regression** from Scikit-learn.

Model parameters are maintained in `params.yaml`:

```yaml
ElasticNet:
  alpha: 0.2
  l1_ratio: 0.1
```

The model is trained using the 11 physicochemical features and predicts the wine `quality` score.

The trained model is serialized using Joblib:

```text
artifacts/model_trainer/model.joblib
```

## Model Evaluation

The model evaluation component calculates:

- **RMSE** — Root Mean Squared Error
- **MAE** — Mean Absolute Error
- **R²** — Coefficient of Determination

The metrics are also saved locally:

```text
artifacts/model_evaluation/metrics.json
```

## MLflow & DagsHub

MLflow is used for experiment tracking.

The evaluation stage records:

- Model parameters
- RMSE
- MAE
- R²
- Trained model artifact

The project is configured to use DagsHub as the remote MLflow tracking service.

> **Security:** MLflow/DagsHub credentials should be stored as environment variables or GitHub/CI secrets. Do not commit access tokens or passwords directly to source code.

## Flask Application

The project includes a Flask web application for making predictions.

Start the application with:

```bash
python app.py
```

The application provides:

```text
/
```

for the input form and:

```text
/predict
```

for submitting wine physicochemical properties and obtaining a predicted quality score.

### Prediction flow

```text
User Input
    ↓
Flask Application
    ↓
PredictionPipeline
    ↓
Trained ElasticNet Model
    ↓
Predicted Wine Quality
    ↓
Results Page
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vigneshwarang47/Datascienceproject.git
cd Datascienceproject
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the ML Pipeline

Execute:

```bash
python main.py
```

The pipeline runs the following stages:

```text
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation
```

Generated artifacts are stored under the `artifacts/` directory.

## Run the Prediction Application

After training the model:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

Enter the wine properties in the form and submit them to obtain the predicted quality.

## Configuration

Pipeline configuration is maintained in:

```text
config/config.yaml
```

Model hyperparameters are maintained in:

```text
params.yaml
```

Dataset schema and target configuration are maintained in:

```text
schema.yaml
```

This keeps configuration separate from the implementation code and makes the pipeline easier to maintain.

## Key Engineering Practices

This project demonstrates:

- Modular ML pipeline architecture
- Configuration-driven development
- Separation of pipeline components
- Reusable configuration manager
- Schema-based data validation
- Model artifact management
- Experiment tracking with MLflow
- Remote experiment tracking with DagsHub
- Custom prediction pipeline
- Flask-based model serving
- Logging throughout pipeline stages
- Research-to-production workflow

## Research-to-Production Workflow

The `research/` directory contains notebooks used to explore and develop individual pipeline stages:

```text
01_data_ingestion.ipynb
02_data_validation.ipynb
03_data_transformation.ipynb
04_model_trainer.ipynb
05_model_evaluation.ipynb
```

The final implementation is organized into reusable Python components under `src/Datascience/`.

This separates experimentation from the production-oriented pipeline code.

## Future Improvements

- [ ] Add automated unit and integration tests
- [ ] Improve schema validation to verify both column names and data types
- [ ] Add automated CI/CD using GitHub Actions
- [ ] Complete Docker-based application deployment
- [ ] Add model comparison with additional regression algorithms
- [ ] Add hyperparameter optimization
- [ ] Improve prediction input validation
- [ ] Add model monitoring
- [ ] Move all MLflow/DagsHub credentials to environment variables
- [ ] Improve Flask UI and prediction result presentation

## Author

**Vigneshwaran G**

Data Science | Machine Learning | MLOps

GitHub:  
https://github.com/vigneshwarang47

## License

This project is licensed under the terms of the included `LICENSE` file.
