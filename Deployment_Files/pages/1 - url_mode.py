##########  URL Mode for Predictions ##########
'''
This pages lets the user paste an Airbnb URL and predicts the price based on if the url exists in the data base
'''

# Library Imports
import pickle
import streamlit as st # Version 1.25.0
import pandas as pd # Version 2.0.1
import numpy as np # Version 1.3.0
import seaborn as sns # Version 0.12.2
import matplotlib.pyplot as plt # version 3.6.3
from sklearn.ensemble import GradientBoostingRegressor # Version 1.3.0
import re

# Read in Data
model_data = pd.read_csv("Data/model_ready.csv.gz", compression = "gzip")
url_df = pd.read_csv("Data/raw_combined.csv.gz", compression="gzip")

# Load models
house_model = pickle.load(open("Code Library/Models/gb_house_tuned.sav", "rb"))
room_model = pickle.load(open("Code Library/Models/gb_room_tuned.sav", "rb"))

# Load fitted pipelines
house_pipeline = pickle.load(open("Deployment_Files/house_pipeline.sav", "rb"))
room_pipeline = pickle.load(open("Deployment_Files/room_pipeline.sav", "rb"))

# Streamlit Setup
st.header("San Diego Airbnb Price Estimator - URL Mode")
st.caption("""This mode will pull the necessary information for predicting 
        the price based on a provided Airbnb URL.
    """)

# URL Field
url = st.text_input(
    "Enter an Airbnb URL: "
)

# Listed Price
price = st.number_input(
    "What is the listed nightly price? "
)

# Clean url to match dataframe url
clean_url = re.match(r"[\w\W]*\?", str(url)).group(0).strip()[:-1]