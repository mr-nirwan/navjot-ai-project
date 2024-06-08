import streamlit as st

def technology_page():
    st.title("Nested Knowledge Technology")
    st.header("Advanced AI for Clinical Trials")
    st.write("""
    ### Key Features
    - **AutoLit**: Search, screen, tag, and extract data with AI-driven tools.
      - Literature Search: Create updatable searches or import studies from various databases.
      - Screening: Automatic PICO highlighting and inclusion prediction AI.
      - Tagging: Build and apply a tagging hierarchy to structure ideas and capture evidence.
      - Meta-Analytical Data Extraction: Turn tags into data elements for qualitative and quantitative synthesis.
    - **Synthesis**: Visualize, analyze, publish, and share insights.
      - Qualitative Synthesis: Interactive visuals like sunburst diagrams.
      - Quantitative Synthesis: Summarize findings, create scatter plots, and compute odds ratios.
      - Manuscript: Draft and auto-update tables and citations.
    """)
    st.image("path_to_technology_image.jpg", caption="Technology in Action")

if __name__ == "__main__":
    technology_page()
