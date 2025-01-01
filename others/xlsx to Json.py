import json
import pandas as pd
import streamlit as st
import os

st.header("xlsx to JSON")

input_file = st.file_uploader("excel file", type="xlsx", key="input_file")

if st.session_state["input_file"]:
    xlsx_file = pd.read_excel(st.session_state["input_file"])
    json_dump = xlsx_file.to_json(orient='records', indent=4)
    print(json_dump)

    st.write("Preview")
    st.json(json_dump)
    with open("temp.json", "w") as nf:
        nf.write(str(json_dump))
    st.divider()

    downloadable = open("temp.json", "rb").read()
    st.download_button("Download", data=downloadable, file_name="object.json")

