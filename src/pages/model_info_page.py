"""
Model Information page — details about XGBoost, its parameters,
feature importance, and comparison with other models.
"""
import streamlit as st
import pandas as pd

from src.constants.constants import MODEL_INFO_HEADING
from src.utils.data_loader import load_metrics, get_plot_files
from src.app_utils.ui_helpers import render_metric_cards


def show_model_info():
    """Render the Model Information page."""
    st.title(f"📊 {MODEL_INFO_HEADING}")
    st.divider()

    # ---------- Deployed Model ----------
    st.markdown("## 🚀 Deployed Model: XGBoost")
    st.markdown(
        """
        **XGBoost** (eXtreme Gradient Boosting) is selected as the production model
        because it offers the best balance of performance, speed, and model size.

        | Criteria | XGBoost | Why |
        |---|---|---|
        | **ROC-AUC** | 0.8556 | Best discriminatory power |
        | **Model Size** | ~2 MB | Lightweight for deployment |
        | **Inference Speed** | Fast | Suitable for real-time predictions |
        | **Precision** | 0.4370 | Better than Logistic Regression |
        """
    )

    st.divider()

    # ---------- Model Comparison ----------
    st.markdown("## ⚖️ Model Comparison")
    try:
        metrics_df = load_metrics()
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
    except Exception:
        st.info("Metrics file not available. Run the notebook first.")

    st.divider()

    # ---------- Why not Random Forest? ----------
    st.markdown("## ❌ Why Random Forest is Not Deployed")
    st.warning(
        """
        **Random Forest** was excluded from deployment due to:
        - **Large model file size** (> 100 MB), making it unsuitable for
          lightweight deployment platforms (Streamlit Cloud, Render, Railway).
        - **Lower ROC-AUC** (0.8396) compared to XGBoost (0.8556).
        - **Slower inference** due to ensemble size.

        The Random Forest model exists **only for comparison** inside the notebook.
        """
    )

    st.divider()

    # ---------- XGBoost Parameters ----------
    st.markdown("## ⚙️ XGBoost Parameters (from notebook)")
    params_df = pd.DataFrame(
        {
            "Parameter": [
                "n_estimators",
                "max_depth",
                "learning_rate",
                "subsample",
                "colsample_bytree",
                "objective",
                "eval_metric",
                "random_state",
            ],
            "Value": [
                "100 (default)",
                "6 (default)",
                "0.3 (default)",
                "1.0 (default)",
                "1.0 (default)",
                "binary:logistic",
                "logloss",
                "42",
            ],
        }
    )
    st.dataframe(params_df, use_container_width=True, hide_index=True)

    st.divider()

    # ---------- Metrics for XGBoost ----------
    st.markdown("## 📈 XGBoost Performance Metrics")
    try:
        render_metric_cards(metrics_df, "XGBoost")
    except Exception:
        pass

    # ---------- Feature Importance ----------
    st.markdown("## 🔍 Feature Importance (Random Forest)")
    st.markdown(
        """
        *Feature importance plot from the Random Forest model is displayed below.
        XGBoost feature importance follows a similar pattern.*
        """
    )
    plots = get_plot_files()
    importance_key = "Random Forest Feature Importance"
    if importance_key in plots:
        st.image(plots[importance_key], use_column_width=True)
    else:
        st.info(
            "Feature importance plot not found. "
            "Ensure the notebook has been executed."
        )

