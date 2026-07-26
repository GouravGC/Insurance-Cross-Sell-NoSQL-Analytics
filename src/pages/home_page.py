"""
Home page — Project overview, key highlights, and quick links.
"""
import streamlit as st
import pandas as pd

from src.constants.constants import HOME_HEADING, HOME_SUBHEADING
from src.utils.data_loader import load_metrics
from src.app_utils.ui_helpers import render_metric_cards


def show_home():
    """Render the home page."""
    st.title(f"🏥 {HOME_HEADING}")
    st.markdown(f"**{HOME_SUBHEADING}**")
    st.divider()

    # ---------- Hero Section ----------
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Dataset Size", "381,109", "Records")
    with col2:
        st.metric("Features", "10", "Predictors")
    with col3:
        st.metric("Deployed Model", "XGBoost", "ROC-AUC: 0.8556")

    st.divider()

    # ---------- Quick Overview ----------
    st.markdown("## 🚀 Project Overview")
    st.markdown(
        """
        This application predicts whether existing health insurance customers
        are interested in purchasing **vehicle insurance** — a classic
        **cross-selling** problem.

        The project integrates:
        - **NoSQL (MongoDB) analytics** for data operations
        - **Machine Learning** (XGBoost) for prediction
        - **Streamlit** for interactive deployment

        Use the **sidebar** to navigate through different sections.
        """
    )

    st.divider()

    # ---------- Metrics preview ----------
    st.markdown("## 📊 Model Performance at a Glance")
    try:
        metrics_df = load_metrics()
        render_metric_cards(metrics_df, "XGBoost")
    except Exception:
        st.info("Metrics not available. Run the notebook first.")

    st.divider()

    # ---------- Key features ----------
    st.markdown("## ✨ Key Features")
    features_cols = st.columns(3)
    features = [
        ("🎯", "Prediction", "Real-time customer interest prediction with confidence scores."),
        ("📊", "Model Insights", "View model metrics, feature importance, and performance."),
        ("📈", "Data Visualizations", "Explore the dataset through pre-generated plots."),
        ("📋", "Metrics Dashboard", "Detailed evaluation metrics for all trained models."),
        ("⬇️", "Download Center", "Download predictions, reports, and data files."),
        ("ℹ️", "About", "Learn about the project, business problem, and tech stack."),
    ]
    for i, (emoji, title, desc) in enumerate(features):
        with features_cols[i % 3]:
            st.markdown(f"### {emoji} {title}")
            st.caption(desc)

    st.divider()
    st.info(
        "👈 **Navigate** using the sidebar to explore predictions, "
        "model details, data insights, and more."
    )

