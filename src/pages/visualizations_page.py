"""
Visualizations page — display saved plots from the notebook.
No plots are regenerated; only pre-saved images are shown.
"""
import streamlit as st
from pathlib import Path

from src.constants.constants import VIZ_HEADING
from src.utils.data_loader import get_plot_files
from src.config.config import RF_CONFUSION_MATRIX, RF_FEATURE_IMPORTANCE


def show_visualizations():
    """Render the Visualizations page."""
    st.title(f"📉 {VIZ_HEADING}")
    st.divider()

    st.markdown(
        """
        This page displays plots that were generated during model training.
        All visualizations are pre-saved artifacts — no recomputation occurs.
        """
    )

    plots = get_plot_files()

    if not plots:
        st.warning(
            "No plot files found in the artifacts directory. "
            "Ensure the notebook has been executed to generate plots."
        )
        return

    # Display each plot
    for plot_name, plot_path in plots.items():
        st.markdown(f"### 🖼️ {plot_name}")
        try:
            st.image(plot_path, use_column_width=True)
        except Exception as e:
            st.error(f"Could not load plot '{plot_name}': {e}")
        st.divider()

    # If specific known plots are missing, provide context
    if "Random Forest Confusion Matrix" not in plots:
        st.info(
            "ℹ️ **Random Forest Confusion Matrix** is not available. "
            "This plot is generated during Random Forest training in the notebook."
        )
    if "Random Forest Feature Importance" not in plots:
        st.info(
            "ℹ️ **Random Forest Feature Importance** is not available. "
            "This plot is generated during Random Forest training in the notebook."
        )

    st.markdown(
        """
        ---
        **Note:** These plots were generated using **Matplotlib** during the
        notebook execution. The Random Forest model was chosen for visualization
        due to its interpretability. XGBoost feature importance follows a
        similar distribution.
        """
    )

