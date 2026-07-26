"""
Application-wide constants, messages, and display strings.
These are derived from the notebook analysis and kept static.
"""

# ---------------------------------------------------------------------------
# Page labels
# ---------------------------------------------------------------------------
PAGE_HOME = "🏠 Home"
PAGE_PREDICTION = "🎯 Prediction"
PAGE_MODEL_INFO = "📊 Model Information"
PAGE_DATA_INSIGHTS = "📈 Data Insights"
PAGE_VISUALIZATIONS = "📉 Visualizations"
PAGE_METRICS = "📋 Metrics"
PAGE_ABOUT = "ℹ️ About"
PAGE_DOWNLOAD = "⬇️ Download Center"

PAGES = [
    PAGE_HOME,
    PAGE_PREDICTION,
    PAGE_MODEL_INFO,
    PAGE_DATA_INSIGHTS,
    PAGE_VISUALIZATIONS,
    PAGE_METRICS,
    PAGE_ABOUT,
    PAGE_DOWNLOAD,
]

# ---------------------------------------------------------------------------
# Home page
# ---------------------------------------------------------------------------
HOME_HEADING = "Insurance Cross-Sell Prediction"
HOME_SUBHEADING = (
    "An end-to-end machine learning application combining "
    "NoSQL analytics with predictive modeling."
)

# ---------------------------------------------------------------------------
# Prediction page
# ---------------------------------------------------------------------------
PREDICTION_HEADING = "Predict Customer Interest"
PREDICTION_DESCRIPTION = (
    "Enter customer details below to predict whether they will be "
    "interested in vehicle insurance."
)

# ---------------------------------------------------------------------------
# Model info
# ---------------------------------------------------------------------------
MODEL_INFO_HEADING = "Model Information"
MODEL_DEPLOYED = "XGBoost"

# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------
METRICS_HEADING = "Model Evaluation Metrics"

# ---------------------------------------------------------------------------
# Visualizations
# ---------------------------------------------------------------------------
VIZ_HEADING = "Visualizations"

# ---------------------------------------------------------------------------
# Data Insights
# ---------------------------------------------------------------------------
DATA_INSIGHTS_HEADING = "Data Insights"

# ---------------------------------------------------------------------------
# Download
# ---------------------------------------------------------------------------
DOWNLOAD_HEADING = "Download Center"

# ---------------------------------------------------------------------------
# About page content
# ---------------------------------------------------------------------------
ABOUT_PROJECT_OVERVIEW = """
This project demonstrates the integration of **NoSQL (MongoDB)** data operations with **Machine Learning**
to solve a real-world business problem — predicting customer interest in vehicle insurance.

The workflow includes:
- **Data Exploration & Cleaning** using Pandas
- **NoSQL Operations** simulated with MongoMock (CRUD, Aggregation Pipeline)
- **Feature Engineering** (encoding categorical variables, scaling numerical features)
- **Model Training** with Logistic Regression, Random Forest, and XGBoost
- **Model Evaluation** using Accuracy, Precision, Recall, F1-Score, and ROC-AUC
- **Deployment** via this interactive Streamlit application
"""

ABOUT_BUSINESS_PROBLEM = """
A health insurance company wants to cross-sell vehicle insurance to its existing customers.
They have provided a dataset of customer demographics, policy information, and vehicle details.
The goal is to build a predictive model that identifies customers most likely to be interested
in purchasing vehicle insurance, enabling the company to target its marketing efforts efficiently.
"""

ABOUT_DATASET_DESCRIPTION = """
The dataset contains **381,109 customer records** with 11 features and a binary target.

**Features:**
- **Demographics:** Gender, Age, Driving License, Region Code
- **Insurance History:** Previously Insured, Vehicle Age, Vehicle Damage
- **Policy Details:** Annual Premium, Policy Sales Channel, Vintage

**Target:**
- **Response:** Whether the customer is interested in vehicle insurance (0=No, 1=Yes)

The dataset is imbalanced — approximately 12% of customers responded positively.
"""

ABOUT_ML_WORKFLOW = """
1. **Data Preprocessing**
   - Label encoding for Gender, Vehicle Age, Vehicle Damage
   - Standard scaling for Age, Annual Premium, Vintage
   - Train-test split (80-20)

2. **Model Training**
   - Logistic Regression (baseline)
   - Random Forest with RandomizedSearchCV
   - **XGBoost** (selected for deployment)

3. **Evaluation**
   - Accuracy, Precision, Recall, F1-Score, ROC-AUC
   - Confusion Matrix visualization
   - Feature Importance analysis

The **XGBoost model** is deployed in this application due to its superior ROC-AUC score
and balanced performance across all metrics.
"""

ABOUT_TECH_STACK = """
- **Frontend:** Streamlit
- **Backend:** Python 3.10+
- **Data Processing:** Pandas, NumPy
- **NoSQL:** PyMongo, MongoMock
- **Machine Learning:** Scikit-learn, XGBoost
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Model Serialization:** Joblib
- **Deployment:** Streamlit Cloud / Render / Railway
"""

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
FOOTER_TEXT = (
    "Built with ❤️ using Streamlit | "
    "Healthcare NoSQL Analytics Portfolio Project"
)

