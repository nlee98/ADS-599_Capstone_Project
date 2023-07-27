#########       App.py file for Flask Application       #########
##  This model begins after notebook two (Cleaning_Engineering.ipynb)   ##

''' 
What the application needs:
- Cleaned Data
- Two trained and optimized models (one per property type) file

'''

# Library and Package Imports
from flask import Flask, request, jsonify, render_template

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, Pipeline 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

import pickle

# Read in Data
clean_data = pd.read_csv(
    "../Data/model_ready.csv.gz", compression = "gzip"
)

# Correct Datatype
clean_data["zipcode"] = clean_data["zipcode"].astype("category")

# Load in saved model objects
house_model = pickle.load(open("templates/housemodel.pkl", "rb"))
room_model = pickle.load(open("templates/room_model.pkl", "rb"))


