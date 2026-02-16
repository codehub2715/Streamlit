import streamlit as st
from PIL import Image

img = st.file_uploader('Upload Image', type=['jpg','png'])
if img:
    image = Image.open(img)
    st.image(image, caption='Uploaded Image')