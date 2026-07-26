"""
Prediction input form — renders input widgets and returns a dict of values.
"""
import streamlit as st
from typing import Dict, Any

from src.config.config import FEATURE_DESCRIPTIONS


def render_prediction_form() -> Dict[str, Any]:
    """
    Render the input form for making predictions.

    Returns
    -------
    dict
        Dictionary with feature names as keys and user-provided values.
    """
    with st.form("prediction_form"):
        st.markdown("### Customer Details")
        cols = st.columns(3)

        # Row 1
        with cols[0]:
            gender = st.selectbox(
                "Gender",
                options=["Male", "Female"],
                help=FEATURE_DESCRIPTIONS["Gender"],
            )

        with cols[1]:
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=35,
                step=1,
                help=FEATURE_DESCRIPTIONS["Age"],
            )

        with cols[2]:
            driving_license = st.selectbox(
                "Driving License",
                options=[1, 0],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help=FEATURE_DESCRIPTIONS["Driving_License"],
            )

        # Row 2
        cols2 = st.columns(3)
        with cols2[0]:
            region_code = st.number_input(
                "Region Code",
                min_value=0.0,
                max_value=100.0,
                value=28.0,
                step=1.0,
                help=FEATURE_DESCRIPTIONS["Region_Code"],
            )

        with cols2[1]:
            previously_insured = st.selectbox(
                "Previously Insured",
                options=[0, 1],
                format_func=lambda x: "No" if x == 0 else "Yes",
                help=FEATURE_DESCRIPTIONS["Previously_Insured"],
            )

        with cols2[2]:
            vehicle_age = st.selectbox(
                "Vehicle Age",
                options=["< 1 Year", "1-2 Year", "> 2 Years"],
                help=FEATURE_DESCRIPTIONS["Vehicle_Age"],
            )

        # Row 3
        cols3 = st.columns(3)
        with cols3[0]:
            vehicle_damage = st.selectbox(
                "Vehicle Damage",
                options=["Yes", "No"],
                help=FEATURE_DESCRIPTIONS["Vehicle_Damage"],
            )

        with cols3[1]:
            annual_premium = st.number_input(
                "Annual Premium",
                min_value=1000.0,
                max_value=1000000.0,
                value=30000.0,
                step=1000.0,
                format="%.0f",
                help=FEATURE_DESCRIPTIONS["Annual_Premium"],
            )

        with cols3[2]:
            policy_sales_channel = st.number_input(
                "Policy Sales Channel",
                min_value=0.0,
                max_value=200.0,
                value=26.0,
                step=1.0,
                help=FEATURE_DESCRIPTIONS["Policy_Sales_Channel"],
            )

        # Row 4
        cols4 = st.columns(3)
        with cols4[0]:
            vintage = st.number_input(
                "Vintage (Days)",
                min_value=0,
                max_value=500,
                value=150,
                step=1,
                help=FEATURE_DESCRIPTIONS["Vintage"],
            )

        with cols4[1]:
            st.markdown("")  # spacer

        with cols4[2]:
            st.markdown("")  # spacer

        submitted = st.form_submit_button(
            "🔮 Predict", type="primary", use_container_width=True
        )

    if submitted:
        # Build the input dict
        input_data = {
            "Gender": gender,
            "Age": age,
            "Driving_License": int(driving_license),
            "Region_Code": float(region_code),
            "Previously_Insured": int(previously_insured),
            "Vehicle_Age": vehicle_age,
            "Vehicle_Damage": vehicle_damage,
            "Annual_Premium": float(annual_premium),
            "Policy_Sales_Channel": float(policy_sales_channel),
            "Vintage": int(vintage),
        }
        return input_data

    return None

