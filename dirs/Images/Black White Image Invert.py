import streamlit as st

import numpy as np
import cv2
from PIL import Image
import os

MAX = 255

st.title("Black And White Image Inverter")

input_file = st.file_uploader("Image", key="input_file", type=["png", "jpg", "jpeg"])

st.divider()
if st.session_state["input_file"]:
    st.subheader("Preview")
    pil_image = Image.open(st.session_state["input_file"])
    im = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2GRAY)
    img = np.array(im)
    img = MAX - img
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # if st.button("Save"):

    #     if os.path.exists("bwinvert"):
    #         pass
    #     else:
    #         os.mkdir("bwinvert")

        
    #     path = os.path.join("bwinvert", "invert.png")
    #     cv2.imwrite(path, img)
    #     st.success("Saved in folder : " + path)

    cv2.imwrite("temp.png", img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="invert.png")
