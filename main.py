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


# create the st.Page for the files inside given path
def get_files_stpage(path, files : list) -> list:
    temp = []
    for file in files:
        # print(os.path.join(path, file))
        page = st.Page(
            os.path.join(path, file),
            title=file.split(".")[0],
            icon="📃"
        )
        temp.append(page)
    return temp

st.set_page_config(
    page_title="Utility App",
    page_icon="😃",
    # initial_sidebar_state='collapsed'
)

st.sidebar.success("Select a page above.")


more_page_dir = os.path.join("dirs")
page_dir = os.path.join("others")
pages_dict = {}
pages_dict["Home"] = [st.Page("landing.py", title="Landing", icon="❤️", default=True)]

dirs = get_dirs(more_page_dir, os.path.isdir)
for dir in dirs:
    files = get_dirs(os.path.join(more_page_dir, dir), is_py_file)
    st_pages = get_files_stpage(os.path.join(more_page_dir, dir), files)
    pages_dict[dir] = st_pages


files = [file for file in os.listdir(page_dir) if file not in dirs]
st_pages = get_files_stpage(os.path.join(page_dir), files)
pages_dict["Others"] = st_pages

app = st.navigation(pages_dict)
app.run()
