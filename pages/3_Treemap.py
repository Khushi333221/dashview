import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ Page Config
st.set_page_config(page_title="Sales Treemap", page_icon="📊", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🌟 Background Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #ffcc80, #ff9800);
        color: black;
    }

    /* ✨ Section Heading */
    .section-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #6d4c41;
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
st.markdown('<p class="section-title">📊 Sales Treemap & Insights</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state:
    df = st.session_state["df"]

    # ✅ Explanation Box
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page **visualizes sales distribution** across different **categories and sub-categories**.
        - The **treemap** below helps in understanding which categories contribute the most to total sales.
        - Larger blocks represent **higher sales values**, while smaller blocks indicate **lower contributions**.
        - **Hover over** any section to see the exact sales figures for that category.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Treemap Chart
    st.markdown('<div class="chart-container"><strong>📊 Sales Treemap Visualization:</strong></div>', unsafe_allow_html=True)
    fig_treemap = px.treemap(df, path=['Category', 'Sub-Category'], values='Sales', title='Sales Treemap', color='Sales',
                             color_continuous_scale='sunsetdark')
    st.plotly_chart(fig_treemap, use_container_width=True)

    # ✅ Dropdown for Category-wise Analysis
    selected_category = st.selectbox("Select a category for detailed insights", df["Category"].unique())

    # ✅ Display Stats for Selected Category
    if selected_category:
        category_data = df[df["Category"] == selected_category]
        total_category_sales = category_data["Sales"].sum()
        total_category_orders = category_data.shape[0]
        avg_category_sales = category_data["Sales"].mean()

        st.markdown('<div class="chart-container"><strong>📊 Category Sales Statistics:</strong></div>', unsafe_allow_html=True)
        st.write(f"**Category:** {selected_category}")
        st.write(f"**Total Sales:** ${total_category_sales:,.2f}")
        st.write(f"**Total Orders:** {total_category_orders}")
        st.write(f"**Average Sales per Order:** ${avg_category_sales:,.2f}")

        # ✅ Sub-Category Sales Breakdown
        st.markdown('<div class="chart-container"><strong>📂 Sub-Category Sales Breakdown:</strong></div>', unsafe_allow_html=True)
        fig_subcategory = px.bar(category_data, x="Sub-Category", y="Sales", text_auto=True, title=f"Sales Breakdown for {selected_category}",
                                 color="Sales", color_continuous_scale="sunsetdark")
        st.plotly_chart(fig_subcategory, use_container_width=True)

else:
    st.warning("⚠ No data found! Please upload a CSV file on the home page first.")
