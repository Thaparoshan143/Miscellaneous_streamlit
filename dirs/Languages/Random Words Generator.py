import streamlit as st
import random

def get_random_word(count) -> str:
    word = ""
    for index in range(count):
        word += chr(random.randint(65, 90) if random.randint(0, 1) == 0 else random.randint(97, 122))
    return word

def get_random_words(word_count : int) -> str:
    word_range = st.session_state['word_count_range']
    passage = ""
    for index in range(word_count):
        word = get_random_word(random.randint(word_range[0], word_range[-1]))
        passage += " " + word
    return passage

st.title("Random Words/Passage Generator")

text_count = st.number_input("Word Count", key="word_count", value=100, min_value=0, step=1)
word_len_range = st.slider("Word char count range", min_value=1, max_value=15, step=1, value=[5, 12], key="word_count_range")

if st.button("Generate"):
    st.divider()
    st.subheader("Output")
    st.text(get_random_words(st.session_state["word_count"]))