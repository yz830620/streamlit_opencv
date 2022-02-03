import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import (color_selector,
                   border,
                   perspective_transform,
                   threshold,
                   morphology,
                   laplacian_canny,
                )

# Create an instance of the app 
app = MultiPage()
# Title of the main page
st.title("OpenCV Visualization")

# Add all your applications (pages) here
app.add_page("laplacian and canny", laplacian_canny.app)
app.add_page("morphology", morphology.app)
app.add_page("threshold", threshold.app)
app.add_page("perspective transform", perspective_transform.app)
app.add_page("color selector", color_selector.app)
app.add_page("border fill", border.app)

# The main app
app.run()