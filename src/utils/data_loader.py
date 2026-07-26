"""
Utility functions to load all saved artifacts, data, and metrics.
All artifacts are loaded from the filesystem; nothing is recomputed.
"""
import pandas as pd
import joblib
import streamlit as st
from pathlib import Path

from src.config.config import (
    XGBOOST_MODEL_FILE,
    ENCODERS_FILE,
    SCALER_FILE,
    METRICS_FILE,
    RAW_DATA_FILE,
    PREPROCESSED_DATA_FILE,
    INITIAL_ML_DATA_FILE,
    ALL_FEATURE_COLUMNS,
    RF_CONFUSION_MATRIX,
    RF_FEATURE_IMPORTANCE,
    MATPLOTLIB_PLOTS_DIR,
)
from src.exception.exception import AppException, handle_exception
from src.logger.logger import get_logger

logger = get_logger(__name__)


@st.cache_resource
def load_model():
    """Load the deployed XGBoost model. Cached for performance."""
    try:
        logger.info("Loading XGBoost model from %s", XGBOOST_MODEL_FILE)
        model = joblib.load(XGBOOST_MODEL_FILE)
        logger.info("Model loaded successfully.")
        return model
    except FileNotFoundError:
        raise AppException(
            f"XGBoost model not found at {XGBOOST_MODEL_FILE}. "
            "Ensure the notebook has been executed to generate artifacts."
        )
    except Exception as e:
        handle_exception(e, "load_model")
        raise AppException("Failed to load XGBoost model.", error=e)


@st.cache_resource
def load_encoders():
    """Load the saved label encoders."""
    try:
        logger.info("Loading encoders from %s", ENCODERS_FILE)
        encoders = joblib.load(ENCODERS_FILE)
        logger.info("Encoders loaded successfully.")
        return encoders
    except FileNotFoundError:
        raise AppException(
            f"Encoders not found at {ENCODERS_FILE}. "
            "Ensure the notebook has been executed."
        )
    except Exception as e:
        handle_exception(e, "load_encoders")
        raise AppException("Failed to load encoders.", error=e)


@st.cache_resource
def load_scaler():
    """Load the saved StandardScaler."""
    try:
        logger.info("Loading scaler from %s", SCALER_FILE)
        scaler = joblib.load(SCALER_FILE)
        logger.info("Scaler loaded successfully.")
        return scaler
    except FileNotFoundError:
        raise AppException(
            f"Scaler not found at {SCALER_FILE}. "
            "Ensure the notebook has been executed."
        )
    except Exception as e:
        handle_exception(e, "load_scaler")
        raise AppException("Failed to load scaler.", error=e)


@st.cache_resource
def load_artifacts():
    """Load all artifacts at once, returning a dictionary."""
    logger.info("Loading all artifacts ...")
    model = load_model()
    encoders = load_encoders()
    scaler = load_scaler()
    logger.info("All artifacts loaded successfully.")
    return {
        "model": model,
        "encoders": encoders,
        "scaler": scaler,
    }


@st.cache_data
def load_raw_data(nrows: int = None) -> pd.DataFrame:
    """Load the raw training data."""
    try:
        logger.info("Loading raw data from %s", RAW_DATA_FILE)
        df = pd.read_csv(RAW_DATA_FILE, nrows=nrows)
        logger.info("Raw data loaded: %d rows, %d columns", df.shape[0], df.shape[1])
        return df
    except FileNotFoundError:
        raise AppException(
            f"Raw data file not found at {RAW_DATA_FILE}."
        )
    except Exception as e:
        handle_exception(e, "load_raw_data")
        raise AppException("Failed to load raw data.", error=e)


@st.cache_data
def load_preprocessed_data(nrows: int = None) -> pd.DataFrame:
    """Load the preprocessed (encoded + scaled) data."""
    try:
        logger.info("Loading preprocessed data from %s", PREPROCESSED_DATA_FILE)
        df = pd.read_csv(PREPROCESSED_DATA_FILE, nrows=nrows)
        logger.info("Preprocessed data loaded: %d rows, %d columns", df.shape[0], df.shape[1])
        return df
    except FileNotFoundError:
        raise AppException(
            f"Preprocessed data file not found at {PREPROCESSED_DATA_FILE}."
        )
    except Exception as e:
        handle_exception(e, "load_preprocessed_data")
        raise AppException("Failed to load preprocessed data.", error=e)


@st.cache_data
def load_metrics() -> pd.DataFrame:
    """Load the evaluation metrics CSV."""
    try:
        logger.info("Loading metrics from %s", METRICS_FILE)
        df = pd.read_csv(METRICS_FILE)
        logger.info("Metrics loaded: %s", df.to_dict(orient="records"))
        return df
    except FileNotFoundError:
        raise AppException(
            f"Metrics file not found at {METRICS_FILE}."
        )
    except Exception as e:
        handle_exception(e, "load_metrics")
        raise AppException("Failed to load metrics.", error=e)


def get_plot_files() -> dict:
    """Return a dict of available plot file paths."""
    plots = {}
    try:
        for png_file in MATPLOTLIB_PLOTS_DIR.glob("*.png"):
            plots[png_file.stem.replace("_", " ").title()] = str(png_file)
    except Exception:
        pass
    return plots

