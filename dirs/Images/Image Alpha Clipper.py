import streamlit as st
import cv2 
import numpy as np
from PIL import Image

def hex_to_rgb(hex) -> list:
    h = hex.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

st.title("Image Alpha Clipper")

input_color = st.color_picker("Pick color to clip", value="#ffffff")
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"""#### RGB
                    {hex_to_rgb(input_color)}""")
with c2:
    st.markdown(f"""#### HEX
                    {input_color}""")

input_file = st.file_uploader("Image", key="input_file", type=["png", "jpg", "jpeg"])
clip_tol = st.slider("Tolerance", key="clip_tol", min_value=0.1, max_value=1.0, step=0.01, value=0.75)

st.divider()
if st.session_state["input_file"]:
    st.subheader("Preview")
    pil_image = Image.open(st.session_state["input_file"])
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGRA)
    tol_per = st.session_state["clip_tol"]
    img[:,:, -1] = np.where((img[:,:,0]>(255*tol_per)) & (img[:,:,1]>(255*tol_per))  & (img[:,:,2]>(255*tol_per)) , 0, img[:,:, -1])
    st.image(cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA))

    cv2.imwrite("temp.png", img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="clipped.png")

