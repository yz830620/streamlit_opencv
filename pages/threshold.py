"""
# Opencv app for threshold
DESC: app for opencv visualizing
user inputs: threshold value
output: show image after filter by threshold
"""
import streamlit as st
import cv2
import numpy as np
from PIL import Image

def app():
    st.subheader('Opencv threshold visualizer')
    st.caption('create by Even Pan, Date: 2022/2/3')