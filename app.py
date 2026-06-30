import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

def calculate_score(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    job_words = set(job_description.split())
    resume_words = set(resume_text.split())

    common = job_words.intersection(resume_words)

    if len(job_words) == 0:
        return 0, set(), set()

    score = (len(common) / len(job_words)) * 100

    missing = job_words - resume_words
    matched = common

    return round(score, 2), matched, missing


if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()

    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume") and job_description:
        score, matched, missing = calculate_score(resume_text, job_description)

        st.subheader("ATS Score")
        st.write(f"{score} / 100")

        st.subheader("Matched Keywords")
        st.write(matched)

        st.subheader("Missing Keywords")
        st.write(missing)
