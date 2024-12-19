import streamlit as st
import webbrowser

st.title("Bulk Link Opener")


browser_cmd = { 
                "GOOGLE" : "open -a /Applications/Google\ Chrome.app %s",
                "BRAVE" : "open -a /Applications/Brave\ Browser.app %s",
            }

browser_choice = st.selectbox("BROWSERS", options=[key.upper() for key in browser_cmd])
is_google_search = st.checkbox("is google search", value=True)
st.divider()
search_text = st.text_area("URL list", key="search_text", height=300)

if st.button("Search"):
    urls = st.session_state["search_text"].split("\n")
    browser = browser_cmd[browser_choice]
    for url in urls:
        if is_google_search:
            link_url = "https://www.google.com/search?q=" + url
        else:
            link_url = url

        webbrowser.get(browser).open(link_url)
        print(link_url)
    
    st.success("Opened successfully")
    print("Finished")

st.divider()

st.subheader("Open from file")
def update_urls():
    pass

file_urls = st.file_uploader("Open txt file with links", type="txt", key="file_urls", on_change=update_urls)
if st.button("Open & search"):
    urls = str(st.session_state["file_urls"].read(), 'utf-8').split("\n")
    browser = browser_cmd[browser_choice]
    for url in urls:
        if is_google_search:
            link_url = "https://www.google.com/search?q=" + url
        else:
            link_url = url

        webbrowser.get(browser).open(link_url)
        print(link_url)
    
    st.success("Opened successfully")
    print("Finished")
    print("opening")
