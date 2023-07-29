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


# Load models
house_model = pickle.load(open("../Code Library/Models/gb_house_tuned.sav", "rb"))
room_model = pickle.load(open("../Code Library/Models/gb_room_tuned.sav", "rb"))

st.header("Fish Weight Prediction App")
# st.text_input("Enter your Name: ", key="name")
# data = pd.read_csv("fish.csv")

