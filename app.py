import os
os.environ["CREW_DISABLE_TELEMETRY"] = "true"

import streamlit as st
from pypdf import PdfReader
from crew_setup import run_resume_agents

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon=":human_facepalming:",
    layout="wide"
)

st.title("AI Resume Reviewer")
st.markdown("Upload your resume and let AI do the hard work for you! :robot_face:")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

def extract_text(file):
    reader=PdfReader(file)
    text=""
    for page in reader.pages:
        text += page.extract_text()
    return text

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)
    st.success("Resume uploaded successfully!")

    if st.button("Review Resume"):
        with st.spinner("AI is reviewing your resume..."):
            result=run_resume_agents(resume_text)
        st.success("AI has reviewed your resume!")
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader("Resume Roast")
            st.write(result.tasks_output[0].raw)
        with col2:
            st.subheader("ATS Compatibility")
            st.write(result.tasks_output[1].raw)
        with col3:
            st.subheader("Missing Skills")
            st.write(result.tasks_output[2].raw)
        st.balloons()