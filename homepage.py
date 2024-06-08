import requests
import streamlit as st
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_rocket = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_5py5ru1u.json")

def homepage():
    with st.container():
        left_column, right_column = st.columns((2, 1))
        
        with left_column:
            st.title("Nested Knowledge: Revolutionizing Clinical Trials")
            st.header("Transforming Clinical Research with AI")
        with right_column:
            st_lottie(lottie_rocket, height=200, key="Rocket")
    st.write("""
    ### A Brief Description of the Technology
    Nested Knowledge is a state-of-the-art medical research platform designed for the digital age. Our platform organizes and presents scientific research from thousands of studies through dynamic, updatable, and interactive visual interfaces. Leveraging machine learning-driven data extraction, we create structured datasets of clinical outcomes that are analyzed using best practices in network meta-analysis.

    ### What is Nested Knowledge?
    Nested Knowledge is a comprehensive software solution for systematic literature review and meta-analysis. It combines AutoLit for search, screening, tagging, and data extraction with Synthesis for visualization, analysis, and publication. Our platform transforms the clinical trial process, making it more efficient and insightful.

    ### Key Features
    - **AutoLit**: Facilitates search, screening, tagging, and extraction of clinical data.
    - **Synthesis**: Visualizes and analyzes data, providing interactive and updatable insights.
    - **Qualitative and Quantitative Synthesis**: Integrates qualitative insights and quantitative metrics, ensuring comprehensive analysis.

    Discover how Nested Knowledge can streamline your clinical trial processes and provide comprehensive insights into medical research.
    """)
    st.info("To see how Nested Knowledge has been used in clinical research, check out the Case Studies page.")

if __name__ == "__main__":
    homepage()
