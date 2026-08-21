# 🚗 Insurance Cross-Sell NoSQL Analytics

An end-to-end Machine Learning and NoSQL Analytics project that combines **MongoDB aggregation pipelines**, **customer analytics**, **feature engineering**, and **predictive modeling** to identify customers most likely to purchase vehicle insurance.

<p align="center">
  <img src="https://uxwing.com/wp-content/themes/uxwing/download/business-professional-services/car-insurance-icon.png" alt="Insurance Cross-Sell Icon" width="80"/>
  <br>
  <em>Production-ready Streamlit application</em>
</p>

---

## 📋 Table of Contents

- [🚗 Insurance Cross-Sell NoSQL Analytics](#-insurance-cross-sell-nosql-analytics)
  - [📋 Table of Contents](#-table-of-contents)
  - [🚀 Overview](#-overview)
  - [💼 Business Problem](#-business-problem)
  - [📦 Dataset](#-dataset)
    - [Features](#features)
  - [🔬 Machine Learning Workflow](#-machine-learning-workflow)
    - [Model Performance](#model-performance)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [📁 Project Structure](#-project-structure)
  - [🔧 Installation](#-installation)
    - [Prerequisites](#prerequisites)
    - [Local Setup](#local-setup)
  - [🎯 Usage](#-usage)
  - [🌐 Deployment](#-deployment)
    - [Streamlit Community Cloud (Recommended)](#streamlit-community-cloud-recommended)
    - [Render](#render)
    - [Railway](#railway)
  - [📸 Screenshots](#-screenshots)
  - [🔗 Links](#-links)
  - [👤 Author](#-author)

---

## 🚀 Overview

This project demonstrates a complete data science pipeline:

1. **Data Exploration & Cleaning** — Pandas and data profiling
2. **NoSQL Operations** — CRUD and aggregation pipelines with MongoMock
3. **Feature Engineering** — Label encoding, standard scaling
4. **Model Training** — Logistic Regression, Random Forest, XGBoost
5. **Model Evaluation** — Accuracy, Precision, Recall, F1, ROC-AUC
6. **Deployment** — Interactive Streamlit web application

The **XGBoost** model is deployed in production due to its superior ROC-AUC score (0.8556) and lightweight footprint (~2 MB).

---

## 💼 Business Problem

A health insurance company wants to **cross-sell vehicle insurance** to its existing customers. The goal is to build a predictive model that identifies customers most likely to be interested in purchasing vehicle insurance, enabling the marketing team to:

- Target high-potential customers efficiently
- Reduce marketing costs
- Increase conversion rates
- Improve customer experience

---

## 📦 Dataset

- **Size:** 381,109 customer records
- **Features:** 10 (demographics, policy details, vehicle information)
- **Target:** `Response` — whether customer is interested in vehicle insurance (0 = No, 1 = Yes)
- **Imbalance:** ~12% positive class, ~88% negative class

### Features

| Feature | Description |
|---|---|
| `Gender` | Customer gender (Male/Female) |
| `Age` | Customer age in years |
| `Driving_License` | Has driving license (0/1) |
| `Region_Code` | Geographic region code |
| `Previously_Insured` | Already has vehicle insurance (0/1) |
| `Vehicle_Age` | Vehicle age category |
| `Vehicle_Damage` | Vehicle previously damaged (Yes/No) |
| `Annual_Premium` | Annual premium amount |
| `Policy_Sales_Channel` | Policy sales channel code |
| `Vintage` | Days with the company |

---

## 🔬 Machine Learning Workflow

1. **Preprocessing**
   - Label encoding (Gender, Vehicle_Age, Vehicle_Damage)
   - Standard scaling (Age, Annual_Premium, Vintage)
   - Train-test split (80:20)

2. **Models Trained**
   - **Logistic Regression** — Baseline model
   - **Random Forest** — With RandomizedSearchCV hyperparameter tuning
   - **XGBoost** — Selected for production deployment

3. **Evaluation Metrics**
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC-AUC

### Model Performance

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 0.8774 | 0.0000 | 0.0000 | 0.0000 | 0.8225 |
| Random Forest | 0.8695 | 0.3754 | 0.0974 | 0.1547 | 0.8396 |
| **XGBoost** | **0.8765** | **0.4370** | **0.0278** | **0.0523** | **0.8556** |

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **Frontend** | Streamlit |
| **Backend** | Python 3.10+ |
| **Data Processing** | Pandas, NumPy |
| **NoSQL** | PyMongo, MongoMock |
| **Machine Learning** | Scikit-learn, XGBoost |
| **Visualization** | Matplotlib, Seaborn, Plotly |
| **Model Serialization** | Joblib |
| **Deployment** | Streamlit Cloud / Render / Railway |

---

## 📁 Project Structure

```
Insurance Cross-Sell Analytics/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore file
│
├── src/                            # Source code
│   ├── __init__.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py               # Paths, parameters, settings
│   │
│   ├── constants/
│   │   ├── __init__.py
│   │   └── constants.py            # Display strings, page content
│   │
│   ├── logger/
│   │   ├── __init__.py
│   │   └── logger.py               # Logging configuration
│   │
│   ├── exception/
│   │   ├── __init__.py
│   │   └── exception.py            # Custom exception handling
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── data_loader.py          # Load artifacts (cached)
│   │   ├── preprocessing.py        # Input preprocessing
│   │   └── prediction.py           # Inference functions
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── prediction_pipeline.py  # End-to-end prediction pipeline
│   │
│   ├── app_utils/
│   │   ├── __init__.py
│   │   ├── ui_helpers.py           # Reusable UI components
│   │   ├── input_form.py           # Prediction input form
│   │   └── prediction_history.py   # In-memory history manager
│   │
│   └── pages/
│       ├── __init__.py
│       ├── home_page.py            # Home / Overview
│       ├── prediction_page.py      # Prediction form + history
│       ├── model_info_page.py      # Model details & comparison
│       ├── data_insights_page.py   # Data exploration
│       ├── visualizations_page.py  # Saved plots display
│       ├── metrics_page.py         # Evaluation metrics
│       ├── about_page.py           # Project information
│       └── download_center_page.py # Download artifacts
│
├── artifacts/                      # Pre-generated artifacts (from notebook)
│   ├── raw_data/
│   │   └── train.csv
│   ├── preprocessed_data/
│   │   ├── insurance_processed.csv
│   │   └── insurance_initial_ml_copy.csv
│   ├── encoders/
│   │   └── encoders.joblib
│   ├── scalers/
│   │   └── scaler.joblib
│   ├── models/
│   │   ├── xgboost_model.joblib
│   │   └── logistic_regression_model.joblib
│   ├── metrics/
│   │   └── evaluation_results.csv
│   └── plots/
│       └── matplotlib/
│           ├── random_forest_confusion_matrix.png
│           └── random_forest_feature_importance.png
│
├── Notebooks/                      # Jupyter notebooks (source of truth)
│   └── Copy of Healthcare NoSQL Analytics Markdown Done.ipynb  # Analysis notebook (rename pending)
│
└── logs/                           # Application logs (auto-generated)
```

---

## 🔧 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/GouravGC/Insurance-Cross-Sell-NoSQL-Analytics.git
cd Insurance-Cross-Sell-NoSQL-Analytics

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 5. Run the application
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 🎯 Usage

Navigate through the application using the **sidebar menu**:

| Page | Description |
|---|---|
| **🏠 Home** | Project overview and key metrics |
| **🎯 Prediction** | Enter customer details and get real-time predictions |
| **📊 Model Info** | XGBoost details, model comparison, feature importance |
| **📈 Data Insights** | Explore the raw dataset, distributions, statistics |
| **📉 Visualizations** | View saved model plots (confusion matrix, etc.) |
| **📋 Metrics** | Detailed evaluation metrics for all models |
| **ℹ️ About** | Project background, workflow, tech stack |
| **⬇️ Download Center** | Download all artifacts (data, models, plots) |

---

## 🌐 Deployment

### Streamlit Community Cloud (Recommended)

1. Push the repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository, branch, and set **Main file path** to `app.py`
5. Click "Deploy"

### Render

1. Create a new **Web Service** on Render
2. Connect your GitHub repository
3. Set:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT`

### Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Add a start command:
   ```
   streamlit run app.py --server.port $PORT --server.address 0.0.0.0
   ```

> **Note:** All artifacts are pre-generated — no retraining or recomputation is required for deployment.

---

## 📸 Screenshots

<!-- Add screenshots here -->
<p align="center">
  <em>Screenshots coming soon</em>
</p>

<!-- 
| Home Page | Prediction Page |
|---|---|
| ![Home](screenshots/home.png) | ![Prediction](screenshots/prediction.png) |

| Model Info | Metrics |
|---|---|
| ![Model Info](screenshots/model_info.png) | ![Metrics](screenshots/metrics.png) |
-->

---

## 🔗 Links

- **📂 GitHub Repository:** [https://github.com/GouravGC/Insurance-Cross-Sell-NoSQL-Analytics](https://github.com/GouravGC/Insurance-Cross-Sell-NoSQL-Analytics)
- **🌐 Live Demo:** [https://insurance-cross-sell-nosql-analytics.streamlit.app/](https://insurance-cross-sell-nosql-analytics.streamlit.app/) (Live Demo Note: The Streamlit Community Cloud app may be asleep due to inactivity. If prompted, click “Yes, get this app back up!” and wait a few seconds for the app to load.)

---

## 👤 Author

**Gourav Chhatwani**  
Aspiring Data Scientist And AI Engineer

- **GitHub:** [@GouravGC](https://github.com/GouravGC)
- **LinkedIn:** [Gourav Chhatwani](https://www.linkedin.com/in/gourav-chhatwani-9a301134a/)

---

<p align="center">
  Built with ❤️ using Streamlit<br>
  <sub>Insurance Cross-Sell NoSQL Analytics Portfolio Project</sub>
</p>
