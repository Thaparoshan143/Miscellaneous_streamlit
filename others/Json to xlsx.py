import json
import pandas as pd
import streamlit as st
import os

st.header("JSON to xlsx")

input_file = st.file_uploader("Json file", type="json", key="input_file")

if st.button("Extract"):
    st.divider()
    try:
        st.subheader("Output")
        data = json.loads(st.session_state["input_file"].read())
        data_frame = pd.json_normalize(data)
        st.table(data_frame)

        if os.path.exists("xlsx"):
            pass
        else:
            os.mkdir("xlsx")
        path = os.path.join("xlsx", "excel.xlsx")
        data_frame.to_excel(path, index=False)
        st.text("Saved to dir : " + path)
        st.success("File saved successfully")
    except:
        st.error("Invalid operation")