import streamlit as st
import plotly.express as px
import pandas as pd

# ✅ Page Config
st.set_page_config(page_title="Region-wise Sales", page_icon="📍", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🎀 Dual Pink Gradient Background */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #880e4f, #f8bbd0); /* Dark Pink + Light Pink */
        color: black; /* Changed text color to black */
    }

    /* 🌟 Section Title with Icon (Heading Color Kept) */
    .section-title {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        color: #f8bbd0; /* Light Pink */
        text-shadow: 3px 3px 15px rgba(0, 0, 0, 0.7);
        animation: fadeIn 2s ease-in-out;
    }

    /* 💜 Explanation Box */
    .explanation-box {
        background: rgba(255, 255, 255, 0.2);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.3);
        font-size: 20px;
        line-height: 1.7;
        text-align: justify;
        margin-top: 20px;
        color: black; /* Changed text color to black */
    }

    /* 🎡 Chart Container */
    .chart-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: black; /* Changed text color to black */
    }

    .chart-container:hover {
        transform: scale(1.03);
        background: rgba(255, 255, 255, 0.2);
    }

    /* 🌟 Big Icons */
    .icon {
        font-size: 80px;
        display: block;
        text-align: center;
        margin-bottom: 10px;
    }

    /* 🛠️ Fade-In Animation */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Title with Animation & Icon
st.markdown('<p class="icon">📍</p>', unsafe_allow_html=True)
st.markdown('<p class="section-title">Region-wise Sales</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state:
    df = st.session_state["df"]

    # ✅ Display Data Insights with Icon
    st.markdown('<div class="chart-container"><p class="icon">📊</p><strong>Regional Sales Overview:</strong></div>', unsafe_allow_html=True)

    # ✅ Calculate Sales per Region
    region_sales = df.groupby("Region", as_index=False)["Sales"].sum()

    # ✅ Show Summary with Icons
    st.markdown('<p class="icon">💰</p>', unsafe_allow_html=True)
    st.write(f"**Total Sales Across All Regions:** ${df['Sales'].sum():,.2f}")

    st.markdown('<p class="icon">🌍</p>', unsafe_allow_html=True)
    st.write(f"**Number of Unique Regions:** {df['Region'].nunique()}")

    # ✅ Explanation Box with Icon
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.markdown('<p class="icon">🔍</p>', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page provides insights into **sales distribution by region**.
        - The **pie chart** below shows the proportion of total sales for each region.
        - You can select a region from the dropdown to see **detailed statistics** about it.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Pie Chart Visualization with Icon
    st.markdown('<div class="chart-container"><p class="icon">📊</p><strong>Sales Distribution by Region:</strong></div>', unsafe_allow_html=True)
    fig_region = px.pie(region_sales, values="Sales", names="Region", hole=0.5, title="Sales Distribution by Region")
    fig_region.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_region, use_container_width=True)

    # ✅ Dropdown for Region-wise Statistics
    selected_region = st.selectbox("Select a region for more details", df["Region"].unique())

    # ✅ Display Stats for Selected Region with Icon
    if selected_region:
        region_data = df[df["Region"] == selected_region]
        total_region_sales = region_data["Sales"].sum()
        total_orders = region_data.shape[0]
        avg_sales = region_data["Sales"].mean()

        st.markdown('<div class="chart-container"><p class="icon">📍</p><strong>Regional Sales Statistics:</strong></div>', unsafe_allow_html=True)
        st.write(f"**Region:** {selected_region}")
        st.write(f"**Total Sales:** ${total_region_sales:,.2f}")
        st.write(f"**Total Orders:** {total_orders}")
        st.write(f"**Average Sales per Order:** ${avg_sales:,.2f}")

else:
    st.warning("⚠ No data found! Please upload a CSV file on the previous page.")
