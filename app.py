import streamlit as st
from utils import extract_text_from_pdf
from agent import HRAgent

# Page Config
st.set_page_config(page_title="AI Agentic HR Screener", layout="centered")

st.title("🤖 Agentic Resume Screener")
st.markdown("Upload a resume and job description to get a professional HR analysis.")

# Sidebar for API Key (or use .env)
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    if api_key:
        import os
        os.environ["GEMINI_API_KEY"] = api_key

# Input Section
job_desc = st.text_area("Step 1: Paste Job Description", height=200)
uploaded_file = st.file_uploader("Step 2: Upload Resume (PDF)", type="pdf")

# Execution Section
if st.button("Run AI Analysis"):
    if not api_key:
        st.error("Please provide an API Key in the sidebar.")
    elif uploaded_file and job_desc:
        with st.spinner("Agent is analyzing the candidate..."):
            # Process
            resume_text = extract_text_from_pdf(uploaded_file)
            agent = HRAgent()
            report = agent.analyze(resume_text, job_desc)
            
            # Display Result
            st.success("Analysis Complete!")
            st.markdown("---")
            st.markdown(report)
    else:
        st.warning("Please upload a resume and paste a job description first.")