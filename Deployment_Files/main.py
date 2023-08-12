##########  Optimized Model for Deployment ##########
'''
This file is the home page for the application
'''

# Library Imports
import streamlit as st # Version 1.25.0
from st_pages import Page, show_pages


# Setup Sidebar
show_pages(
    [
        Page("Deployment_Files/main.py", "Home", "🏠"),
        Page("Deployment_Files/pages/1 - url_mode.py", "URL Mode", "🌐"),
        Page("Deployment_Files/pages/2 - manual_mode.py", "Manual Mode", "✏️"),
        Page("Deployment_Files/pages/3 - about.py", "About", "❓")
    ]
)


# Streamlit Setup
st.header("Fairbnb: A San Diego Airbnb Price Fairness Estimator")

st.markdown("""
    Welcome to our application for predicting Airbnb price fairness in San Diego, California. 
""")

st.markdown("""
    This application has two modes: _URL Mode_ and _Manual Mode_. We recommend trying _URL Mode_ first.
         
            
    - In _URL Mode_, you can simply copy and paste the URL of an Airbnb listing of interest, enter the listed price,
    and click _Price Prediction_ to get a price estimate.
    
            
    - In _Manual Mode_, you can manually enter data regarding the property and host to get a price estimate.
    
    For info about the creators, models, and code, please visit the _About_ section.
""")

# Image at bottom of page
sd_path = 'Deployment_Files/pages/images/SD.jfif'

st.image(sd_path,
         caption= 'Photo by: JIM GRANT sdc')

# Logo in sidebar
logo_path = 'Deployment_Files/pages/images/fairbnb_logo.png'

st.sidebar.image(logo_path, use_column_width=True)

# Logo for page icon
st.set_page_config(page_icon=logo_path)
