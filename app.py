import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import color_selector, border

# Create an instance of the app 
app = MultiPage()
# Title of the main page
st.title("OpenCV practice")

# Add all your applications (pages) here
app.add_page("color selector", color_selector.app)
app.add_page("border fill", border.app)

# The main app
app.run()