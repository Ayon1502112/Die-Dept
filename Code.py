import streamlit as st

# Set page config for wide mode and a nice theme
# This should be the very first Streamlit command
st.set_page_config(layout="centered", page_title="App Launcher", page_icon="🚀")

# Inject custom CSS for styling the app
# We use Inter for the font
st.markdown("""
    <style>
        /* Import Google Font 'Inter' */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        /* Font Awesome is no longer needed as icons are removed */

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

        /* Styling for the search input field */
        .stTextInput > div > div > input {
            border-radius: 8px; /* Rounded corners for search bar */
            border: 1px solid #ced4da; /* Light gray border */
            padding: 10px 15px; /* Comfortable padding */
            font-size: 1.1em;
            box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.05); /* Subtle inner shadow */
            transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }

        .stTextInput > div > div > input:focus {
            border-color: #80bdff; /* Blue border on focus */
            box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Light blue shadow on focus */
            outline: none; /* Remove default outline */
        }

        /* Container for the buttons to group them and add a background/shadow */
        .button-container {
            display: flex;
            flex-direction: column; /* Stack buttons vertically */
            gap: 15px; /* Space between buttons */
            align-items: center; /* Center buttons horizontally */
            padding: 20px;
            background-color: #ffffff; /* White background for the container */
            border-radius: 15px; /* Rounded corners for the container */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08); /* Softer, more pronounced shadow */
            max-width: 600px; /* Max width for the container */
            margin: 30px auto; /* Center the container on the page */
            border: 1px solid #e0e0e0; /* Light border for the container */
        }

        /* Styling for the custom link buttons */
        .custom-button {
            display: flex; /* Use flexbox for text alignment */
            align-items: center;
            justify-content: center; /* Center content horizontally */
            width: 100%; /* Take full width of the container */
            padding: 15px 25px; /* Generous padding */
            background-color: #f0f2f6; /* Very light gray background */
            color: #2c3e50; /* Dark text color for readability */
            border: 1px solid #dcdcdc; /* Light gray border */
            border-radius: 10px; /* Rounded corners for buttons */
            font-size: 1.1em; /* Slightly smaller font size for button text */
            font-weight: 600; /* Semi-bold text */
            text-decoration: none; /* Explicitly remove underline from links */
            text-align: center;
            transition: all 0.2s ease-in-out; /* Smooth transitions for hover effects */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Subtle shadow for buttons */
            cursor: pointer; /* Indicate clickable element */
        }

        /* Hover effect for custom buttons */
        .custom-button:hover {
            background-color: #e0e2e6; /* Slightly darker light gray on hover */
            transform: translateY(-2px); /* Lift button slightly on hover */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Enhance shadow on hover */
            border-color: #c0c0c0; /* Darker border on hover */
        }

        /* Styling for icons within the custom buttons - REMOVED as icons are no longer used */
        /* .custom-button i {
            margin-right: 12px;
            font-size: 1.2em;
            color: #555;
        } */

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

# Define buttons with their URLs (icons removed)
# Each entry is a dictionary containing only the URL
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

# Add a search input field
# The key ensures Streamlit treats this widget uniquely across reruns
search_query = st.text_input("Search applications...", "", key="search_input")

# Filter the URLs based on the search query
# Convert both the button name and the search query to lowercase for case-insensitive matching
filtered_urls = {
    name: data for name, data in all_urls.items()
    if search_query.lower() in name.lower()
}

# Start the button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Iterate through the filtered URLs and create a custom-styled button for each
if filtered_urls: # Only display buttons if there are any matching the search
    for name, data in filtered_urls.items():
        url = data["url"]
        # Icons are removed, so no 'icon' variable is needed here
        st.markdown(f"""
            <a href="{url}" target="_blank" class="custom-button">
                {name}
            </a>
        """, unsafe_allow_html=True)
else:
    # Display a message if no applications match the search
    st.markdown("<p style='text-align: center; color: #7f8c8d;'>No applications found matching your search.</p>", unsafe_allow_html=True)

# Close the button container
st.markdown('</div>', unsafe_allow_html=True)

# Add a small informative footer
st.markdown("""
    <p class="footer-text">
        Click on any button above to open the respective application in a new tab.
    </p>
""", unsafe_allow_html=True)
