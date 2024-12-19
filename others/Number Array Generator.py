import streamlit as st
import numpy as np

def get_random_num(dim):
    return np.random.randn(dim)

st.header("Generate the array for variable")

st.subheader("-- Currently work on progress --")

st.number_input("Dimension", key="_dim", min_value=1, value=1, step=1)

if st.session_state["_dim"]:
    dim = st.session_state["_dim"]

    for ind, dim_range in enumerate(range(int(dim))):
        st.number_input(f'{ind+1} - Dim', key=f'dim{ind+1}', min_value=1, step=1, value=1)

if st.button("Generate"):
    nums = 50 * np.random.rand(20, 20) + 1

    for i, rows in enumerate(nums):
        for j, item in enumerate(rows):
            nums[i][j] = int(item)
        

    st.write(str(nums))
    # st.write(st.session_state)
    # st.text(get_random_num())


