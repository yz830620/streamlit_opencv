"""
# Opencv app for perspective transform
DESC: app for opencv visualizing
user inputs: 3 points to as src point , 3 points as dst point 
(point include x,y, totally 12 data as user input)
output: show image after user transform
"""
import streamlit as st
import cv2
import numpy as np
from .utils import replace_file_by_upload

def app():
    st.subheader('Opencv perspective transform visualizer')
    st.caption('create by Even Pan, Date: 2022/2/3')

    img = cv2.imread('img_source/face-png-42647.png')
    img = replace_file_by_upload(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rep = st.columns(3)
    with rep[0]:
        st.write('original')
        st.image(img)

    kernel_size = st.slider('kernel size', 3, 21, 5, 2)

    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    with rep[1]:
        st.write('erosion')
        st.image(erosion)

    dilation = cv2.dilate(img, kernel, iterations=1)

    with rep[2]:
        st.write('dilation')
        st.image(dilation)

    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    rep = st.columns(3)
    with rep[0]:
        st.write('opening')
        st.image(opening)

    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    with rep[1]:
        st.write('closing')
        st.image(closing)

    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    with rep[2]:
        st.write('gradient')
        st.image(gradient)

    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    rep = st.columns(2)
    with rep[0]:
        st.write('tophat')
        st.image(tophat)

    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

    with rep[1]:
        st.write('blackhat')
        st.image(blackhat)