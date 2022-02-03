"""
# Opencv app for threshold
DESC: app for opencv visualizing
user inputs: threshold value
output: show image after filter by threshold
"""
import streamlit as st
import cv2
from .utils import replace_file_by_upload

def app():
    st.subheader('Opencv threshold visualizer')
    st.caption('create by Even Pan, Date: 2022/2/3')

    method_dict = {
        'binary': cv2.THRESH_BINARY,
        'binary inverse': cv2.THRESH_BINARY_INV,
        'truncate': cv2.THRESH_TRUNC,
        'to zero': cv2.THRESH_TOZERO,
        'to zero inverse': cv2.THRESH_TOZERO_INV
        }

    img = cv2.imread('img_source/face-png-42647.png')
    img = replace_file_by_upload(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rep = st.columns(3)
    with rep[0]:
        st.write('original')
        st.image(img)

    threshold = st.slider('threshold value', 0, 255, 127)
    for idx, key in enumerate(list(method_dict.keys())[:2]):
        with rep[idx+1]:
            ret, thresh = cv2.threshold(img, int(threshold), 255, method_dict[key])
            st.write(key)
            st.image(thresh)
    rep = st.columns(3)
    for idx, key in enumerate(list(method_dict.keys())[2:]):
        with rep[idx]:
            ret, thresh = cv2.threshold(img, int(threshold), 255, method_dict[key])
            st.write(key)
            st.image(thresh)

    st.subheader('adaptive Threshold')

    block_size = st.slider('block size', 5, 45, 33, step=2)
    c = st.slider('C', 1, 30, 17)
    
    rep = st.columns(2)
    with rep[0]:
        adapt_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=block_size, C=c)
        st.write('ADAPTIVE_THRESH_MEAN_C')
        st.image(adapt_mean)
    with rep[1]:
        adapt_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize=block_size, C=c)
        st.write('ADAPTIVE_THRESH_GAUSSIAN_C')
        st.image(adapt_gaussian)