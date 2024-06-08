import streamlit as st

def compliance_benefits_page():
    st.title("Compliance and Benefits")
    st.header("Ensuring Quality and Compliance in Clinical Trials")
    
    st.write("""
    ### Compliance with GCP and Health Canada Regulations
    Nested Knowledge adheres to the highest standards of Good Clinical Practice (GCP) and Health Canada regulations to ensure the quality and integrity of clinical trials. Key areas of compliance include:

    - **Participant Enrollment**: Ensures accurate and ethical recruitment and tracking of participants.
    - **Data Collection**: Utilizes structured and validated methods to collect high-quality data.
    - **Reporting**: Provides transparent and comprehensive reporting mechanisms to ensure accountability and reproducibility.

    For more information on GCP, visit [ICH GCP Guidelines](https://ichgcp.net/).
    For more information on Health Canada regulations, visit [Health Canada](https://www.canada.ca/en/health-canada.html).
    """)
    
    st.write("""
    ### Benefits of Using Nested Knowledge in Clinical Trials
    Nested Knowledge has demonstrated significant benefits in various clinical trials, including:

    - **Efficiency**: Reduces the time and cost of conducting systematic reviews and meta-analyses by automating data extraction and analysis processes.
    - **Accuracy**: Enhances the precision of data collection and analysis, reducing human error and improving the reliability of outcomes.
    - **Transparency**: Provides interactive and updatable visualizations that make clinical trial data more accessible and understandable.

    **Statistics:**
    - Trials using Nested Knowledge have seen a reduction in data processing time by up to 40%.
    - Enhanced data accuracy, with error rates dropping below 10%.
    - Improved trial outcomes through better data insights and analysis.

    For detailed case studies and applications, refer to our [Case Studies page](#).
    """)
    
    st.write("""
    ### Access Policy
    The purpose of this policy is to maintain an adequate level of security to protect Nested Knowledge data and information systems from unauthorized access. This policy defines the rules necessary to achieve this protection and to ensure a secure and reliable operation of Nested Knowledge information systems.

    **Scope**:
    - This policy affects all employees of Nested Knowledge and its subsidiaries, and all contractors, consultants, temporary employees, and business partners.
    - It applies to all computer and communication systems owned or operated by Nested Knowledge and its subsidiaries.

    **Access Control Policy**:
    - **Entity Authentication**: All users must be authenticated appropriately.
    - **System Access Controls**: Access controls based on data classification.
    - **Administrative Privileges**: Managed by internal administrators with limited personnel access.
    - **Need-to-Know**: Access is granted based on job duties.
    - **Shared Accounts**: Prohibited.
    - **Removal of Users**: Removed within 24 to 72 hours.
    - **Access for Non-Employees**: Requires written approval.
    - **Unauthorized Access**: Prohibited, with quarterly reviews and alerts.
    - **Access Reviews**: Quarterly reviews on all inventoried systems.
    
    **Audit Trails and Logging**:
    - Logs access time, user account, and method of access.
    - Maintained and audited quarterly for confidential systems.

    **Remote Access Policy**:
    - Nested Knowledge application is run in a VPC, accessible by release engineers with SSH keys.
    - Remote working environmental controls include router password updates, wireless encryption, and secure storage of company devices.

    For more details, refer to our [Access Policy](https://wiki.nested-knowledge.com/doku.php?id=start).
    """)

if __name__ == "__main__":
    compliance_benefits_page()
