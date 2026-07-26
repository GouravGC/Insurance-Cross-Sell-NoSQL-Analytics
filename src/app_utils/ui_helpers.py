"""
Reusable UI helper functions for Streamlit pages.
"""
import streamlit as st
import pandas as pd
from typing import Optional, List, Dict, Any

from src.constants.constants import PAGES, FOOTER_TEXT, PAGE_ABOUT

# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
def render_sidebar():
    """Render the sidebar navigation."""
    with st.sidebar:
        st.image(
            "https://img.icons8.com/fluency/96/health-insurance.png",
            width=80,
        )
        st.markdown("### Healthcare NoSQL")
        st.markdown("**Analytics Dashboard**")
        st.divider()

        selected = st.radio("Navigation", PAGES, label_visibility="collapsed")
        st.divider()

        # Quick stats in sidebar
        st.markdown("#### ⚡ Quick Info")
        st.caption("• Deployed Model: XGBoost")
        st.caption("• Dataset: 381,109 records")
        st.caption("• Features: 10")
        st.caption("• Target: Response (0/1)")

        st.divider()
        st.caption("v1.0.0")
        return selected


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
def render_footer():
    """Render a consistent footer."""
    st.divider()
    st.caption(FOOTER_TEXT)


# ---------------------------------------------------------------------------
# Metric Cards
# ---------------------------------------------------------------------------
def render_metric_cards(metrics_df: pd.DataFrame, model_name: str = "XGBoost"):
    """Display metric cards for a given model from the evaluation CSV."""
    row = metrics_df[metrics_df["Model"] == model_name]
    if row.empty:
        st.warning(f"No metrics found for model: {model_name}")
        return

    row = row.iloc[0]
    cols = st.columns(5)
    metrics_display = [
        ("Accuracy", f"{row['Accuracy']:.4f}"),
        ("Precision", f"{row['Precision']:.4f}"),
        ("Recall", f"{row['Recall']:.4f}"),
        ("F1 Score", f"{row['F1']:.4f}"),
        ("ROC-AUC", f"{row['ROC_AUC']:.4f}"),
    ]
    for col, (label, value) in zip(cols, metrics_display):
        with col:
            st.metric(label=label, value=value, delta=None)


# ---------------------------------------------------------------------------
# Prediction Result Display
# ---------------------------------------------------------------------------
def display_prediction_result(
    prediction: int,
    probability_0: float,
    probability_1: float,
):
    """Display the prediction outcome with confidence indicators."""
    col1, col2 = st.columns(2)

    with col1:
        if prediction == 1:
            st.success("## ✅ Interested")
            st.markdown(
                "This customer is **likely interested** in vehicle insurance."
            )
        else:
            st.info("## ❌ Not Interested")
            st.markdown(
                "This customer is **unlikely interested** in vehicle insurance."
            )

    with col2:
        st.metric(
            label="Confidence (Positive Class)",
            value=f"{probability_1:.2%}",
        )
        st.metric(
            label="Confidence (Negative Class)",
            value=f"{probability_0:.2%}",
        )

    # Confidence bar
    st.markdown("#### Confidence Breakdown")
    proba_df = pd.DataFrame(
        {
            "Class": ["Not Interested (0)", "Interested (1)"],
            "Probability": [probability_0, probability_1],
        }
    )
    st.bar_chart(proba_df.set_index("Class"), horizontal=True)


# ---------------------------------------------------------------------------
# Loading Spinner
# ---------------------------------------------------------------------------
def show_loading_spinner(message: str = "Loading ..."):
    """Context manager for a loading spinner."""
    return st.spinner(message)

