import streamlit as st

# Set page config for wide mode and a nice theme
st.set_page_config(layout="centered", page_title="App Launcher", page_icon="🚀")

# Inject custom CSS for styling the app
st.markdown("""
    <style>
        /* Import Google Font 'Inter' */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        /* Apply Inter font to all Streamlit elements */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
        }

        /* Styling for the main header */
        .main-header {
            color: #2c3e50;
            text-align: center;
            font-size: 2.5em;
            margin-bottom: 30px;
            font-weight: 700;
            padding-bottom: 10px;
            border-bottom: 2px solid #ecf0f1;
        }

        /* Container for the buttons to group them and add a background/shadow */
        .button-container {
            display: flex;
            flex-direction: column;
            gap: 15px;
            align-items: center;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 15px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
            max-width: 600px;
            margin: 30px auto;
            border: 1px solid #e0e0e0;
        }

        /* Styling for the custom link buttons */
        .custom-button {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 15px 25px;
            background-color: #f0f2f6;
            color: #2c3e50;
            border: 1px solid #dcdcdc;
            border-radius: 10px;
            font-size: 1.1em;
            font-weight: 600;
            text-decoration: none; /* Remove underline */
            text-align: center;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            cursor: pointer;
        }

        /* Hover effect for custom buttons */
        .custom-button:hover {
            background-color: #e0e2e6;
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-color: #c0c0c0;
        }

        /* General paragraph styling for the footer */
        .footer-text {
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9em;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Main title of the application
st.markdown('<h1 class="main-header">নিচের button গুলো click করে, app গুলো open করা যাবে</h1>', unsafe_allow_html=True)

# Define buttons with their URLs
all_urls = {
    "Monthly All Die Maintenance (Dashboard)": {
        "url": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523"
    },
    "(Entry Form) Maintenance": {
        "url": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29"
    },
    "For Foundry Maintenance": {
        "url": "https://www.appsheet.com/start/66f77481-5c17-4959-8f4d-847319939c9a"
    },
    "Maintenance (Dashboard)": {
        "url": "https://lookerstudio.google.com/reporting/5a415e63-ac18-46d1-bfc9-78eb60f9b943"
    }
}

# Start the button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Iterate through the URLs and create a custom-styled button for each
for name, data in all_urls.items():
    url = data["url"]
    st.markdown(f"""
        <a href="{url}" target="_blank" class="custom-button">
            {name}
        </a>
    """, unsafe_allow_html=True)

# Close the button container
st.markdown('</div>', unsafe_allow_html=True)

# Add a small informative footer
st.markdown("""
    <p class="footer-text">
        Click on any button above to open the respective application in a new tab.
    </p>
""", unsafe_allow_html=True)
