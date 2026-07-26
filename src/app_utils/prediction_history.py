"""
In-memory prediction history manager using Streamlit's session state.
"""
import pandas as pd
import streamlit as st
from typing import Dict, Any, Optional, List

from src.config.config import MAX_PREDICTION_HISTORY


class PredictionHistory:
    """Manage prediction history in session state."""

    @staticmethod
    def initialize():
        """Ensure the history list exists in session state."""
        if "prediction_history" not in st.session_state:
            st.session_state["prediction_history"] = []

    @staticmethod
    def add_record(record: Dict[str, Any]):
        """Append a record (input + prediction + probability) to history."""
        st.session_state["prediction_history"].append(record)
        # Trim to max size (FIFO)
        if len(st.session_state["prediction_history"]) > MAX_PREDICTION_HISTORY:
            st.session_state["prediction_history"].pop(0)

    @staticmethod
    def get_history() -> List[Dict[str, Any]]:
        """Return the full history list."""
        return st.session_state.get("prediction_history", [])

    @staticmethod
    def clear():
        """Clear the prediction history."""
        st.session_state["prediction_history"] = []

    @staticmethod
    def to_dataframe() -> pd.DataFrame:
        """Convert history to a pandas DataFrame for download."""
        records = PredictionHistory.get_history()
        if not records:
            return pd.DataFrame()
        return pd.DataFrame(records)

    @staticmethod
    def count() -> int:
        """Return the number of predictions made."""
        return len(PredictionHistory.get_history())

