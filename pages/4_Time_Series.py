import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Page Config
st.set_page_config(page_title="Time Series Sales Analysis", page_icon="📈", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🌟 Background Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #6a1b9a, #d50000);
        color: white;
    }

    /* ✨ Section Heading */
    .section-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #ffebee;
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
st.markdown('<p class="section-title">📈 Time Series Sales Analysis</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state:
    df = st.session_state["df"]

    # ✅ Convert 'Order Date' to datetime if not already
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    # ✅ Aggregate Sales Over Time
    time_series_data = df.groupby("Order Date")["Sales"].sum().reset_index()

    # ✅ Explanation Box
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page **analyzes sales trends over time**.
        - The **line chart below** shows the fluctuation of sales over different periods.
        - Hover over any point to see **exact sales figures** for that date.
        - You can **zoom into specific time ranges** to identify trends and patterns.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Time Series Sales Chart
    st.markdown('<div class="chart-container"><strong>📊 Sales Trend Over Time:</strong></div>', unsafe_allow_html=True)
    fig_time_series = px.line(time_series_data, x="Order Date", y="Sales", title="Sales Trend Over Time",
                              color_discrete_sequence=["#ff1744"])
    fig_time_series.update_traces(mode='lines+markers', marker=dict(size=5))

    st.plotly_chart(fig_time_series, use_container_width=True)

    # ✅ Moving Average Selection
    moving_avg_window = st.slider("Select Moving Average Window (Days)", min_value=7, max_value=90, step=7, value=30)
    
    # ✅ Calculate & Plot Moving Average
    time_series_data["Moving Average"] = time_series_data["Sales"].rolling(window=moving_avg_window).mean()

    st.markdown('<div class="chart-container"><strong>📈 Sales Moving Average Analysis:</strong></div>', unsafe_allow_html=True)
    fig_moving_avg = px.line(time_series_data, x="Order Date", y=["Sales", "Moving Average"], 
                             title=f"Sales vs {moving_avg_window}-Day Moving Average", 
                             labels={"value": "Sales"},
                             color_discrete_map={"Sales": "#ff1744", "Moving Average": "#651fff"})

    fig_moving_avg.update_traces(mode='lines', line=dict(width=2))
    st.plotly_chart(fig_moving_avg, use_container_width=True)

else:
    st.warning("⚠ No data found! Please upload a CSV file on the home page first.")
