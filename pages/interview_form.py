import streamlit as st

def interview_details_form():
    st.title("Interview Details Form")
    
    # Get applicant information
    applicant_name = st.text_input("Applicant's Name")
    applicant_email = st.text_input("Applicant's Email")
    applicant_phone = st.text_input("Applicant's Phone Number")
    
    # Get interview information
    company_name = st.text_input("Company Name")
    interview_date = st.date_input("Interview Date")
    interview_time = st.time_input("Interview Time")
    interviewer_name = st.text_input("Interviewer's Name")
    
    # Get additional details
    additional_notes = st.text_area("Additional Notes", "Enter any additional notes here...")
    
    # Submit button
    if st.button("Submit"):
        # Save the details or perform any necessary actions
        st.success("Interview details submitted successfully!")

# Run the app
if __name__ == "__main__":
    interview_details_form()