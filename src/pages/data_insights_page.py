"""
Data Insights page — explore the dataset, distributions, and key statistics.
"""
import streamlit as st
import pandas as pd

from src.constants.constants import DATA_INSIGHTS_HEADING
from src.utils.data_loader import load_raw_data


def show_data_insights():
    """Render the Data Insights page."""
    st.title(f"📈 {DATA_INSIGHTS_HEADING}")
    st.divider()

    st.markdown(
        """
        Explore the raw training dataset used for model development.
        The data contains **381,109 customer records** with **11 columns**
        (10 features + 1 target).
        """
    )

    try:
        with st.spinner("Loading dataset..."):
            df = load_raw_data()

        # ---- Dataset Preview ----
        st.markdown("### 👀 Dataset Preview")
        st.dataframe(df.head(100), use_container_width=True, hide_index=True)
        st.caption(f"Showing first 100 of {df.shape[0]:,} rows | {df.shape[1]} columns")

        st.divider()

        # ---- Dataset Shape ----
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Rows", f"{df.shape[0]:,}")
        with col2:
            st.metric("Total Columns", df.shape[1])

        st.divider()

        # ---- Data Types & Missing Values ----
        st.markdown("### 📋 Data Types & Missing Values")
        info_df = pd.DataFrame(
            {
                "Column": df.dtypes.index,
                "Data Type": df.dtypes.values.astype(str),
                "Non-Null Count": df.notna().sum().values,
                "Null Count": df.isna().sum().values,
                "Null %": (df.isna().sum().values / len(df) * 100).round(2),
                "Unique Values": df.nunique().values,
            }
        )
        st.dataframe(info_df, use_container_width=True, hide_index=True)

        st.divider()

        # ---- Descriptive Statistics ----
        st.markdown("### 📊 Descriptive Statistics (Numerical Columns)")
        st.dataframe(
            df.describe().style.format("{:.2f}"),
            use_container_width=True,
        )

        st.divider()

        # ---- Target Distribution ----
        st.markdown("### 🎯 Target Distribution (Response)")
        if "Response" in df.columns:
            target_counts = df["Response"].value_counts().reset_index()
            target_counts.columns = ["Response", "Count"]
            target_counts["Percentage"] = (
                target_counts["Count"] / target_counts["Count"].sum() * 100
            ).round(2)

            col1, col2 = st.columns(2)
            with col1:
                st.dataframe(
                    target_counts.style.format({"Percentage": "{:.2f}%"}),
                    use_container_width=True,
                    hide_index=True,
                )
            with col2:
                st.bar_chart(target_counts.set_index("Response")["Count"])

            st.info(
                f"**Imbalance ratio:** {target_counts.iloc[1]['Percentage']:.2f}% "
                f"positive class vs {target_counts.iloc[0]['Percentage']:.2f}% "
                f"negative class. Only ~12% of customers are interested."
            )

        st.divider()

        # ---- Categorical Distributions ----
        st.markdown("### 📊 Categorical Feature Distributions")
        cat_cols = ["Gender", "Vehicle_Age", "Vehicle_Damage", "Previously_Insured"]
        cat_tabs = st.tabs(cat_cols)
        for tab, col in zip(cat_tabs, cat_cols):
            with tab:
                if col in df.columns:
                    counts = df[col].value_counts().reset_index()
                    counts.columns = [col, "Count"]
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.dataframe(counts, use_container_width=True, hide_index=True)
                    with col_b:
                        st.bar_chart(counts.set_index(col)["Count"])

    except Exception as e:
        st.error(f"⚠️ Could not load dataset: {e}")
        st.info(
            "Ensure the raw data file exists at `artifacts/raw_data/train.csv` "
            "and the notebook has been executed."
        )

