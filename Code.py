import streamlit as st

# Set page configuration for a modern look
st.set_page_config(page_title="App Launcher", layout="wide")

# Custom CSS for styling (avoiding red)
st.markdown("""
    <style>
    .main {
        background-color: #e6f0fa;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1e88e5;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #1567 fancied;
        transform: translateY(-2px);
    }
    .header {
        text-align: center;
        color: #1e88e5;
        font-size: 36px;
        font-family: 'Arial', sans-serif;
        margin-bottom: 10px;
    }
    .subheader {
        text-align: center;
        color: #555;
        font-size: 20px;
        font-family: 'Arial', sans-serif;
        margin-bottom: 40px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<div class="header">App Launcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Access your apps with a single click below</div>', unsafe_allow_html=True)

# Define buttons with their URLs
urls = {
    "Monthly All Die Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f7d8c",
    "(Entry Form) Maintenance": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29",
    "Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/5a415e63-ac18-46d1-bfc9-78eb60f9b943"
}

# Create a container for a card-like layout
with st.container():
    for name, url in urls.items():
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.link_button(name, url, type="primary")
            st.markdown('</div>', unsafe_allow_html=True)
