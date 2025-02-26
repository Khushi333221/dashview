import streamlit as st
import plotly.figure_factory as ff
import pandas as pd

# ✅ Page Config
st.set_page_config(page_title="Sales Data Table", page_icon="📋", layout="wide")

# ✅ Apply Custom CSS for Styling & Animation
st.markdown("""
    <style>
    /* 🌟 Background Styling */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #66bb6a, #e91e63); /* Green & Pink */
        color: white;
    }

    /* ✨ Section Heading */
    .section-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: #ffffff;
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

    /* 📊 Table Container */
    .table-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        transition: 0.3s;
        text-align: center;
    }

    .table-container:hover {
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
st.markdown('<p class="section-title">📋 Sales Data Table</p>', unsafe_allow_html=True)

# ✅ Check if Data Exists
if "df" in st.session_state and not st.session_state["df"].empty:
    df = st.session_state["df"]

    # ✅ Explanation Box
    st.markdown('<div class="explanation-box">', unsafe_allow_html=True)
    st.write("### What is happening on this page?")
    st.write(
        """
        - This page **displays a structured table** with key sales data fields.
        - The table provides an **interactive, scrollable** view for easy navigation.
        - You can **search, filter, and download** the dataset for further analysis.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # ✅ Table Visualization
    st.markdown('<div class="table-container"><strong>📊 Sales Data Table:</strong></div>', unsafe_allow_html=True)
    
    # ✅ Filter Option - Search Data
    search_query = st.text_input("🔍 Search by State or Region", "")
    if search_query:
        filtered_df = df[df["State"].str.contains(search_query, case=False, na=False) | 
                         df["Region"].str.contains(search_query, case=False, na=False)]
    else:
        filtered_df = df

    # ✅ Display the First Few Rows in a Styled Table
    fig_table = ff.create_table(filtered_df[['Order Date', 'Sales', 'Region', 'State', 'Category']].head(), 
                                colorscale="greens_r")  # Green Theme
    st.plotly_chart(fig_table)

    # ✅ Download Data Button
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button(label="💾 Download Data as CSV", data=csv, file_name="sales_data.csv", mime="text/csv")

else:
    st.warning("⚠ No data found! Please upload a CSV file on the home page first.")
