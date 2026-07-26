"""
Download Center — download all artifacts, reports, and data files.
"""
import streamlit as st
import pandas as pd
from pathlib import Path

from src.constants.constants import DOWNLOAD_HEADING
from src.config.config import (
    METRICS_FILE,
    RAW_DATA_FILE,
    PREPROCESSED_DATA_FILE,
    INITIAL_ML_DATA_FILE,
    MODELS_DIR,
    ENCODERS_FILE,
    SCALER_FILE,
    MATPLOTLIB_PLOTS_DIR,
    ARTIFACTS_DIR,
)


def show_download_center():
    """Render the Download Center page."""
    st.title(f"⬇️ {DOWNLOAD_HEADING}")
    st.divider()

    st.markdown(
        """
        Download all project artifacts — data files, metrics, models,
        preprocessing artifacts, and plots. All files are loaded from
        the saved artifacts directory.
        """
    )

    # ---- Data Files ----
    st.markdown("## 📁 Data Files")
    data_files = {
        "Raw Data (train.csv)": RAW_DATA_FILE,
        "Processed Data (insurance_processed.csv)": PREPROCESSED_DATA_FILE,
        "Initial ML Copy (insurance_initial_ml_copy.csv)": INITIAL_ML_DATA_FILE,
    }
    for label, path in data_files.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{label}**")
            st.caption(f"Path: `{path.relative_to(ARTIFACTS_DIR.parent)}`")
        with col2:
            if path.exists():
                with open(path, "rb") as f:
                    st.download_button(
                        label="📥 Download",
                        data=f,
                        file_name=path.name,
                        mime="text/csv",
                        use_container_width=True,
                    )
            else:
                st.button("❌ Not Found", disabled=True, use_container_width=True)

    st.divider()

    # ---- Metrics ----
    st.markdown("## 📊 Metrics")
    if METRICS_FILE.exists():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**Evaluation Results**")
            st.caption(f"Path: `{METRICS_FILE.relative_to(ARTIFACTS_DIR.parent)}`")
        with col2:
            with open(METRICS_FILE, "rb") as f:
                st.download_button(
                    label="📥 Download",
                    data=f,
                    file_name=METRICS_FILE.name,
                    mime="text/csv",
                    use_container_width=True,
                )
    else:
        st.warning("Metrics file not found.")

    st.divider()

    # ---- Models ----
    st.markdown("## 🤖 Models")
    model_files = list(MODELS_DIR.glob("*.joblib"))
    if model_files:
        for model_path in model_files:
            col1, col2 = st.columns([3, 1])
            with col1:
                size_kb = model_path.stat().st_size / 1024
                st.markdown(
                    f"**{model_path.name}** ({size_kb:.1f} KB)"
                )
                st.caption(
                    f"Path: `{model_path.relative_to(ARTIFACTS_DIR.parent)}`"
                )
            with col2:
                with open(model_path, "rb") as f:
                    st.download_button(
                        label="📥 Download",
                        data=f,
                        file_name=model_path.name,
                        mime="application/octet-stream",
                        use_container_width=True,
                    )
    else:
        st.warning("No model files found.")

    st.divider()

    # ---- Preprocessing Artifacts ----
    st.markdown("## 🔧 Preprocessing Artifacts")
    preproc_files = {
        "Encoders (encoders.joblib)": ENCODERS_FILE,
        "Scaler (scaler.joblib)": SCALER_FILE,
    }
    for label, path in preproc_files.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            size_kb = path.stat().st_size / 1024 if path.exists() else 0
            st.markdown(f"**{label}** ({size_kb:.1f} KB)")
            st.caption(f"Path: `{path.relative_to(ARTIFACTS_DIR.parent)}`")
        with col2:
            if path.exists():
                with open(path, "rb") as f:
                    st.download_button(
                        label="📥 Download",
                        data=f,
                        file_name=path.name,
                        mime="application/octet-stream",
                        use_container_width=True,
                    )
            else:
                st.button("❌ Not Found", disabled=True, use_container_width=True)

    st.divider()

    # ---- Plots ----
    st.markdown("## 🖼️ Plots")
    plot_files = list(MATPLOTLIB_PLOTS_DIR.glob("*.png"))
    if plot_files:
        for plot_path in plot_files:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{plot_path.stem.replace('_', ' ').title()}**")
                st.caption(
                    f"Path: `{plot_path.relative_to(ARTIFACTS_DIR.parent)}`"
                )
            with col2:
                with open(plot_path, "rb") as f:
                    st.download_button(
                        label="📥 Download",
                        data=f,
                        file_name=plot_path.name,
                        mime="image/png",
                        use_container_width=True,
                    )
    else:
        st.info("No plot files found.")

