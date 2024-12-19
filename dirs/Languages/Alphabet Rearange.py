import streamlit as st

st.title("Alphabet Rearanging")

st.subheader("For new line seperator")
col1, col2 = st.columns(2)

def update_sort():
    try:
        sort_text = st.session_state["input_text"].split("\n")
        sort_text.sort()
        col2.text("\n".join(sort_text))
    except:
        pass

input_text = col1.text_area("Input text", height=400, on_change=update_sort, key="input_text")

col2.subheader("Output")
col2.divider()

st.divider()
st.subheader("For custom seperator")
col11, col22 = st.columns(2)

def update_sep_sort():
    try:
        print("Can do ")
        sort_text = st.session_state["input_text_sep"].split(st.session_state["seperator"])
        sort_text.sort()
        col22.text(st.session_state["seperator"].join(sort_text))
    except:
        print("Cannot do it")
        pass

input_text_sep = col11.text_area("Input text", height=400, on_change=update_sep_sort, key="input_text_sep")
seperator = col22.text_input("Seperator", on_change=update_sep_sort, value=", ", key="seperator")
col22.divider()

col22.subheader("Output")
col22.divider()
