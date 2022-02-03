import streamlit as st
import numpy as np
import cv2
from PIL import Image
    
def replace_file_by_upload(img):
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", 'png'])
    if uploaded_file:
        st.write('upload successed')
        image = np.array(Image.open(uploaded_file))
        st.image(image, width=200)
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return img