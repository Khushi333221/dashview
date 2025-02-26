import streamlit as st
import pandas as pd

# ✅ Set Page Config (This should always be first)
st.set_page_config(page_title="Superstore Dashboard", page_icon="📊", layout="wide")

# ✅ Apply Custom CSS for Styling
st.markdown("""
    <style>
    /* 🌟 Professional Gradient Background with Yellow */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(45deg, #0f2027, #203a43, #2c5364, #FFD700);
        background-size: 300% 300%;
        animation: gradientBG 8s ease infinite;
        color: white;
    }

    /* 🌟 Smooth Background Animation */
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 🔹 MASSIVE Title Styling */
    .title {
        text-align: center;
        font-size: 200px; /* 9x the original size */
        font-weight: bold;
        color: white;
        text-shadow: 5px 5px 25px rgba(0, 0, 0, 0.7);
    }

    /* ✨ Animated Heading Effect */
    @keyframes glow {
        0% { text-shadow: 0 0 20px #fff, 0 0 40px #FFD700, 0 0 60px #FFD700; }
        50% { text-shadow: 0 0 30px #fff, 0 0 50px #FFD700, 0 0 70px #FFD700; }
        100% { text-shadow: 0 0 20px #fff, 0 0 40px #FFD700, 0 0 60px #FFD700; }
    }

    .glowing-text {
        animation: glow 2s infinite alternate;
    }

    /* 📂 File Upload Box */
    div.stFileUploader {
        border: 3px solid white;
        padding: 15px;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.2);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    }

    /* 🔘 Button Styling */
    div.stButton>button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        border-radius: 10px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton>button:hover {
        background: #ff4b2b;
        transform: scale(1.08);
        box-shadow: 0px 4px 15px rgba(255, 75, 43, 0.5);
    }

    /* 📊 Metric Box Styling */
    .metric-container {
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        font-size: 18px;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)

# ✅ Title with Animation (MASSIVE SIZE)
st.markdown('<p class="title glowing-text">🌟 Superstore Dashboard</p>', unsafe_allow_html=True)

# ✅ File Upload Section
st.markdown("### 📂 Upload Your Data File")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# ✅ Data Handling with Encoding Fix
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors='coerce')

    # Store DataFrame in session state
    st.session_state["df"] = df

    # ✅ Display Success Message
    st.success("🎉 File uploaded successfully! Now, navigate to different pages to see the visualizations.")

    # ✅ Display Data Preview
    st.markdown('<div class="metric-container">📊 <strong>Data Preview:</strong></div>', unsafe_allow_html=True)
    st.dataframe(df.head(5))  # Show first 5 rows of the uploaded CSV file
