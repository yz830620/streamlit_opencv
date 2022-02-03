"""
# Opencv app for laplacian and canny
DESC: app for opencv visualizing
user inputs: kernel size
output: show image after user transform
"""
import streamlit as st
import cv2
import numpy as np
from .utils import replace_file_by_upload

def app():
    st.subheader('Opencv laplacian and canny visualizer')
    st.caption('create by Even Pan, Date: 2022/2/4')
    st.markdown('---')
    st.subheader('Laplacian and sable')

    img = cv2.imread('img_source/face-png-42647.png')
    img = replace_file_by_upload(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rep = st.columns(2)

    kernel_size = st.slider('kernel size', 3, 11, 5, 2)

    with rep[0]:
        st.write('origin')
        st.image(img)

    with rep[1]:
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        st.write('Laplacian')
        st.image(laplacian, clamp=True)
    rep = st.columns(2)

    with rep[0]:
        sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=kernel_size)
        st.write('Sobel X')
        st.image(sobel_x, clamp=True)

    with rep[1]:
        sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=kernel_size)
        st.write('Sobel Y')
        st.image(sobel_y, clamp=True)

    st.markdown('---')
    st.subheader('Canny')

    minVal = st.slider('minVal', 0, 255, 100)
    maxVal = st.slider('maxVal', 0, 255, 200)

    rep = st.columns(2)
    with rep[0]:
        st.write('origin')
        st.image(img)

    with rep[1]:
        edge = cv2.Canny(img, minVal, maxVal)
        st.write('Canny')
        st.image(edge, clamp=True)