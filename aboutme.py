import streamlit as st

def aboutme():
    st.title("About AI Marketing Tool")
    st.header("Clinical Research, Conestoga College")

    st.divider()
    
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            st.write("""
            - **Prepared by**: Navjot Kaur
            - **Submitted to**: Rachid Nessar
                    
            ### © Conestoga College
            """)
            st.write("""
            Nested Knowledge is dedicated to improving clinical trials through AI-driven solutions. 
            Which offer a suite of tools that optimize the systematic review and meta-analysis process, making it more efficient and accurate.
            """)
        with col2:
            col2.image('kevin8.png')

    
if __name__ == "__main__":
    aboutme()
