"""
# Opencv app for morphology
DESC: app for opencv visualizing
user inputs: kernel size
output: show image after user transform
"""
import streamlit as st
import cv2
import numpy as np
from .utils import replace_file_by_upload

def app():
    st.subheader('Opencv morphology visualizer')
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
    with rep[1]:
        erosion = cv2.erode(img, kernel, iterations=1)
        st.write('erosion')
        st.image(erosion)

    with rep[2]:
        dilation = cv2.dilate(img, kernel, iterations=1)
        st.write('dilation')
        st.image(dilation)

    rep = st.columns(3)
    with rep[0]:
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        st.write('opening')
        st.image(opening)

    with rep[1]:
        closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        st.write('closing')
        st.image(closing)

    with rep[2]:
        gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
        st.write('gradient')
        st.image(gradient)

    with rep[0]:
        st.write('origin')
        st.image(img)

    with rep[1]:
        tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
        st.write('tophat')
        st.image(tophat)

    with rep[2]:
        blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
        st.write('blackhat')
        st.image(blackhat)
