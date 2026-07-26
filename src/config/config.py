"""
Configuration module for the Healthcare NoSQL Analytics application.
Centralizes all paths, model parameters, and application settings.
"""
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Project Base Path
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# ---------------------------------------------------------------------------
# Artifact Paths
# ---------------------------------------------------------------------------
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

# Raw data
RAW_DATA_DIR = ARTIFACTS_DIR / "raw_data"
RAW_DATA_FILE = RAW_DATA_DIR / "train.csv"

# Preprocessed data
PREPROCESSED_DATA_DIR = ARTIFACTS_DIR / "preprocessed_data"
PREPROCESSED_DATA_FILE = PREPROCESSED_DATA_DIR / "insurance_processed.csv"
INITIAL_ML_DATA_FILE = PREPROCESSED_DATA_DIR / "insurance_initial_ml_copy.csv"

# Encoders
ENCODERS_DIR = ARTIFACTS_DIR / "encoders"
ENCODERS_FILE = ENCODERS_DIR / "encoders.joblib"

# Scaler
SCALERS_DIR = ARTIFACTS_DIR / "scalers"
SCALER_FILE = SCALERS_DIR / "scaler.joblib"

# Models
MODELS_DIR = ARTIFACTS_DIR / "models"
XGBOOST_MODEL_FILE = MODELS_DIR / "xgboost_model.joblib"
LOGISTIC_REGRESSION_MODEL_FILE = MODELS_DIR / "logistic_regression_model.joblib"

# Metrics
METRICS_DIR = ARTIFACTS_DIR / "metrics"
METRICS_FILE = METRICS_DIR / "evaluation_results.csv"

# Plots
PLOTS_DIR = ARTIFACTS_DIR / "plots"
MATPLOTLIB_PLOTS_DIR = PLOTS_DIR / "matplotlib"
RF_CONFUSION_MATRIX = MATPLOTLIB_PLOTS_DIR / "random_forest_confusion_matrix.png"
RF_FEATURE_IMPORTANCE = MATPLOTLIB_PLOTS_DIR / "random_forest_feature_importance.png"

# ---------------------------------------------------------------------------
# Data Column Information
# ---------------------------------------------------------------------------
# Target column
TARGET_COLUMN = "Response"

# Feature columns (as used in the notebook)
NUMERICAL_FEATURES = ["Age", "Annual_Premium", "Vintage"]
CATEGORICAL_FEATURES_TO_ENCODE = ["Gender", "Vehicle_Age", "Vehicle_Damage"]
BOOLEAN_FEATURES = ["Driving_License", "Previously_Insured"]
OTHER_FEATURES = ["Region_Code", "Policy_Sales_Channel"]
DROP_COLUMNS = ["id"]

# All feature columns expected by the model
ALL_FEATURE_COLUMNS = [
    "Gender",
    "Age",
    "Driving_License",
    "Region_Code",
    "Previously_Insured",
    "Vehicle_Age",
    "Vehicle_Damage",
    "Annual_Premium",
    "Policy_Sales_Channel",
    "Vintage",
]

# ---------------------------------------------------------------------------
# Data Dictionary
# ---------------------------------------------------------------------------
DATA_DICTIONARY = {
    "id": "Unique identifier for each customer",
    "Gender": "Gender of the customer (Male/Female)",
    "Age": "Age of the customer",
    "Driving_License": "Whether the customer has a driving license (0=No, 1=Yes)",
    "Region_Code": "Code representing the region of the customer",
    "Previously_Insured": "Whether the customer already has vehicle insurance (0=No, 1=Yes)",
    "Vehicle_Age": "Age of the vehicle (1-2 Year, < 1 Year, > 2 Years)",
    "Vehicle_Damage": "Whether the vehicle has been damaged before (Yes/No)",
    "Annual_Premium": "Annual premium amount the customer has to pay",
    "Policy_Sales_Channel": "Channel code through which the policy was sold",
    "Vintage": "Number of days the customer has been associated with the company",
    "Response": "Target variable - whether the customer is interested in vehicle insurance (0=No, 1=Yes)",
}

# ---------------------------------------------------------------------------
# Feature descriptions for UI
# ---------------------------------------------------------------------------
FEATURE_DESCRIPTIONS = {
    "Gender": "Gender of the customer (0=Female, 1=Male)",
    "Age": "Age of the customer in years",
    "Driving_License": "Whether the customer has a valid driving license (0=No, 1=Yes)",
    "Region_Code": "Geographical region code of the customer's location",
    "Previously_Insured": "Whether the customer already has vehicle insurance (0=No, 1=Yes)",
    "Vehicle_Age": "Age category of the vehicle (0=<1 Year, 1=1-2 Year, 2=>2 Years)",
    "Vehicle_Damage": "Whether the customer's vehicle has been damaged before (0=No, 1=Yes)",
    "Annual_Premium": "Annual premium amount the customer pays (in currency units)",
    "Policy_Sales_Channel": "Anonymized code representing the policy sales channel",
    "Vintage": "Number of days the customer has been with the company",
}

# ---------------------------------------------------------------------------
# Model Display Names
# ---------------------------------------------------------------------------
MODEL_DISPLAY_NAMES = {
    "Logistic Regression": "Logistic Regression",
    "Random Forest": "Random Forest",
    "XGBoost": "XGBoost (Deployed)",
}

# ---------------------------------------------------------------------------
# Application Settings
# ---------------------------------------------------------------------------
APP_TITLE = "Healthcare NoSQL Analytics — Insurance Cross-Sell Prediction"
APP_ICON = "🏥"
APP_LAYOUT = "wide"
SIDEBAR_STATE = "expanded"

# ---------------------------------------------------------------------------
# Prediction History (in-memory)
# ---------------------------------------------------------------------------
MAX_PREDICTION_HISTORY = 100

