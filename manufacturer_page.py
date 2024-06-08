import streamlit as st

def manufacturer_page():
    st.title("Nested Knowledge")
    st.header("Innovators in Clinical Trial Technology")
    st.write("""
    ### Company Information
    - **Name**: Nested Knowledge
    - **Website**: [Nested Knowledge](https://www.nested-knowledge.com)
    - **More info**: [About](https://about.nested-knowledge.com/)
    """)

    st.write("""
    Nested Knowledge offers a comprehensive software platform for systematic literature review and meta-analysis. 
    The platform consists of two main components, AutoLit and Synthesis, which work in tandem to streamline clinical research processes.

    ### AutoLit
    - **Search**: Create updatable searches of PubMed or import studies from various databases.
    - **Screening**: Automatic PICO highlighting and inclusion prediction AI.
    - **Tagging**: Build and apply a tagging hierarchy to structure ideas and capture evidence.
    - **Extraction**: Meta-analytical data extraction for qualitative and quantitative synthesis.

    ### Synthesis
    - **Qualitative Synthesis**: Interactive visuals like sunburst diagrams to represent tagged concepts.
    - **Quantitative Synthesis**: Summarize findings, create scatter plots, and compute odds ratios.
    - **Manuscript**: Draft and auto-update tables and citations, integrating with Synthesis visuals.
    """)
    
if __name__ == "__main__":
    manufacturer_page()
