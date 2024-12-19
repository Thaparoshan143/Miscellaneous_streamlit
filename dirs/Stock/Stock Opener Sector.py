import streamlit as st
import json
import webbrowser
import os

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

def get_scripts(path):
    with open(path, "r") as nf:
        sectorListDict = json.load(nf)
        return sectorListDict

curPath = os.getcwd() + "/dirs/Stock/"
sectors_scripts = get_scripts(curPath + "scripts.json")
sectors = [item for item in sectors_scripts]
active_sectors_scripts = []

def get_scripts_of_sector(sector : str):
    scripts = sectors_scripts[sector.upper()]
    return scripts




def ui():
    st.title("Stock Utility")
    st.text("This is work only with the M1 mac machine! change browser cmd for other machine")

    if st.button("Open Script", on_click=update_sectors):
        st.write("Opening, SCRIPTS : " + ", ".join(active_sectors_scripts))
        browser = browser_cmd[browser_choice]
        st.write("URL : " + urls[urls_choice] + " || From : " + urls_choice)
        st.write("Browser path : " + browser + " || From : " + browser_choice)
        for script in active_sectors_scripts:
            url = urls[urls_choice] + script
            webbrowser.get(browser).open(url)


def update_active_scripts(scripts : list):
    for script in scripts:
        if script['Symbol'] not in active_sectors_scripts:
            active_sectors_scripts.append(script['Symbol'])



def update_sectors():
    ui()
    st.divider()

    active_sectors = st.session_state['active_sectors']
    st.set_page_config(layout="wide")
    col1, col2, col3 = st.columns(3)

    for index, sector in enumerate(active_sectors):
        sector_scripts = get_scripts_of_sector(sector)
        update_active_scripts(sector_scripts)
        if index % 3 == 0:
            col = col1
        elif index % 3 == 1:
            col = col2
        else:
            col = col3

        col.write(str(index+1) + ". " + sector)
        col.table(sector_scripts)

sectors_choice = st.multiselect("SECTORS", options=sectors, on_change=update_sectors, key="active_sectors")
# urls_choice = st.multiselect("URLS", options=[key for key in urls], on_change=update_sectors, key="active_urls")
urls_choice = st.selectbox("URLS", options=[key for key in urls], index=2, on_change=update_sectors, key="active_urls")
#browser_choice = st.multiselect("Browser", options=[key.upper() for key in browser_cmd])
browser_choice = st.selectbox("BROWSERS", options=[key.upper() for key in browser_cmd])

