import streamlit as st

# Set page config for wide mode and a nice theme
# This should be the very first Streamlit command
st.set_page_config(layout="centered", page_title="App Launcher", page_icon="🚀")

# Inject custom CSS for styling the app
# We use Font Awesome for icons and Inter for the font
st.markdown("""
    <style>
        /* Import Google Font 'Inter' */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        /* Import Font Awesome for icons */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');

        /* Apply Inter font to all Streamlit elements */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
        }

        /* Styling for the main header */
        .main-header {
            color: #2c3e50; /* Dark blue-gray for better contrast */
            text-align: center;
            font-size: 2.5em; /* Larger font size */
            margin-bottom: 30px;
            font-weight: 700; /* Bolder text */
            padding-bottom: 10px;
            border-bottom: 2px solid #ecf0f1; /* Subtle bottom border */
        }

        /* Container for the buttons to group them and add a background/shadow */
        .button-container {
            display: flex;
            flex-direction: column; /* Stack buttons vertically */
            gap: 20px; /* Space between buttons */
            align-items: center; /* Center buttons horizontally */
            padding: 20px;
            background-color: #f8f9fa; /* Very light gray background */
            border-radius: 15px; /* Rounded corners for the container */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow */
            max-width: 600px; /* Max width for the container */
            margin: 30px auto; /* Center the container on the page */
        }

        /* Styling for the custom link buttons */
        .custom-button {
            display: flex; /* Use flexbox for icon and text alignment */
            align-items: center;
            justify-content: center; /* Center content horizontally */
            width: 100%; /* Take full width of the container */
            padding: 15px 25px; /* Generous padding */
            background: linear-gradient(135deg, #3498db, #2980b9); /* Blue gradient background */
            color: white; /* White text color */
            border: none; /* No border */
            border-radius: 10px; /* Rounded corners for buttons */
            font-size: 1.2em; /* Larger font size for button text */
            font-weight: 600; /* Semi-bold text */
            text-decoration: none; /* Remove underline from links */
            text-align: center;
            transition: all 0.3s ease; /* Smooth transitions for hover effects */
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow for buttons */
            cursor: pointer; /* Indicate clickable element */
        }

        /* Hover effect for custom buttons */
        .custom-button:hover {
            background: linear-gradient(135deg, #2980b9, #3498db); /* Reverse gradient on hover */
            transform: translateY(-3px); /* Lift button slightly on hover */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* Enhance shadow on hover */
        }

        /* Styling for icons within the custom buttons */
        .custom-button i {
            margin-right: 10px; /* Space between icon and text */
            font-size: 1.3em; /* Slightly larger icon size */
        }

        /* Override default Streamlit button styling if any st.button() is used */
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            border: none;
            background-color: #3498db;
            color: white;
            font-size: 1.1em;
            padding: 12px;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #2980b9;
            transform: translateY(-2px);
        }

        /* General paragraph styling for the footer */
        .footer-text {
            text-align: center;
            color: #7f8c8d; /* Muted gray color */
            font-size: 0.9em;
            margin-top: 40px; /* Space above the footer text */
        }
    </style>
    """, unsafe_allow_html=True) # unsafe_allow_html is necessary to inject raw HTML/CSS

# Main title of the application
# Using st.markdown with a custom class for styling
st.markdown('<h1 class="main-header">নিচের button গুলো click করে, app গুলো open করা যাবে</h1>', unsafe_allow_html=True)

# Define buttons with their URLs and Font Awesome icons
# Each entry is a dictionary containing the URL and the icon class
urls = {
    "Monthly All Die Maintenance (Dashboard)": {
        "url": "https://lookerstudio.google.com/reporting/6d689733-0d3c-4667-ac7f-ee96cd4f0523",
        "icon": "fas fa-chart-line" # Icon for a dashboard (chart line)
    },
    "(Entry Form) Maintenance": {
        "url": "https://www.appsheet.com/start/a81e8891-6548-4994-80c5-d7ec4f7d8c29",
        "icon": "fas fa-clipboard-list" # Icon for an entry form (clipboard list)
    },
    "For Foundry Maintenance": {
        "url": "https://www.appsheet.com/start/66f77481-5c17-4959-8f4d-847319939c9a",
        "icon": "fas fa-industry" # Icon for foundry (industry building)
    },
    "Maintenance (Dashboard)": {
        "url": "https://lookerstudio.google.com/reporting/5a415e63-ac18-46d1-bfc9-78eb60f9b943",
        "icon": "fas fa-tachometer-alt" # Another icon for a dashboard (tachometer)
    }
}

# Start the button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Iterate through the defined URLs and create a custom-styled button for each
for name, data in urls.items():
    url = data["url"]
    icon = data["icon"]
    # Use st.markdown to insert custom HTML for each button
    # The 'target="_blank"' attribute ensures the link opens in a new tab
    st.markdown(f"""
        <a href="{url}" target="_blank" class="custom-button">
            <i class="{icon}"></i> {name}
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
