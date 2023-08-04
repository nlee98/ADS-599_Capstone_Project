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
        Page("main.py", "Home", "🏠"),
        Page("pages/url_mode.py", "URL Mode"),
        Page("pages/manual_mode.py", "Manual Mode", "✏️")
    ]
)

# Streamlit Setup
st.header("Fairbnb: A San Diego Airbnb Price Fairness Estimator")

st.markdown("""
    Welcome to our application for predicting Airbnb prices in San Diego, California. 
""")

st.markdown("""
    This application has two modes: URL Mode and Manual Mode.
         
            
    - In URL Mode, you can simply copy and paste the URL of an Airbnb listing of interest, enter the listed price,
    and click _Price Prediction_ to get a price estimate.
    
            
    - In Manual Mode, you can manually enter some data regarding the property and the lister to get a price estimate.
""")