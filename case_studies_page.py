import streamlit as st

def case_studies_page():
    st.title("Case Studies")
    st.header("Real-world Applications of Nested Knowledge")
    
    # Study 1
    st.subheader("Endovascular Thrombectomy for Ischemic Stroke with Large Core Volume")
    st.write("""
    **How is it used?**
    Nested Knowledge AutoLit software was utilized to conduct a systematic literature review from inception to February 12, 2023, including the TESLA trial results on June 10, 2023. 

    **Study Description**
    This study performed a meta-analysis of RCTs comparing endovascular thrombectomy (EVT) to medical therapy (MEDT) for acute ischemic stroke with large ischemic core volume. EVT was associated with greater rates of improved outcomes and early neurological improvement, though with higher rates of symptomatic intracranial hemorrhage.
    """)
    
    # Study 2
    st.subheader("Hypoperfusion Intensity Ratio as a Predictor of Outcomes after Thrombectomy Triage")
    st.write("""
    **How is it used?**
    Nested Knowledge was used to screen literature for studies comparing patients with favorable versus unfavorable hypoperfusion intensity ratio (HIR) who underwent thrombectomy triage.

    **Study Description**
    This meta-analysis assessed the correlation between HIR and successful reperfusion after thrombectomy in patients with acute ischemic stroke due to large vessel occlusion. The analysis faced limitations due to heterogeneity in data reporting but highlighted the need for data homogeneity in future research.
    """)
    
    # Study 3
    st.subheader("Mortality of COVID-19 in Patients with Hematological Malignancies versus Solid Tumors")
    st.write("""
    **How is it used?**
    Nested Knowledge software was used to systematically search PubMed and Embase for articles reporting mortality rates for cancer patients with COVID-19.

    **Study Description**
    This study examined mortality rates among cancer patients with COVID-19, comparing those with hematological malignancies to those with solid tumors. The findings indicated higher mortality rates for patients with hematological malignancies, underscoring the vulnerability of this group.
    """)
    
    # Study 4
    st.subheader("Endovascular Thrombectomy after Acute Ischemic Stroke of the Basilar Artery")
    st.write("""
    **How is it used?**
    Nested Knowledge was used to screen literature for RCTs on endovascular thrombectomy (EVT) for basilar artery occlusion.

    **Study Description**
    This meta-analysis included four RCTs and demonstrated that EVT significantly improved functional outcomes and reduced mortality compared to medical therapy alone, although it was associated with higher rates of symptomatic intracranial hemorrhage.
    """)

    st.info("There are many more applications and studies that have used Nested Knowledge. These case studies highlight just a few examples.")

if __name__ == "__main__":
    case_studies_page()
