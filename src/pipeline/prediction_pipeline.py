"""
Prediction pipeline — orchestrates model loading, preprocessing, and prediction.
Uses cached artifacts for performance.
"""
from typing import Dict, Any, Tuple

from src.utils.data_loader import load_artifacts
from src.utils.prediction import predict, predict_proba
from src.exception.exception import AppException, handle_exception
from src.logger.logger import get_logger

logger = get_logger(__name__)


class PredictionPipeline:
    """End-to-end prediction pipeline."""

    def __init__(self):
        self.artifacts = None
        self._load_artifacts()

    def _load_artifacts(self):
        """Load and cache all artifacts."""
        try:
            self.artifacts = load_artifacts()
        except Exception as e:
            handle_exception(e, "PredictionPipeline._load_artifacts")
            raise AppException(
                "Failed to initialize prediction pipeline. "
                "Ensure all artifacts exist.",
                error=e,
            )

    def run(self, input_dict: Dict[str, Any]) -> Tuple[int, float, float]:
        """
        Run the full pipeline: preprocess → predict → return results.

        Returns
        -------
        (prediction, probability_0, probability_1)
        """
        try:
            model = self.artifacts["model"]
            encoders = self.artifacts["encoders"]
            scaler = self.artifacts["scaler"]

            pred = predict(input_dict, encoders, scaler, model)
            prob_0, prob_1 = predict_proba(input_dict, encoders, scaler, model)

            logger.info(
                "Prediction: %d | Prob(0): %.4f | Prob(1): %.4f",
                pred, prob_0, prob_1,
            )
            return pred, prob_0, prob_1

        except Exception as e:
            handle_exception(e, "PredictionPipeline.run")
            raise AppException("Prediction pipeline failed.", error=e)

