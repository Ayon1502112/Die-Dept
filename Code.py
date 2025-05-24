import streamlit as st

# Set page configuration for a better look
st.set_page_config(page_title="App Launcher", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        font-size: 16px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .header {
        text-align: center;
        color: #333;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .subheader {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Header and subheader
st.markdown('<div class="header">App Launcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Click the buttons below to open the respective apps</div>', unsafe_allow_html=True)

# Define buttons with their URLs
urls = {
    "Monthly All Die Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523",
    "(Entry Form) Maintenance": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29",
    "Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/5a415e63-ac18-46d1-bfc9-78eb60f9b943"
}

# Create a centered container for buttons
with st.container():
    # Use columns to make buttons look organized
    for name, url in urls.items():
        st.link_button(name, url, type="primary")
