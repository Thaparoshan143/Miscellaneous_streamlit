import streamlit as st

import numpy as np
import cv2
from PIL import Image
from math import floor

def hex2rgb(h : str):
    h = h.lstrip("#")
    return list(int(h[i:i+2], 16) for i in (0, 2, 4))


st.title("Multiple Image Combiner")

input_file = st.file_uploader("Images", key="input_files", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
st.radio("Stack Axis", ["Horizontal", "Vertical"], horizontal=True, key="stack_axis")
st.checkbox("Should Resize", key="should_resize")
border_color = st.color_picker("Border Color", value="#ffffff")

st.divider()
if st.session_state["input_files"]:
    st.subheader("Preview")
    img_width_list = []
    img_height_list = []
    np_image_list = []

    for item in st.session_state["input_files"]:
        pil_image = Image.open(item)
        np_image_list.append(np.array(pil_image))
        dim = np_image_list[-1].shape
        img_width_list.append(dim[1])
        img_height_list.append(dim[0])


    min_width = int(max(img_width_list))
    min_height = int(max(img_height_list))
    print("---------------------")
    print("Min height ", min_height)
    print("Min width ", min_width)

    stack_axis = 0 if st.session_state["stack_axis"] == "Vertical" else 1
    should_resize = st.session_state["should_resize"]

    try:
        for ind, img in enumerate(np_image_list):
            if should_resize:
                resize_ratio = min_height/img_height_list[ind] if stack_axis == 1 else min_width/img_width_list[ind]
                # print("Ratio : ", resize_ratio)
                np_image_list[ind] = cv2.resize(img, (int(img_width_list[ind] * resize_ratio), int(img_height_list[ind] * resize_ratio)), interpolation=cv2.INTER_AREA)
            else:
                border_width = int(abs((min_width - img_width_list[ind])/2)) if stack_axis == 0 else 0
                border_height = int(abs((min_height - img_height_list[ind])/2)) if stack_axis == 1 else 0
                # print("Border width : ", border_width)
                # print("Border height : ", border_height)
                # print("Border color : ", hex2rgb(border_color))

                if (int(abs(min_width-img_width_list[ind]))/2).is_integer():
                    np_image_list[ind] = cv2.copyMakeBorder(cv2.cvtColor(np_image_list[ind], cv2.COLOR_RGB2BGR), border_height, border_height, border_width, border_width, cv2.BORDER_CONSTANT, value=hex2rgb(border_color)) 
                else:
                    np_image_list[ind] = cv2.copyMakeBorder(cv2.cvtColor(np_image_list[ind], cv2.COLOR_RGB2BGR), border_height+1, border_height, border_width+1, border_width, cv2.BORDER_CONSTANT, value=hex2rgb(border_color)) 
    except:
        st.error("Incorrect dimension on image or incomptible")

    comb_img = np.concatenate(tuple(np_image_list), axis=stack_axis)
    st.image(comb_img)


    cv2.imwrite("temp.png", comb_img)
    downloadable = open("temp.png", "rb").read()
    st.download_button("Download", data=downloadable, file_name="merge.png")
