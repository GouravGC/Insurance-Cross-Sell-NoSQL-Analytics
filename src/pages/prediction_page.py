"""
Prediction page — input form, run inference, display results,
show prediction history, and provide CSV/JSON download.
"""
import streamlit as st
import pandas as pd
import json
from io import BytesIO, StringIO

from src.constants.constants import PREDICTION_HEADING, PREDICTION_DESCRIPTION
from src.app_utils.input_form import render_prediction_form
from src.app_utils.prediction_history import PredictionHistory
from src.app_utils.ui_helpers import display_prediction_result
from src.pipeline.prediction_pipeline import PredictionPipeline
from src.exception.exception import AppException


def show_prediction():
    """Render the prediction page."""
    st.title(f"🎯 {PREDICTION_HEADING}")
    st.markdown(PREDICTION_DESCRIPTION)
    st.divider()

    # Initialize prediction history
    PredictionHistory.initialize()

    # Initialize pipeline
    try:
        pipeline = PredictionPipeline()
    except AppException as e:
        st.error(
            f"⚠️ **Prediction service unavailable.**\n\n{e.message}\n\n"
            "Please ensure the notebook has been executed to generate artifacts."
        )
        return
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred while loading the model: {e}")
        return

    # ---------- Tabs ----------
    tab_predict, tab_history = st.tabs(["Make Prediction", "Prediction History"])

    # ---- TAB 1: Make Prediction ----
    with tab_predict:
        input_data = render_prediction_form()

        if input_data is not None:
            with st.spinner("Running prediction..."):
                try:
                    pred, prob_0, prob_1 = pipeline.run(input_data)

                    # Display result
                    st.divider()
                    st.markdown("### 📊 Prediction Result")
                    display_prediction_result(pred, prob_0, prob_1)

                    # Store in history
                    record = {
                        **input_data,
                        "Prediction": int(pred),
                        "Probability_0": round(prob_0, 4),
                        "Probability_1": round(prob_1, 4),
                    }
                    PredictionHistory.add_record(record)

                except AppException as e:
                    st.error(f"❌ Prediction failed: {e.message}")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")

    # ---- TAB 2: Prediction History ----
    with tab_history:
        st.markdown("### 📜 Prediction History")
        history_df = PredictionHistory.to_dataframe()

        if history_df.empty:
            st.info("No predictions made yet. Go to **Make Prediction** tab to start.")
        else:
            st.dataframe(history_df, use_container_width=True, hide_index=True)

            st.markdown(f"**Total predictions: {PredictionHistory.count()}**")

            # Download buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                # CSV download
                csv_buffer = StringIO()
                history_df.to_csv(csv_buffer, index=False)
                st.download_button(
                    label="📥 Download as CSV",
                    data=csv_buffer.getvalue(),
                    file_name="prediction_history.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
            with col2:
                # JSON download
                json_buffer = StringIO()
                json.dump(
                    json.loads(history_df.to_json(orient="records")),
                    json_buffer,
                    indent=2,
                )
                st.download_button(
                    label="📥 Download as JSON",
                    data=json_buffer.getvalue(),
                    file_name="prediction_history.json",
                    mime="application/json",
                    use_container_width=True,
                )
            with col3:
                if st.button("🗑️ Clear History", use_container_width=True):
                    PredictionHistory.clear()
                    st.rerun()

