##########  Optimized Model for Deployment ##########
'''
This pages loads the optimized model, and requires manual entry of data
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
st.set_page_config(page_title="Manual Mode")
st.header("San Diego Airbnb Price Estimator - Manual Mode")
st.caption("This mode asks that you manually enter the following information: ")

## Input info for the features - not all 24 features can be inputted so...
number_of_host_listings_feat1 = st.number_input(
    "How many listings does the host have? "
)

zipcode_feat19 = st.selectbox(
    "What is the zipcode of the listing?",
    tuple(data.zipcode.unique())
)
# Pull median income info based on zipcode selected
## Dictionary of zipcode-income info
zipcode_income_dict = data.set_index("zipcode").to_dict()["median_income_dollars"]
median_income_dollars_feat20 = zipcode_income_dict[int(zipcode_feat19)]

property_type_feat2 = st.selectbox(
    "What kind of property is this?",
    tuple(data.property_type.unique())
)

room_type_feat3 = st.selectbox(
    "Select the type of room/house: ",
    tuple(data.room_type.unique())
)

bathrooms_feat4 = st.number_input(
    "How many bathrooms are listed? "
)

bedrooms_feat5 = st.number_input(
    "How many bedrooms are listed?"
)

price_feat6 = st.number_input(
    "What is the listed price?"
)

# Extract whether the property is a single room or whole house based on selection
property_type_binary_feat21 = "room" if "room" in property_type_feat2.lower() else "house"
# 0/1 Binary value whether listing is private or not
private_feat22 = 1 if "private" in property_type_feat2.lower() or "entire" in property_type_feat2.lower() else 0


# Filter the data based on the selected property type and zipcode
# Average the following features in the data based on the filter conditions
# Use the average to fill in the values

# Find most precise filtering granularity
# First filter by zipcode and house/room
if data.loc[(data["zipcode"] == int(zipcode_feat19)) & 
            (data["property_type_binary"] == property_type_binary_feat21)].shape[0] != 0:
    # Check if filtering by privacy results in some data
    if data.loc[(data["zipcode"] == int(zipcode_feat19)) & 
                (data["property_type_binary"] == str(property_type_binary_feat21)) &
                (data["private"] == int(private_feat22))].shape[0] != 0:
        # Subset data by zipcode, room/house, and privacy
        data_subset = data.loc[
            (data["zipcode"] == int(zipcode_feat19)) & 
            (data["property_type_binary"] == str(property_type_binary_feat21)) &
            (data["private"] == int(private_feat22))
            ]
else:
    data_subset = data.loc[
        (data["zipcode"] == int(zipcode_feat19)) & 
        (data["property_type_binary"] == property_type_binary_feat21)
        ]

min_nights_feat7 = data_subset["minimum_nights"].mean()
max_nights_feat8 = data_subset["maximum_nights"].mean()
minimum_minimum_nights_feat9 = data_subset["minimum_minimum_nights"].mean()
maximum_maximum_nights_feat10 = data_subset["maximum_maximum_nights"].mean()
has_availability_feat11 = data_subset["has_availability"].mode()
availability_30_feat12 = data_subset["availability_30"].mean()
availability_365_feat13 = data_subset["availability_365"].mean()
instant_bookable_feat14 = data_subset["instant_bookable"].mode()
calculated_host_listings_count_feat15 = int(number_of_host_listings_feat1)

## TEMPORARILY Use the mean of these features ##
calculated_host_listings_count_private_rooms_feat16 = data_subset["calculated_host_listings_count_private_rooms"].mean()
calculated_host_listings_count_shared_rooms_feat17 = data_subset["calculated_host_listings_count_shared_rooms"].mean()
reviews_per_month_feat18 = data_subset["reviews_per_month"].mean()
sentiment_feat23 = data_subset["sentiment"].mean()
review_score_weighted_feat24 = data_subset["review_score_weighted"].mean()


# Push all entries into a list
values = [
    number_of_host_listings_feat1, property_type_feat2, room_type_feat3,
    bathrooms_feat4, bedrooms_feat5, price_feat6,
    min_nights_feat7, max_nights_feat8, minimum_minimum_nights_feat9,
    maximum_maximum_nights_feat10, has_availability_feat11,
    availability_30_feat12, availability_365_feat13,
    instant_bookable_feat14, calculated_host_listings_count_feat15,
    calculated_host_listings_count_private_rooms_feat16,
    calculated_host_listings_count_shared_rooms_feat17,
    reviews_per_month_feat18, zipcode_feat19,
    median_income_dollars_feat20, property_type_binary_feat21,
    private_feat22, sentiment_feat23,
    review_score_weighted_feat24
]

column_names = data.columns.tolist()

# Make a dictionary {column_name : [value]}
input_dict = {}
for i in range(0, len(column_names)):
    input_dict[column_names[i]] = values[i]

# Convert input dict to dataframe
input_df = pd.DataFrame(input_dict)

# Prediction Button
if st.button("Price Prediction"):
    # Drop the property types
    listing_data = input_df.drop(columns=["property_type_binary"])

    # Separate input data from target variable
    input_data = listing_data.drop(columns = ["price"])
    target_price = listing_data["price"].values[0]

    # Find the appropriate model - if room, use room model and transformer
    # Else: use house model and transformer
    if input_df["property_type_binary"].values[0] == "room":
        input_transformed = room_pipeline.transform(input_data)
        price_pred = room_model.predict(input_transformed)
    else:
        input_transformed = house_pipeline.transform(input_data)
        price_pred = house_model.predict(input_transformed)
        
    price_pred = round(price_pred[0], 2)
    st.write(f"The predicted price is: ${price_pred}")

    # Print price differences
    price = price_feat6
    price_diff = round(price - price_pred, 2)
    st.write(f"The difference between the listed price and the predicted price is {price_diff}")

    price_diff_percent = round(((price_diff/price) * 100), 2)
    st.write(f"That is a {price_diff_percent}% difference")
