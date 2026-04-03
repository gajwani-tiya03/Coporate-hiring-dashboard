import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------- MODEL --------
def logistic_growth(t, P0, K, r):
    return K / (1 + ((K - P0) / P0) * np.exp(-r * t))

# -------- PAGE CONFIG --------
st.set_page_config(page_title="Hiring Dashboard", layout="wide")

# -------- CUSTOM UI --------
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1F3A;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding: 30px 0;
    }

    /* Card Container */
    .main > div {
        background-color: #25274D;
        border: 3px solid #6C63FF;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4), 0 0 20px rgba(157, 78, 221, 0.4);
        padding: 25px;
        max-width: 1100px;
        width: 100%;
    }

    .header-box {
        background: linear-gradient(90deg, #5F4BFF, #A259FF, #C77DFF);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        box-shadow: 0 0 15px rgba(199, 125, 255, 0.6);
    }

    .section {
        font-size: 18px;
        font-weight: bold;
        color: #C77DFF;
        margin-bottom: 10px;
    }

    label {
        color: #E0E0FF !important;
        font-weight: 600 !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #7B2CBF, #9D4EDD);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 0 10px rgba(157, 78, 221, 0.6);
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        box-shadow: 0 0 18px rgba(199, 125, 255, 0.9);
        transform: scale(1.03);
    }

    .stNumberInput input {
        background-color: #2A1E5C;
        border: 2px solid #9D4EDD;
        border-radius: 10px;
        color: #EAEAFF;
        box-shadow: 0 0 8px rgba(157, 78, 221, 0.4);
    }

    .stNumberInput button {
        background-color: #5A189A;
        border-radius: 6px;
        color: white;
    }

    .divider {
        border-left: 3px solid #6C63FF;
        height: 500px;
        margin: auto;
        box-shadow: 0 0 10px rgba(108, 99, 255, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# -------- HEADER --------
st.markdown('<div class="header-box">📊 Corporate Hiring Dashboard</div>', unsafe_allow_html=True)

# -------- LAYOUT --------
col1, divider, col2 = st.columns([1, 0.05, 1.5])

# -------- INPUT PANEL --------
with col1:
    st.markdown('<div class="section">🧾 Input Parameters</div>', unsafe_allow_html=True)

    P0 = st.number_input("Initial Employees", value=50)
    K = st.number_input("Max Workforce", value=500)
    r = st.number_input("Growth Rate", value=0.3)
    time_period = st.number_input("Time (Months)", value=24)

    simulate = st.button("Simulate")

# -------- DIVIDER --------
with divider:
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# -------- OUTPUT PANEL --------
with col2:
    st.markdown('<div class="section">📈 Results</div>', unsafe_allow_html=True)

    if simulate:
        t = np.linspace(0, time_period, 50)
        employees = logistic_growth(t, P0, K, r)

        growth_rate = r * employees * (1 - employees / K)
        peak_time = round(t[np.argmax(growth_rate)], 2)

        st.success(f"📈 Peak Hiring Month: {peak_time}")

        # -------- GRAPH --------
        fig, ax = plt.subplots(figsize=(4,2))
        ax.plot(t, employees, color="#C77DFF", linewidth=2)
        ax.set_xlabel("Time (Months)")
        ax.set_ylabel("Employees")
        ax.set_title("Hiring Trend")
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        fig.patch.set_facecolor('#25274D')
        ax.set_facecolor('#25274D')

        st.pyplot(fig, use_container_width=False)

        # -------- TABLE --------
        st.markdown('<div class="section">📋 Data Table</div>', unsafe_allow_html=True)

        data = {
            "Time (Months)": [round(i,2) for i in t],
            "Employees": [int(i) for i in employees]
        }

        st.dataframe(data, use_container_width=True)
