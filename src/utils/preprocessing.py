"""
Input preprocessing for prediction.
Applies the exact same transformations as the notebook:
- Label encoding for Gender, Vehicle_Age, Vehicle_Damage
- Standard scaling for Age, Annual_Premium, Vintage
"""
import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple

from src.config.config import ALL_FEATURE_COLUMNS
from src.exception.exception import AppException, handle_exception
from src.logger.logger import get_logger

logger = get_logger(__name__)


def preprocess_input(
    input_dict: Dict[str, Any],
    encoders: Dict[str, Any],
    scaler: Any,
) -> np.ndarray:
    """
    Transform raw user input into the feature vector expected by the model.

    Parameters
    ----------
    input_dict : dict
        Raw user-provided values. Keys must match the config columns.
    encoders : dict
        Dictionary of LabelEncoder objects loaded from artifacts.
    scaler : StandardScaler
        Fitted scaler loaded from artifacts.

    Returns
    -------
    np.ndarray
        (1, n_features) array ready for model prediction.
    """
    try:
        # Build a DataFrame from the input
        df = pd.DataFrame([input_dict])

        # Ensure all required columns exist
        for col in ALL_FEATURE_COLUMNS:
            if col not in df.columns:
                raise ValueError(f"Missing required feature: {col}")

        # Reorder columns to match training order
        df = df[ALL_FEATURE_COLUMNS].copy()

        # ---- Label Encoding ----
        for col in ["Gender", "Vehicle_Age", "Vehicle_Damage"]:
            encoder = encoders.get(col)
            if encoder is None:
                raise ValueError(f"Encoder for column '{col}' not found.")
            # If the encoder has never seen this category, fallback to 0
            try:
                df[col] = encoder.transform(df[col].astype(str))
            except ValueError:
                logger.warning(
                    "Unknown category in '%s': %s. Falling back to 0.",
                    col, df[col].iloc[0]
                )
                df[col] = 0

        # ---- Scaling ----
        scale_cols = ["Age", "Annual_Premium", "Vintage"]
        try:
            df[scale_cols] = scaler.transform(df[scale_cols])
        except Exception as e:
            logger.error("Scaling failed: %s", e)
            raise AppException("Error during feature scaling.", error=e)

        # ---- Ensure dtypes ----
        df = df.astype(np.float64)

        logger.debug("Preprocessed input shape: %s", df.shape)
        return df.values

    except Exception as e:
        handle_exception(e, "preprocess_input")
        raise AppException("Failed to preprocess input data.", error=e)

