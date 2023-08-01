##########  Optimized Model for Deployment ##########
'''
This file is the home page for the application
'''

# Library Imports
import streamlit as st # Version 1.25.0

# Streamlit Setup
st.header("San Diego Airbnb Price Estimator")

st.markdown("""
    Welcome to our application for predicting Airbnb prices in San Diego, California. 
""")

st.write("""\n\tThis application has two mode: URL Mode and Manual Mode.
         In URL Mode, you can simply copy and paste the URL of an Airbnb listing of interest, enter the listed price,
         and click _Price Prediction_ to get a price estimate
         """)