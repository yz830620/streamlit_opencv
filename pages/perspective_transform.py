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

    img = cv2.imread('img_source/poker.jpeg')
    img = replace_file_by_upload(img)

    rows, cols, c = img.shape

    res1, res2, res3 = st.columns(3)
    with res1:
        src_pt1_x = st.slider('src_pt1_x',0.0,1.0, 0.48, step=0.01)
        src_pt1_y = st.slider('src_pt1_y',0.0,1.0, 0.3, step=0.01)
    with res2:
        src_pt2_x = st.slider('src_pt2_x',0.0,1.0, 0.68, step=0.01)
        src_pt2_y = st.slider('src_pt2_y',0.0,1.0, 0.36, step=0.01)
    with res3:
        src_pt3_x = st.slider('src_pt3_x',0.0,1.0, 0.34, step=0.01)
        src_pt3_y = st.slider('src_pt3_y',0.0,1.0, 0.62, step=0.01)

    res1, res2, res3 = st.columns(3)
    with res1:
        dst_pt1_x = st.slider('dst_pt1_x',0.0,1.0, 0.20,step=0.01)
        dst_pt1_y = st.slider('dst_pt1_y',0.0,1.0, 0.20,step=0.01)
    with res2:
        dst_pt2_x = st.slider('dst_pt2_x',0.0,1.0, 0.45,step=0.01)
        dst_pt2_y = st.slider('dst_pt2_y',0.0,1.0, 0.20,step=0.01)
    with res3:
        dst_pt3_x = st.slider('dst_pt3_x',0.0,1.0, 0.21,step=0.01)
        dst_pt3_y = st.slider('dst_pt3_y',0.0,1.0, 0.75,step=0.01)

    points_src = ([[int(src_pt1_x*cols), int(src_pt1_y*rows)],
                  [int(src_pt2_x*cols), int(src_pt2_y*rows)],
                  [int(src_pt3_x*cols), int(src_pt3_y*rows)]])
                  
    points_dsc = [[int(dst_pt1_x*cols), int(dst_pt1_y*rows)],
                  [int(dst_pt2_x*cols), int(dst_pt2_y*rows)],
                  [int(dst_pt3_x*cols), int(dst_pt3_y*rows)]]

    st.write('origin')
    for pt in points_src:
        img = cv2.circle(img, pt, 5, [0,255,0], 5)
    st.image(img, channels='BGR')

    M1 = cv2.getAffineTransform(np.float32(points_src), np.float32(points_dsc))
    dst_transform = cv2.warpAffine(img, M1, (cols,rows))
    st.image(dst_transform, channels='BGR')
