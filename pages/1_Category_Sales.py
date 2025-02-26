import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Page Config
st.set_page_config(page_title="Data Insights", page_icon="📊", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🌟 Background Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #1a1a40, #4b0082); /* Dark Blue & Dark Purple */
        color: white;
    }

    /* ✨ Section Heading */
    .section-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #FFD700;
        text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
        animation: fadeIn 2s ease-in-out;
    }

    /* 📜 Explanation Box */
    .explanation-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        font-size: 18px;
        line-height: 1.6;
        text-align: justify;
        margin-top: 20px;
    }

    /* 📊 Chart Container */
    .chart-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
        text-align: center;
    }

    .chart-container:hover {
        transform: scale(1.02);
        background: rgba(255, 255, 255, 0.2);
    }

    /* 🔄 Fade-In Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    </style>
""", unsafe_allow_html=True)

# ✅ Title with Animation
st.markdown('<p class="section-title">📊 Data Insights & Analysis</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state:
    df = st.session_state["df"]

    # ✅ Display Data Insights
    st.markdown('<div class="chart-container"><strong>🔍 Dataset Overview:</strong></div>', unsafe_allow_html=True)
    
    st.write(f"**Total Rows:** {df.shape[0]}")
    st.write(f"**Total Columns:** {df.shape[1]}")

    # ✅ Categorical & Numerical Column Insights
    categorical_cols = df.select_dtypes(include=['object']).columns
    numerical_cols = df.select_dtypes(include=['number']).columns

    st.markdown('<div class="chart-container"><strong>📂 Categorical Data Summary:</strong></div>', unsafe_allow_html=True)
    for col in categorical_cols:
        st.write(f"**{col}:** {df[col].nunique()} unique categories")

    st.markdown('<div class="chart-container"><strong>📊 Numerical Data Summary:</strong></div>', unsafe_allow_html=True)
    for col in numerical_cols:
        st.write(f"**{col}:** Mean value = {df[col].mean():.2f}")

    # ✅ Explanation Box
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page provides an **overview of the dataset** uploaded in the previous step.
        - It identifies **categorical columns** (e.g., region, category, customer segment) and counts unique values.
        - It also summarizes **numerical columns** (e.g., sales, profit, quantity) by calculating their mean values.
        - **A dynamic chart** is displayed below to visualize categorical data distributions.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Display Categorical Data Chart
    st.markdown('<div class="chart-container"><strong>📊 Categorical Data Visualization:</strong></div>', unsafe_allow_html=True)
    
    selected_col = st.selectbox("Select a categorical column for visualization", categorical_cols)

    if selected_col:
        fig, ax = plt.subplots(figsize=(10, 5))
        df[selected_col].value_counts().plot(kind="bar", color="yellow", ax=ax)
        ax.set_title(f"Distribution of {selected_col}", fontsize=16, fontweight="bold")
        ax.set_ylabel("Count")
        ax.set_xlabel(selected_col)
        ax.grid(axis="y", linestyle="--", alpha=0.7)
        st.pyplot(fig)

else:
    st.warning("⚠ No data found! Please upload a CSV file on the previous page.")
