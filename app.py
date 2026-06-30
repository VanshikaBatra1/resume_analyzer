import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

resume_text = ""

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    st.write("Resume Uploaded Successfully")

if uploaded_file and job_description:
    st.write("Job Description Received")
