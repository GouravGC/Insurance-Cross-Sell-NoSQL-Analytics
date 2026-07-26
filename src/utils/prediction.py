"""
Prediction utilities: single prediction and probability.
"""
import numpy as np
from typing import Dict, Any, Tuple

from src.utils.preprocessing import preprocess_input
from src.exception.exception import AppException, handle_exception
from src.logger.logger import get_logger

logger = get_logger(__name__)


def predict(
    input_dict: Dict[str, Any],
    encoders: Dict[str, Any],
    scaler: Any,
    model: Any,
) -> int:
    """
    Return the binary prediction (0 or 1).
    """
    try:
        features = preprocess_input(input_dict, encoders, scaler)
        pred = model.predict(features)
        return int(pred[0])
    except Exception as e:
        handle_exception(e, "predict")
        raise AppException("Prediction failed.", error=e)


def predict_proba(
    input_dict: Dict[str, Any],
    encoders: Dict[str, Any],
    scaler: Any,
    model: Any,
) -> Tuple[float, float]:
    """
    Return (probability_class_0, probability_class_1).
    """
    try:
        features = preprocess_input(input_dict, encoders, scaler)
        proba = model.predict_proba(features)[0]
        return float(proba[0]), float(proba[1])
    except Exception as e:
        handle_exception(e, "predict_proba")
        raise AppException("Probability prediction failed.", error=e)

