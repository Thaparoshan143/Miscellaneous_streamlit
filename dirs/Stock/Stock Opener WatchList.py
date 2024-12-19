import webbrowser
import streamlit as st
import os
import pandas as pd

def get_file_content(fileName) -> list:
    with open(fileName, "r") as nf:
        return [item for item in nf.read().split("\n") if item != ""]

    
def write_file_content(fileName, content : list) -> None:
    with open(fileName, "w") as nf:
        nf.write("\n".join(content))

urls = {    
            "SHARESANSAR" : "https://www.sharesansar.com/company/",
            "MEROLAGANI" : "https://merolagani.com/CompanyDetail.aspx?symbol=",
            "NEPSEALPHA" : "https://nepsealpha.com/trading/chart?symbol=",
            "CHUKUL" : "https://chukul.com/stock-profile?symbol=",
            "NEPALIPAISA" : "https://www.nepalipaisa.com/company/",
            "NEPSETRADING" : "https://www.nepsetrading.com/stock?code="
        }

browser_cmd = { 
                "GOOGLE" : "open -a /Applications/Google\ Chrome.app %s",
                "BRAVE" : "open -a /Applications/Brave\ Browser.app %s",
            }

curPath = os.getcwd() + "/dirs/Stock/"
watchlist_scripts = get_file_content(curPath + "watchlist.txt") 
if "watchlist" not in st.session_state:
    st.session_state["watchlist"] = watchlist_scripts
    # print(st.session_state["watchlist"])
scripts_list = get_file_content(curPath + "scripts.txt")
# print(scripts_list)

def update_watchlist():
    if st.session_state["watchlist"]:
        write_file_content(curPath + "watchlist.txt", st.session_state["watchlist"])
        st.table(pd.DataFrame(st.session_state["watchlist"]))

st.header("Stock Watchlist")

temp = []
st.text_input("Script Name", key="script")

if st.button("Add"):
    script = str(st.session_state["script"]).upper()
    if script not in scripts_list:
        st.error("Script doesnt exist " +  script)
    elif script in st.session_state["watchlist"]:
        st.error("Script already added " +  script)
    elif script and script in scripts_list:
        st.success(script + " Script added to watchlist")
        st.session_state["watchlist"].append(script)
        # print(st.session_state["watchlist"])
    else:
        st.error("Input errror")
    
    update_watchlist()

if st.button("Open Script"):
    browser = browser_cmd["GOOGLE"]
    url = urls["NEPSEALPHA"]
    st.write("URL : " + url)
    st.write("Browser path : " + browser)
    for script in st.session_state["watchlist"]:
        web_url = url + script
        webbrowser.get(browser).open(web_url)



