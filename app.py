import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from homepage import homepage
from manufacturer_page import manufacturer_page
from case_studies_page import case_studies_page
from aboutme import aboutme
from compliance_page import compliance_benefits_page



st.set_page_config(page_title="AI Marketing", page_icon="app-indicator", layout="wide")



@st.cache_data
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_AI = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_y7VH7yWmJE.json")
lottie_rocket = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5py5ru1u.json")

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)



# Initialize session state for navigation and authentication status
if 'navigation' not in st.session_state:
    st.session_state.navigation = "Home"  # set the default navigation to Home

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

def footer():
    st.markdown("---")
    col1, col2 = st.columns([5, 5])

    with col1:
        st.markdown("Copyright ©Conestoga 2024", unsafe_allow_html=True)

    with col2:
        st.empty()
        
st.markdown('<div class="fullScreenDiv">', unsafe_allow_html=True)
with st.container():
    left_column, right_column = st.columns((2, 7))
    
    with left_column:
        selected = option_menu(
            menu_title=None,
            options=["Introduction",'Case Studies', 'Manfacturer', 'Compliance', 'About Me'], 
            icons=['house', 'person-circle', 'file-earmark-word-fill', 'person-lines-fill', 'shield-check', 'translate', 'envelope', 'file-lock'], 
            menu_icon="cast", 
            default_index=0, 
            orientation="vertical"
        )
        #lottie = load_lottiefile("similo3.json")
        #st_lottie(lottie,key='loc')
        #st_lottie(lottie_rocket, height=200, key="Rocket")
        st_lottie(lottie_AI, height=170, key="AI")  
    with right_column:
        if selected == "Introduction":
            homepage()
        elif selected == "Case Studies":
            case_studies_page()
        elif selected == "Manfacturer":
            manufacturer_page()            
        elif selected == "About Me":
            aboutme()
        elif selected == "Compliance":
            compliance_benefits_page()


st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    footer()
