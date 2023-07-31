##########  Optimized Model for Deployment ##########
'''
This file creates the optimized data transformation pipelines and saves it
'''

# Library Imports
import pandas as pd
import numpy as np
import pickle
import scipy.stats as stats
import statsmodels.formula.api as smf
from statsmodels.nonparametric.smoothers_lowess import lowess

from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV, GridSearchCV
from sklearn.pipeline import make_pipeline, Pipeline 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn import set_config
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.ensemble import GradientBoostingRegressor

import warnings
warnings.filterwarnings("ignore")

# Read in data from the previous notebook
clean_data = pd.read_csv("Data/model_ready.csv.gz", compression = "gzip")
print("Data read in!")

print("Cleaning Data...")
# Change some features to the proper data types
# i.e. zipcode to categorical
clean_data["zipcode"] = clean_data["zipcode"].astype("category")

# Split the data by property type
house_df = clean_data.loc[clean_data["property_type_binary"] == "house"]
room_df = clean_data.loc[clean_data["property_type_binary"] == "room"]

# Drop the property types
house_df = house_df.drop(columns=['property_type_binary'])
room_df = room_df.drop(columns=['property_type_binary'])

# Separate numerical and categorical features
num_cols = house_df.select_dtypes(["int64", "float64"]).columns.tolist()
categorical_cols = house_df.select_dtypes("object").columns.tolist()

# Separate out the target
num_cols.remove('price')

# Set up separate pipelines for different datatypes

# Set transformer output as a pandas dataframe
set_config(transform_output="pandas")

# Numerical Pipeline
num_pipeline = Pipeline([
    ("standardscaler", StandardScaler())
])

# Categorical Pipeline
categorical_pipeline = Pipeline([
    # Handle_unknown = "ignore" to deal with one off values in categorical features
    ("encoder", OneHotEncoder(
        sparse_output = False, drop = "if_binary", handle_unknown = "ignore"
        )
    )
])

# Global Data Pipeline
data_transformer = ColumnTransformer(
    transformers = [
        ("numerical", num_pipeline, num_cols),
        ("categorical", categorical_pipeline, categorical_cols)
    ]
)

# A function to output preprocessed, model-ready data using the data_transformer
def preprocess_data(data_set, pipeline = data_transformer,
                    num_cols = num_cols, categorical_cols = categorical_cols):
    
    # Data partitioning 75:25 Train-Test Split
    training_data, testing_data = train_test_split(
        data_set, test_size = 0.25, random_state = 2023
        )
    
    # Separate target from df
    training_data_X = training_data.drop(columns = ['price'])
    train_data_y = training_data['price']

    testing_data_X = testing_data.drop(columns = ['price'])
    test_data_y = testing_data['price']

    # Fit and transform the training data partition
    trained_pipeline = pipeline.fit(training_data_X)
    train_data_X = pipeline.transform(training_data_X)        

    # Transform the test data set based on the training data
    test_data_X = pipeline.transform(testing_data_X)

    # Remove whitespace in col names
    train_data_X.columns = train_data_X.columns.str.replace(' ', '_')
    test_data_X.columns = test_data_X.columns.str.replace(' ', '_')

    # Remove slashes in col names
    train_data_X.columns = train_data_X.columns.str.replace('/', '_')
    test_data_X.columns = test_data_X.columns.str.replace('/', '_')

    return train_data_X, train_data_y, test_data_X, test_data_y, trained_pipeline

print("Preprocessing Data...")
# Preprocess the house-type and room-type data sets
house_train_X, house_train_y, house_test_X, house_test_y, house_pipeline = preprocess_data(house_df)
room_train_X, room_train_y, room_test_X, room_test_y, room_pipeline = preprocess_data(room_df)
print("Data Processed!")

print("Exporting Pipelines...")
# Export trained pipeline
pickle.dump(house_pipeline, open("Deployment_Files/house_pipeline.sav", "wb"))
pickle.dump(room_pipeline, open("Deployment_Files/room_pipeline.sav", "wb"))
print("All Done!")