import streamlit as st

def recruitment_form():
    st.title("Company Recruitment Form")
    
    # Company information
    company_name = st.text_input("Company Name")
    company_location = st.text_input("Company Location")
    
    # Job details
    job_title = st.text_input("Job Title")
    job_category = st.text_input("Job Category")
    
    # Responsibilities (comma-separated)
    responsibilities = st.text_area("Responsibilities", "Enter responsibilities separated by commas")
    
    # Preferred Qualifications (comma-separated)
    preferred_qualifications = st.text_area("Preferred Qualifications", "Enter preferred qualifications separated by commas")
    
    # Submit button
    if st.button("Submit"):
        # Store the details or perform any necessary actions
        st.success("Recruitment details submitted successfully!")

# Run the app
if __name__ == "__main__":
    recruitment_form()
