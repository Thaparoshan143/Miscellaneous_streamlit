import cv2
import numpy as np
import streamlit as st
import colorsys
from PIL import Image
from sklearn.cluster import KMeans
from streamlit_image_coordinates import streamlit_image_coordinates

UINT_MAX = (1 << 8) - 1
HUE_MAX = 179 # this in actual case is 360 but, cv2 uses 0-179 format for 8-bit representation
SAT_MAX = 255 # saturation max in cv2
VALUE_MAX = 255 # value max in cv2

def hex_to_hsv(hex_col):
    """
    Converts a hexadecimal color code to HSV.

    Args:
        hex_color (str): The hexadecimal color string (e.g., '#RRGGBB' or 'RRGGBB').

    Returns:
        tuple: A tuple containing the H, S, V values [range are cv2 based, H[0-179], S & V [0-255]]
    """
    hex_col = hex_col.lstrip('#')

    r_int = int(hex_col[0:2], 16)
    g_int = int(hex_col[2:4], 16)
    b_int = int(hex_col[4:6], 16)

    h_norm, s_norm, v_norm = colorsys.rgb_to_hsv(r_int/255, g_int/255, b_int/255) # expected in normalized rgb form.. so

    return (h_norm * HUE_MAX, s_norm * SAT_MAX, v_norm * VALUE_MAX)


def pixel_iterator(img, op_cb, **kwargs):
    """
    For given image iterator over each pixel and invoke callback to assign result
    #Warning: the result will be stored in same image
    """

    # h_vals = []
    h_ref = kwargs["h_ref"]
    h_off = kwargs["h_off"] 
    hsv_rep = kwargs["hsv_rep"]

    for x, row in enumerate(img):
        for y, pix in enumerate(row):
            img[x][y] = op_cb(pixel=pix, h_ref=h_ref, h_off=h_off, hsv_rep=hsv_rep)
            # h_vals.append(pix[0])

    # print(np.unique(np.array(h_vals)))

def within_range(val, ref, off):
    return val > ref-off and val < ref+off

def hue_op(**kwargs):

    h, s, v = kwargs["pixel"]
    h_ref = kwargs["h_ref"]
    h_off = kwargs["h_off"] 
    hsv_rep = kwargs["hsv_rep"] # replacing value

    if not h_ref or not h_off:
        st.text("Unknown ref or offset value")
        return

    if within_range(h, h_ref, h_off):
        h, s, v = hsv_rep[0], s, v # currently only replacing hue with same S & V

    return (h, s, v)

st.title("HUE based color changer")

c1, c2 = st.columns(2)
with c1:
    input_file = st.file_uploader("Image", key="input_file", type=["png", "jpg", "jpeg"])
with c2:
    h_offset = st.slider("HUE offset range", key="clip_tol", min_value=1, max_value=127, step=1, value=10)


st.divider()
if st.session_state["input_file"]:
    c1, c2 = st.columns(2)
    pil_image = Image.open(st.session_state["input_file"])
    hsv_img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2HSV)

    with c1:
        st.subheader("Click anywhere on the image to pick color")
        # Display image and capture coordinates
        # We use use_column_width=True to make it responsive
        value = streamlit_image_coordinates(pil_image, key="pil")

    with c2:
        if value:
            x, y = value["x"], value["y"]
            
            rgb = pil_image.getpixel((x, y))
            hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb)
            hsv_col = hex_to_hsv(hex_color)

            st.subheader("Picked Color")
            
            st.markdown(
                f'<div style="background-color:{hex_color}; width:150px; height:100px; border-radius:10px; border:2px solid #ddd;"></div>',
                unsafe_allow_html=True
            )
            
            st.write(f"**HEX:** `{hex_color.upper()} ` || **RGB:** `{rgb}` || **Coordinates:** `x={x}, y={y}`")
            
            st.color_picker("Fine-tune color", value=hex_color)

            st.divider()

            replacing_col_hex = st.color_picker("Replacing Color (HUE only used):", value="#ffffff")
            hsv_replace = hex_to_hsv(replacing_col_hex)

            result = hsv_img.copy()

            pixel_iterator(result, hue_op, h_ref=hsv_col[0], h_off=h_offset, hsv_rep=hsv_replace)

            st.image(cv2.cvtColor(result, cv2.COLOR_HSV2RGB))

            cv2.imwrite("temp.png", result)
            downloadable = open("temp.png", "rb").read()
            st.download_button("Download", data=downloadable, file_name="result.png")

        else:
            st.info("Click the image to see the color details.")




