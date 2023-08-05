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
url_df = pd.read_csv("Data/app_df.csv.gz", compression="gzip")

# Load models
house_model = pickle.load(open("Code Library/Models/gb_house_tuned.sav", "rb"))
room_model = pickle.load(open("Code Library/Models/gb_room_tuned.sav", "rb"))

# Load fitted pipelines
house_pipeline = pickle.load(open("Deployment_Files/house_pipeline.sav", "rb"))
room_pipeline = pickle.load(open("Deployment_Files/room_pipeline.sav", "rb"))

# Streamlit Setup
st.set_config_file("config.toml")
st.header("URL Mode")
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

        # Select model features
        listing_data = listing_data[[x for x in listing_data.columns.tolist() if x in model_data.columns.tolist()]]

        # Drop the property types
        input_data = listing_data.drop(columns=["property_type_binary"])

        # Separate input data from target variable
        input_data = listing_data.drop(columns = ["price"])
        target_price = listing_data["price"].values[0]

        # Find the appropriate model - if room, use room model and transformer
        # Else: use house model and transformer
        if listing_data["property_type_binary"].values[0] == "room":
            input_transformed = room_pipeline.transform(input_data)
            price_pred = room_model.predict(input_transformed)
        else:
            input_transformed = house_pipeline.transform(input_data)
            price_pred = house_model.predict(input_transformed)
        
        price_pred = round(price_pred[0], 2)
        st.write(f"The predicted price is: ${price_pred}")

        # Print price differences
        price_diff = round(price - price_pred, 2)
        st.write(f"The difference between the listed price and the predicted price is {price_diff}")

        price_diff_percent = round(((price_diff/price) * 100), 2)
        st.write(f"That is a {price_diff_percent}% difference")

    else:
        st.write("The URL was not found in our database. Please use manual mode.")
