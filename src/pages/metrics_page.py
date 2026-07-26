"""
Metrics page — display model evaluation metrics from the saved CSV.
"""
import streamlit as st
import pandas as pd

from src.constants.constants import METRICS_HEADING
from src.utils.data_loader import load_metrics
from src.app_utils.ui_helpers import render_metric_cards


def show_metrics():
    """Render the Metrics page."""
    st.title(f"📋 {METRICS_HEADING}")
    st.divider()

    st.markdown(
        """
        Model evaluation metrics computed during training on the test set.
        All metrics are loaded from the saved `evaluation_results.csv` artifact.
        """
    )

    try:
        metrics_df = load_metrics()
    except Exception as e:
        st.error(f"⚠️ Could not load metrics: {e}")
        st.info("Ensure the notebook has been executed to generate metrics.")
        return

    # ---- Overview Table ----
    st.markdown("### 📊 All Models Comparison")
    st.dataframe(
        metrics_df.style.format(
            {
                "Accuracy": "{:.4f}",
                "Precision": "{:.4f}",
                "Recall": "{:.4f}",
                "F1": "{:.4f}",
                "ROC_AUC": "{:.4f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # ---- Per-Model Metrics ----
    st.markdown("### 📈 Per-Model Metrics")
    model_tabs = st.tabs(metrics_df["Model"].tolist())
    for tab, (_, row) in zip(model_tabs, metrics_df.iterrows()):
        with tab:
            model_name = row["Model"]
            st.markdown(f"**{model_name}**")

            cols = st.columns(5)
            metric_items = [
                ("Accuracy", row["Accuracy"]),
                ("Precision", row["Precision"]),
                ("Recall", row["Recall"]),
                ("F1 Score", row["F1"]),
                ("ROC-AUC", row["ROC_AUC"]),
            ]
            for col, (label, value) in zip(cols, metric_items):
                with col:
                    st.metric(label=label, value=f"{value:.4f}")

    st.divider()

    # ---- Deployed Model Highlight ----
    st.markdown("### ✅ Deployed Model: XGBoost")
    render_metric_cards(metrics_df, "XGBoost")

    st.info(
        """
        **Why XGBoost was chosen for deployment:**
        - Highest **ROC-AUC** (0.8556) — best at distinguishing classes
        - **Lightweight** model file (~2 MB) suitable for cloud deployment
        - **Fast inference** — ideal for real-time predictions
        - Despite lower Recall, the model's overall discriminative power and
          operational efficiency make it the best choice for production.
        """
    )

    st.divider()

    # ---- Metrics Discussion ----
    with st.expander("📘 Understanding the Metrics"):
        st.markdown(
            """
            **Accuracy:** Proportion of correct predictions (both positive and negative).
            Can be misleading for imbalanced datasets.

            **Precision:** Of all positive predictions, what fraction was correct.
            High precision → fewer false positives.

            **Recall:** Of all actual positives, what fraction was correctly identified.
            High recall → fewer false negatives.

            **F1 Score:** Harmonic mean of Precision and Recall.
            Good balance between the two.

            **ROC-AUC:** Area Under the Receiver Operating Characteristic curve.
            Measures the model's ability to distinguish between classes across
            all thresholds. **Best metric for imbalanced classification.**
            """
        )

