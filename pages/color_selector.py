"""
# My opencv app color selector
DESC: app for opencv visualizing
user inputs: R, G, B
output: show color user selector by RGB
"""
import streamlit as st
import cv2
import numpy as np


def app():
    st.subheader('Opencv color seletor')
    st.caption('create by Even Pan, Date: 2022/2/2')


    img = np.zeros((300, 512, 3), np.int8)

    R = st.slider('Red', min_value=0, max_value=255, value=0)
    G = st.slider('Green', min_value=0, max_value=255, value=0)
    B = st.slider('Blue', min_value=0, max_value=255, value=0)

    st.write(f"Red: `{R}`; Green: `{G}`; Blue: `{B}`")
    img[:] = [B//2, G//2, R//2]
    cv2.imwrite('cache/temp.jpg', img)
    st.image('cache/temp.jpg', clamp=True, channels='BGR')
