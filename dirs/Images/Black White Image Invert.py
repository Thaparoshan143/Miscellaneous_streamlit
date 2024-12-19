import streamlit as st

import numpy as np
import cv2
from PIL import Image

MAX = 255

st.title("Black And White Image Inverter")

input_file = st.file_uploader("Image", key="input_file", type=["png", "jpg", "jpeg"])

st.divider()
if st.session_state["input_file"]:
    st.subheader("Preview")
    pil_image = Image.open(st.session_state["input_file"])
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2GRAY)
    img = MAX - img
    st.image(img)

    cv2.imwrite("temp.png", img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="invert.png")
