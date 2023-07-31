import streamlit as st

def intro():
    import streamlit as st

    st.write("# San Diego Airbnb Pricing App")
    st.sidebar.success("Select a Data Entry Mode")

    st.markdown(
        """
        This application is trained on data provided by Inside Airbnb. 
        For price predictions, use the url from the Airbnb listing of interest. 
    """
    )

def url_mode():
    


def manual_mode():


page_names_to_funcs = {
    "Home Page": intro,
    "URL Mode": url_mode,
    "Manual Demo": manual_mode
}

prediction_page = st.sidebar.selectbox("Choose a Price Prediction Mode", page_names_to_funcs.keys())
page_names_to_funcs[prediction_page]()