import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Page Config
st.set_page_config(page_title="Hierarchical Sales View", page_icon="🌞", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🌟 Background Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fdd835, #1976d2); /* Lemon Yellow + Deep Blue */
        color: white;
    }

    /* ✨ Section Heading */
    .section-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #fff9c4; /* Soft Lemon */
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
st.markdown('<p class="section-title">🌞 Hierarchical Sales View</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state and not st.session_state["df"].empty:
    df = st.session_state["df"]

    # ✅ Explanation Box
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page **visualizes sales hierarchy** using an **interactive Sunburst Chart**.
        - The chart breaks down **sales across different levels**, from **Category → Sub-Category → Product Name**.
        - You can explore the sales distribution **dynamically** and hover over sections for more details.
        - Additional charts below provide **deep insights** into sales trends.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Total Sales Summary
    total_sales = df["Sales"].sum()
    total_orders = df.shape[0]
    unique_categories = df["Category"].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
    col2.metric("📦 Total Orders", total_orders)
    col3.metric("🗂 Unique Categories", unique_categories)

    # ✅ Sunburst Chart Visualization
    st.markdown('<div class="chart-container"><strong>🌞 Sales Hierarchy Breakdown:</strong></div>', unsafe_allow_html=True)
    fig_hierarchical = px.sunburst(df, path=['Category', 'Sub-Category', 'Product Name'], values='Sales',
                                   title="Sales Hierarchy",
                                   color_discrete_sequence=["#ffeb3b", "#0d47a1", "#ff9800", "#2196f3"])  # Lemon & Blue Variations
    st.plotly_chart(fig_hierarchical, use_container_width=True)

    # ✅ Bar Chart - Top Selling Categories
    st.markdown('<div class="chart-container"><strong>📊 Top-Selling Categories:</strong></div>', unsafe_allow_html=True)
    top_categories = df.groupby("Category")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)
    fig_top_categories = px.bar(top_categories, x="Category", y="Sales", text="Sales", 
                                title="Top-Selling Categories", color="Category", color_discrete_sequence=["#fdd835", "#1976d2"])
    fig_top_categories.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
    st.plotly_chart(fig_top_categories, use_container_width=True)

    # ✅ Dropdown Filter - Category Wise Analysis
    st.markdown('<div class="chart-container"><strong>🔍 Filter Sales by Category:</strong></div>', unsafe_allow_html=True)
    selected_category = st.selectbox("Select a category to analyze:", df["Category"].unique())

    if selected_category:
        filtered_df = df[df["Category"] == selected_category]
        filtered_sales = filtered_df.groupby("Sub-Category")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)

        st.markdown(f"### 📂 Sales Breakdown for **{selected_category}**")
        fig_filtered_sales = px.bar(filtered_sales, x="Sub-Category", y="Sales", text="Sales",
                                    title=f"Sales Distribution in {selected_category}", color="Sub-Category",
                                    color_discrete_sequence=["#ff9800", "#1976d2"])
        fig_filtered_sales.update_traces(texttemplate='$%{text:,.2f}', textposition='outside')
        st.plotly_chart(fig_filtered_sales, use_container_width=True)

else:
    st.warning("⚠ No data found! Please upload a CSV file on the home page first.")
