import streamlit as st

st.title("নিচের button গুলো click করে, app গুলো open করা যাবে")

# Define buttons with their URLs
urls = {
    "Monthly All Die Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523",
    "(Entry Form) Maintenance": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29",
    "For Foundry Maintenance": "https://www.appsheet.com/start/66f77481-5c17-4959-8f4d-847319939c9a",
    "Maintenance (Dashboard)": "https://lookerstudio.google.com/reporting/5a415e63-ac18-46d1-bfc9-78eb60f9b943"
}

# Create buttons using st.link_button()
for name, url in urls.items():
    st.link_button(name, url)
