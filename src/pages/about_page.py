"""
About page — project overview, business problem, dataset, workflow, and tech stack.
"""
import streamlit as st

from src.constants.constants import (
    ABOUT_PROJECT_OVERVIEW,
    ABOUT_BUSINESS_PROBLEM,
    ABOUT_DATASET_DESCRIPTION,
    ABOUT_ML_WORKFLOW,
    ABOUT_TECH_STACK,
)


def show_about():
    """Render the About page."""
    st.title("ℹ️ About This Project")
    st.divider()

    # ---- Project Overview ----
    with st.container():
        st.markdown("## 📋 Project Overview")
        st.markdown(ABOUT_PROJECT_OVERVIEW)
        st.divider()

    # ---- Business Problem ----
    with st.container():
        st.markdown("## 💼 Business Problem")
        st.markdown(ABOUT_BUSINESS_PROBLEM)
        st.divider()

    # ---- Dataset ----
    with st.container():
        st.markdown("## 📦 Dataset Description")
        st.markdown(ABOUT_DATASET_DESCRIPTION)
        st.divider()

    # ---- ML Workflow ----
    with st.container():
        st.markdown("## 🔬 Machine Learning Workflow")
        st.markdown(ABOUT_ML_WORKFLOW)
        st.divider()

    # ---- Tech Stack ----
    with st.container():
        st.markdown("## 🛠️ Technologies Used")
        st.markdown(ABOUT_TECH_STACK)
        st.divider()

    # ---- Links ----
    with st.container():
        st.markdown("## 🔗 Links & Resources")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info(
                "**📂 GitHub Repository**\n\n"
                "[View on GitHub](https://github.com/yourusername/"
                "insurance-cross-sell-analytics) *(placeholder)*"
            )
        with col2:
            st.info(
                "**🌐 Live Demo**\n\n"
                "[View Live App](https://your-demo-url.streamlit.app) "
                "*(placeholder)*"
            )
        with col3:
            st.info(
                "**📄 Project Report**\n\n"
                "See the Jupyter Notebook for the full analysis."
            )
        st.divider()

    # ---- Author ----
    with st.container():
        st.markdown("## 👤 Author")
        st.markdown(
            """
            **Gurucharan S**  
            Data Scientist | Machine Learning Engineer

            This project is part of a portfolio demonstrating end-to-end
            machine learning capabilities, from data exploration and NoSQL
            operations to model deployment with an interactive web application.
            """
        )

