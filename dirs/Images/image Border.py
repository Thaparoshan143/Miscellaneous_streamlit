import streamlit as st

import numpy as np
import cv2
from PIL import Image
from math import floor

def hex2rgb(h : str):
    h = h.lstrip("#")
    return list(int(h[i:i+2], 16) for i in (0, 2, 4))

st.title("Image Border")

input_file = st.file_uploader("Images", key="input_file", type=["png", "jpg", "jpeg"])
border_color = st.color_picker("Border Color", value="#ffffff")
border_width = st.number_input("Border Width", value=0)
border_height = st.number_input("Border Height", value=0)

st.divider()
if st.session_state["input_file"]:
    st.subheader("Preview")

    pil_image = Image.open(st.session_state["input_file"])
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGRA)

    img = cv2.copyMakeBorder(cv2.cvtColor(img, cv2.COLOR_RGB2BGR), border_height, border_height, border_width, border_width, cv2.BORDER_CONSTANT, value=hex2rgb(border_color)) 

    st.image(img)

    cv2.imwrite("temp.png", img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="border.png")

