##########  Optimized Model for Deployment ##########
'''
This file loads the optimized model and runs the prediction
'''

# Library Imports
import pickle
import streamlit as st # Version 1.25.0
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor


# Load models
house_model = pickle.load(open("../Code Library/Models/gb_house_tuned.sav", "rb"))
room_model = pickle.load(open("../Code Library/Models/gb_room_tuned.sav", "rb"))

st.header("Fish Weight Prediction App")
# st.text_input("Enter your Name: ", key="name")
# data = pd.read_csv("fish.csv")

