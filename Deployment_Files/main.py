##########  Optimized Model for Deployment ##########
'''
This file loads the optimized model and runs the prediction
'''

# Library Imports
import pickle
import streamlit as st # Version 1.25.0
import pandas as pd # Version 2.0.1
import numpy as np # Version 1.3.0
import seaborn as sns # Version 0.12.2
import matplotlib.pyplot as plt # version 3.6.3
from sklearn.ensemble import GradientBoostingRegressor # Version 1.3.0

# Read in Data
data = pd.read_csv("Data/model_ready.csv.gz", compression = "gzip")

# Load models
house_model = pickle.load(open("Code Library/Models/gb_house_tuned.sav", "rb"))
room_model = pickle.load(open("Code Library/Models/gb_room_tuned.sav", "rb"))

# Load fitted pipelines
house_pipeline = pickle.load(open("Deployment_Files/house_pipeline.sav", "rb"))
room_pipeline = pickle.load(open("Deployment_Files/room_pipeline.sav", "rb"))

# Streamlit Setup
st.header("San Diego Airbnb Price Estimator")
st.caption("Enter information on your property to get a price estimate.")

## Input info for the features - not all 24 features can be inputted so...
number_of_host_listings_feat1 = st.number_input(
    "How many listings does the host have? "
)

property_type_feat2 = st.selectbox(
    "What kind of property is this?",
    tuple(data.property_type.values)
)

room_type_feat3 = st.selectbox(
    "What kind of room is being listed?",
    tuple(data.room_type.values)
)

bathrooms_feat4 = st.number_input(
    "How many bathrooms are listed? "
)
