import streamlit as st

import numpy as np
import cv2
from PIL import Image

st.title("Image Resize")

input_file = st.file_uploader("Image", key="input_file", type=["png", "jpg", "jpeg"])
scale_factor = st.slider("Scale Factor", key="scale_factor", min_value=0.1, max_value=4.0, step=0.1, value=1.0)

st.divider()
if st.session_state["input_file"]:
    st.subheader("Preview")
    pil_image = Image.open(st.session_state["input_file"])
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    factor = st.session_state["scale_factor"]
    curr_width, curr_height = img.shape[1], img.shape[0]
    img = cv2.resize(img, (int(curr_width * factor), int(curr_height * factor)), interpolation=cv2.INTER_CUBIC)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    cv2.imwrite("temp.png", img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="resize.png")
