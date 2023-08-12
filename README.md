# ADS-599 Capstone Project
_USD ADS-599 Capstone Project Summer 2023 by Hunter Blum, Kyle Esteban Dalope, and Nicholas Lee_

## Overview
<img src="https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Images/fairbnb_logo.png" align="left" width="200px"/>
This study aimed to create a web application, aptly named <i>Fairbnb</i>, powered by a transparent machine learning algorithm, that could create a fair estimate of Airbnb prices in San Diego, CA. The web application can be found [here](https://fairbnb.streamlit.app/). To use the application, the user can either enter an Airbnb URL in URL mode or manually enter the required information for price predicting in Manual mode.

<br clear="left"/>
</br>

_Application Home Page_

<p align="center">
  <img src="https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Images/Fairbnb_Home_Page3.png" />
</p>

## Repository Contents
[_Code Library Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Code%20Library)
- This folder contains the jupyter notebooks, ordered sequentially, utilized to produce the final output. The details of the notebooks are as follows:
  
    1. [_Data Exploration_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/1_Data_Exploration.ipynb)
      - This notebook contains preliminary data exploration and data preparation steps, including: data importation, data deduplication, descriptive statistics, early feature removal, feature engineering, missing data imputation, univariate and bivariate data analysis, outlier detection, feature correlation, and geospatial feature exploration. 
    2. [_Cleaning and Engineering_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/2_Cleaning_Engineering.ipynb)
      - This notebook goes further in-depth on feature engineering, missing data handling, and dimensionality reduction. A sentiment feature is derived from the text-based review feature. Every missing value is handled either by imputation based on logic, imputation by manual assessment, or removal. Feature data types are also assessed; and, unnecessary features are removed.
    3. [_Modeling_](https://github.com/nlee98/ADS-599_Capstone_Project/blob/main/Code%20Library/3_Modeling.ipynb)
      - This notebook contains our data splitting and preprocessing pipeline. After splitting, the notebook explores 16 different models (eight for homes and eight for rooms). The models were then evaluated using adjusted r-squared, root mean square error, and mean absolute error. Finally, the important features of the best models, the gradient boosting regressions, were plotted.
    4. [_Models Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Code%20Library/Models)
      - This folder contains all of the pickled models from the previous notebook.
    5. [_Presentation_plots_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Code%20Library/Presentation_plots)
      - This folder contains a copy of the three main notebooks, however, plots are adjusted to match our presentation theme. 

[_Documents Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Documents)
- The documents folder contains the article and presentation for this project.

[_Data Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Data)
- The data folder contains the raw data from [Inside Airbnb](http://insideairbnb.com/get-the-data/) utilized for this project, as well as other files needed during EDA, feature engineering, and check points (such as geojson files, U.S. Census data, and compressed CSV data frame outputs).
  -  2022_06_june_listings.csv.gz - Raw Airbnb data for San Diego, CA from June 2022 sourced from Inside Airbnb.
  -  2022_09_sept_listings.csv.gz - Raw Airbnb data for San Diego, CA from September 2022 sourced from Inside Airbnb.
  -  2022_12_dec_listings.csv.gz - Raw Airbnb data for San Diego, CA from December 2022 sourced from Inside Airbnb.
  -  2023_03_mar_listings.csv.gz - Raw Airbnb data for San Diego, CA from March 2023 sourced from Inside Airbnb.
  -  raw_combined.csv.gz - Combined data from the above four data frames, only keeping the most recent observation from each property. Created in 1_Data_Exploration.
  -  eda.csv.gz - Data frame from the end results of EDA. Includes new features such as zip code and removed features that had high correlation. Created in 1_Data_Exploration.
  -  sentiment.csv.gz - Data frame including the sentiment-based feature. Created in 2_Cleaning_Engineering.
  -  app_df.csv.gz - Data frame used by the application to look up property data. Created in 2_Cleaning_Engineering.
  -  clean_df.csv.gz - Data frame created after final feature removal. Created in 2_Cleaning_Engineering.
  -  model_ready.csv.gz - Data frame created after imputing missing values. Created in 2_Cleaning_Engineering.
  -  SanDiego5Y2021_IncomeData.csv - Data frame used to create median income feature. Sourced from https://data.census.gov/.
  -  SDZips.geojson - Data used to create zip code borders for maps in 1_Data_Exploration. Sourced from https://sdgis-sandag.opendata.arcgis.com/datasets/SANDAG::zip-code/explore.
  -  Inside Airbnb Data Dictionary - listings.csv detail v4.3.csv - Data dictionary for the raw data. Sourced from Inside Airbnb.


[_Deployment Files Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Deployment_Files)
- The Deployment Files folder contains all the files necessary for establishing the Streamlit application. The file _main.py_ is the primary, foundational file, which establishes the home page for the application. The subfolder _pages_ contains three python files that power each of the corresponding pages on the application.

[_.streamlit Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/.streamlit)
- Contains the config.toml file used to set the theme for the application.

[_images Folder_](https://github.com/nlee98/ADS-599_Capstone_Project/tree/main/Images)
- Contains images used for the README.
