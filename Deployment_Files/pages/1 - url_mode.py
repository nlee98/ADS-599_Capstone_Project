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

# Prediction Button
if st.button("Price Prediction"):
    # Clean url to match dataframe url
    clean_url = re.match(r"[\w\W]*\?", url).group(0).strip()[:-1]

    # Check if url is in dataframe:
    if clean_url in url_df["listing_url"].values:
        listing_data = url_df.loc[url_df["listing_url"] == clean_url]
        st.write("URL Found")
    else:
        st.write("The URL was not found in our database. Please use manual mode.")

    '''
    input_species = encoder.transform(np.expand_dims(inp_species, -1))

    inputs = np.expand_dims(
    [int(input_species), input_Length1, input_Length2, input_Length3, input_Height, input_Width], 0)

    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your fish weight is: {np.squeeze(prediction, -1)} Gram")
    '''
