# app.py
import streamlit as st
from datetime import datetime
import pytz
import styles
import viber_blast
import email_blast_bucket2
import email_blast_bucket4
import email_blast_level1
import email_blast_level6
import email_blast_sbf_new_endo   # ← ONLY CORRECT VERSION (Client Name included)
import mc4_ptp
import auto_statistics
import live_inbound_monitoring
import random
import sms_blasting

# === LOGIN CREDENTIALS (MOVE TO secrets.toml FOR PRODUCTION) ===
try:
    USERNAME = st.secrets["USERNAME"]
    PASSWORD = st.secrets["PASSWORD"]
except:
    USERNAME = "zmjepollo"
    PASSWORD = "Hepollo_021"

# === PAGE CONFIG ===
st.set_page_config(
    page_title="WORKLOADS-AUTOMATED",
    page_icon="Chart Increasing",
    layout="wide"
)

# === CUSTOM CSS ===
st.markdown(styles.custom_css, unsafe_allow_html=True)

# === LOGIN STATE ===
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# === LOGIN PAGE ===
if not st.session_state.logged_in:
    st.header("Login to WORKLOADS-AUTOMATED")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        login_btn = st.button("Login", use_container_width=True, type="primary")

        if login_btn:
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Invalid username or password")

else:
    # === MOTIVATIONAL QUOTE ===
    st.markdown(f"<div class='quote-box'>{random.choice(styles.motivational_quotes)}</div>", unsafe_allow_html=True)

    # === SIDEBAR MENU ===
    with st.sidebar:
        st.markdown(
            """
            <div class="burger-menu">Menu</div>
            """,
            unsafe_allow_html=True
        )

        option = st.selectbox(
            "Select Tool:",
            [
                "VIBER BLAST",
                "SMS BLASTING",
                "EMAIL BLAST",
                "LIVE INBOUND MONITORING",
                "AUTO STATISTICS"
            ],
            key="main_option",
            label_visibility="collapsed"
        )

    # === MAIN CONTENT ROUTING ===
    if option == "VIBER BLAST":
        viber_blast.viber_blast_section()

    elif option == "SMS BLASTING":
        sms_blasting.sms_blasting_section()

    elif option == "EMAIL BLAST":
        email_option = st.selectbox(
            "Select Email Blast Type:",
            [
                "BUCKET 2",
                "BUCKET 4",
                "LEVEL 1 NEGATIVE ACCOUNT",
                "LEVEL 6 NEGATIVE ACCOUNT",
                "SBF",           # ← CLEAN LABEL (was SBF NEW ENDO)
                "MC4 PTP"
            ],
            key="email_blast_option"
        )

        if email_option == "BUCKET 2":
            email_blast_bucket2.email_blast_bucket2_section()
        elif email_option == "BUCKET 4":
            email_blast_bucket4.email_blast_bucket4_section()
        elif email_option == "LEVEL 1 NEGATIVE ACCOUNT":
            email_blast_level1.email_blast_level1_section()
        elif email_option == "LEVEL 6 NEGATIVE ACCOUNT":
            email_blast_level6.email_blast_level6_section()
        elif email_option == "SBF":   # ← MATCHES NEW LABEL
            email_blast_sbf_new_endo.email_blast_sbf_new_endo_section()
        elif email_option == "MC4 PTP":
            mc4_ptp.mc4_ptp_section()

    elif option == "LIVE INBOUND MONITORING":
        live_inbound_monitoring.live_inbound_monitoring_section()

    elif option == "AUTO STATISTICS":
        auto_option = st.selectbox(
            "Select Auto Statistics Type:",
            [
                "SBF NEGATIVE AUTOSTATS",
                "L1-L6 NEGATIVE AUTOSTATS",
                "SBF NEW ENDO"
            ],
            key="auto_statistics_option"
        )
        if auto_option == "SBF NEGATIVE AUTOSTATS":
            auto_statistics.auto_statistics_section(stats_option="SBF NEGATIVE AUTOSTATS")
        elif auto_option == "L1-L6 NEGATIVE AUTOSTATS":
            auto_statistics.auto_statistics_section(stats_option="L1-L6 NEGATIVE AUTOSTATS")
        elif auto_option == "SBF NEW ENDO":
            auto_statistics.auto_statistics_sbf_new_endo_section()

    # === FOOTER ===
    st.markdown(
        f"""
        <div class='footer'>
            <p>WORKLOADS-AUTOMATED v1.0 | Last updated: {datetime.now(pytz.timezone('Asia/Manila')).strftime('%B %d, %Y %I:%M %p PHT')}</p>
        </div>
        """,
        unsafe_allow_html=True
    )