import streamlit as st

st.header("Construction on progress")

st.subheader("Cusomized page to get updated with the list of interest things.")

# st.write(
#         f'<iframe src="https://merolagani.com/" style="margin:5%;width:90%;height:800px;"></iframe>',
#         unsafe_allow_html=True,
#     )

# st.write(
#         f"""
#         <style>
#         [data-testid="stHorizontalBlock"]:has(div.PortMarker) [data-testid="stMarkdownContainer"] p { 
#             margin: 0px 0px 0.2rem; 
#             color: #ff0000;
#         }   
#         </style>
#         <p>This is content from <span id="temp" style="font-weight:bold;cursor:pointer;">Merolagani</span></p>
#         """,
#         unsafe_allow_html=True,
#     )

st.write('''<style>
[data-testid="stHorizontalBlock"]:has(div.PortMarker) [data-testid="stMarkdownContainer"] p { 
    margin: 0px 0px 0.2rem; 
    color: #ff0000;
}        
</style>''', unsafe_allow_html=True)

with st.container():
    INcol1, INcol2 = st.columns(2) 
    with INcol1:
            st.write('Test 1')
            st.write("""<div class='PortMarker'/>""", unsafe_allow_html=True)
    with INcol2:
            st.write('Test 2')
