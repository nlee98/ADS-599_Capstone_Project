# ADS-599 Capstone Project
_USD ADS-599 Capstone Project Summer 2023 by Hunter Blum, Kyle Esteban Dalope, and Nicholas Lee_

## Overview

This study aimed to create a web application, powered by a transparent machine learning algorithm, that could create a fair estimate of Airbnb prices in San Diego, CA. The web application can be found [here](https://fairbnb.streamlit.app/). 

## Repository Contents
[_Code Library Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Code%20Library)
- This folder contains the jupyter notebooks, ordered sequentially, utilized to produce the final output. The details of the notebooks are as follows:
  
    1. [_Data Exploration_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/1_Data_Exploration.ipynb)
      - This notebook contains preliminary data exploration and data preparation steps, including: data importation, data deduplication, descriptive statistics, early feature removal, feature engineering, missing data imputation, univariate and bivariate data analysis, outlier detection, feature correlation, and geospatial feature exploration. 
    2. [_Cleaning and Engineering_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/2_Cleaning_Engineering.ipynb)
      - This notebook goes further in-depth on feature engineering, missing data handling, and dimensionality reduction. A sentiment feature is derived from the text-based review feature. Every missing value is handled either by imputation based on logic, imputation by manual assessment, or removal. Feature data types are also assessed; and, unnecessary features are removed.
    3. [_Modeling_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/3_Modeling.ipynb)

[_Data Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Data)
- The data folder contains the raw data from [Inside Airbnb](http://insideairbnb.com/get-the-data/) utilized for this project, as well as other files needed during EDA, feature engineering, and check points (such as geojson files, U.S. Census data, and compressed CSV dataframe outputs).

[_Deployment Files Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Deployment_Files)
- The Deployment Files folder contains all the files necessary for establishing the Streamlit application. The file _main.py_ is the primary, foundational file, which establishes the home page for the application. The subfolder _pages_ contains three python files that power each of the corresponding pages on the application. 
