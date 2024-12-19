import streamlit as st
import random


st.title("Passage/Sentence word counter")
input_text = st.text_area("Input text", height=400, key="input_text")

if st.button("Count"):
    st.divider()
    st.subheader("Word Count")
    if st.session_state['input_text'] != "":
        st.text(len(str(st.session_state['input_text']).split(" ")))
    else:
        st.text("0")