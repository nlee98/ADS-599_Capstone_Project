# Libraries
import streamlit as st
from PIL import Image

# Streamlit page stuff
st.header("About Us:")

st.markdown("""
    This project was completed by Hunter Blum, Kyle Esteban Dalope, and Nicholas Lee.
    The project served as the capstone for the University of San Diego's M.S. in Applied Data Science.
    To access our code and article, please visit the projects GitHub page at https://github.com/nlee98/ADS-599_Capstone_Project.
    
""")

st.header("About the Model:")


st.markdown("""
    We used two models to create our predictions, one based on entire homes and the other on single rooms.
    Each model is a gradient boosted regressor.
    The models work by starting with a "decision tree."
    This tree usually doesn't create the most accurate predictions,
    so build a new tree that tries to correct the old tree's errors (this is boosting!)
    We keep repeating this process until we create a pre-determined number of trees.
    Each of our trees will get a weighted vote based on its accuracy, and these votes are combined to generate our final prediction!
    Below is a brief overview of the important features in both of our models.   
""")

house_path = 'images/house.png'
room_path = 'images/room.png'

st.image(house_path)
st.image(room_path)