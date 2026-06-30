import streamlit as st
import PyPDF2
import re

st.set_page_config(page_title="Smart Resume Analyzer", page_icon="📄", layout="centered")

st.title("📄 Smart Resume Analyzer")
st.caption("Built by Vanshika 🚀")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning", "nlp",
    "pandas", "numpy", "streamlit", "tensorflow",
    "keras", "data analysis", "git", "docker"
]

def extract_text(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

def calculate_ats_score(text):
    found_skills = []
    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    score = int((len(found_skills) / len(SKILLS_DB)) * 100)
    return score, found_skills

if uploaded_file:

    text = extract_text(uploaded_file)

    st.success("Resume processed successfully 🚀")

    score, skills = calculate_ats_score(text)

    st.subheader("📊 ATS Score")
    st.progress(score)
    st.write(f"Your ATS Score: **{score}/100**")

    st.subheader("✅ Matched Skills")
    st.write(skills)

    st.subheader("❌ Missing Skills")
    missing = list(set(SKILLS_DB) - set(skills))
    st.write(missing[:10])

    st.subheader("📄 Resume Preview")
    st.write(text[:2000])
