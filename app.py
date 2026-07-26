"""
Main entry point for the Healthcare NoSQL Analytics Streamlit application.

Usage:
    streamlit run app.py
"""
import streamlit as st

from src.config.config import APP_TITLE, APP_ICON, APP_LAYOUT, SIDEBAR_STATE
from src.constants.constants import (
    PAGE_HOME,
    PAGE_PREDICTION,
    PAGE_MODEL_INFO,
    PAGE_DATA_INSIGHTS,
    PAGE_VISUALIZATIONS,
    PAGE_METRICS,
    PAGE_ABOUT,
    PAGE_DOWNLOAD,
)
from src.app_utils.ui_helpers import render_sidebar, render_footer
from src.app_utils.prediction_history import PredictionHistory
from src.logger.logger import setup_logger

# ---------------------------------------------------------------------------
# Page Configuration (must be the first Streamlit command)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=APP_LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE,
)

# ---------------------------------------------------------------------------
# Logger
# ---------------------------------------------------------------------------
logger = setup_logger("app")
logger.info("Application started.")


# ---------------------------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------------------------
def init_session_state():
    """Initialize all required session state variables."""
    PredictionHistory.initialize()


# ---------------------------------------------------------------------------
# Main Application
# ---------------------------------------------------------------------------
def main():
    """Render the multi-page Streamlit application."""

    # Initialize state
    init_session_state()

    # Sidebar navigation
    selected_page = render_sidebar()

    # Main content area
    st.markdown(
        f"""
        <style>
        .block-container {{padding-top: 2rem; padding-bottom: 2rem;}}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Route to the selected page
    if selected_page == PAGE_HOME:
        from src.pages.home_page import show_home
        show_home()

    elif selected_page == PAGE_PREDICTION:
        from src.pages.prediction_page import show_prediction
        show_prediction()

    elif selected_page == PAGE_MODEL_INFO:
        from src.pages.model_info_page import show_model_info
        show_model_info()

    elif selected_page == PAGE_DATA_INSIGHTS:
        from src.pages.data_insights_page import show_data_insights
        show_data_insights()

    elif selected_page == PAGE_VISUALIZATIONS:
        from src.pages.visualizations_page import show_visualizations
        show_visualizations()

    elif selected_page == PAGE_METRICS:
        from src.pages.metrics_page import show_metrics
        show_metrics()

    elif selected_page == PAGE_ABOUT:
        from src.pages.about_page import show_about
        show_about()

    elif selected_page == PAGE_DOWNLOAD:
        from src.pages.download_center_page import show_download_center
        show_download_center()

    # Footer
    render_footer()

    logger.info("Page rendered: %s", selected_page)


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()

