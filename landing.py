import streamlit as st
import os.path

def is_py_file(file_name) -> bool:
    return file_name.split(".")[-1] == "py"

# filter is the callback function that recives every items and returns true if to include in list
def get_dirs(path, filter = None) -> list:
    if not filter:
        return os.listdir(path)
    else:
        return [item for item in os.listdir(path) if filter(os.path.join(path, item))]

def display_files(files : list):
    for file in files:
        if is_py_file(file):
            st.markdown("- **" + file.split(".")[0] + "**")


st.markdown("""
            ## Available Operations
            """)


more_page_dir = os.path.join("dirs")
page_dir = os.path.join("others")

dirs = get_dirs(more_page_dir, os.path.isdir)
for dir in dirs:
    st.subheader(dir)
    files = get_dirs(os.path.join(more_page_dir, dir), is_py_file)
    display_files(files)
    st.markdown("")

st.divider()
st.subheader("Others")
files = [file for file in os.listdir(page_dir) if file not in dirs]
display_files(files)
