"""
# My opencv app border fill
DESC: app for opencv visualizing
user inputs: R, G, B
output: show color user selector by RGB
"""
import io
import streamlit as st
import cv2
import numpy as np
from tempfile import NamedTemporaryFile
from PIL import Image


def app():
    st.subheader('Opencv color seletor')
    st.caption('create by Even Pan, Date: 2022/2/2')
    
    method_dict = {
        'constant': cv2.BORDER_CONSTANT,
        'reflect': cv2.BORDER_REFLECT,
        'reflect_101': cv2.BORDER_REFLECT_101,
        'replicate': cv2.BORDER_REPLICATE,
        'wrap': cv2.BORDER_WRAP
        }
    

    img = cv2.imread('img_source/face-png-42647.png')
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", 'png'])
    
    if uploaded_file:
        st.write('upload successed')
        image = np.array(Image.open(uploaded_file))
        st.image(image, width=200)
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        # st.image(image_boxed)


    res = st.columns(3)
    BORDER_PX = st.slider('how many pixel to show in border', min_value=10, max_value=200, value=70)

    with res[0]:
        st.write('origin')
        st.image(img, clamp=True, channels='BGR')

    for idx, key in enumerate(list(method_dict.keys())[:2]):
        with res[idx+1]:
            if key == 'constant':
                transformed_img = cv2.copyMakeBorder(img, BORDER_PX,BORDER_PX,BORDER_PX,BORDER_PX, method_dict[key], value=[255,0,0])
            else:
                transformed_img = cv2.copyMakeBorder(img, BORDER_PX,BORDER_PX,BORDER_PX,BORDER_PX, method_dict[key])
            st.write(key)
            st.image(transformed_img, channels='BGR')

    rep = st.columns(3)

    for idx, key in enumerate(list(method_dict.keys())[2:]):
        with rep[idx]:
            transformed_img = cv2.copyMakeBorder(img, BORDER_PX,BORDER_PX,BORDER_PX,BORDER_PX, method_dict[key])
            st.write(key)
            st.image(transformed_img, channels='BGR')