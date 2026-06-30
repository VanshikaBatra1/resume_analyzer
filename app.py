import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

# Job Description Input
job_description = st.text_area(
    "Paste Job Description Here (Optional)"
)

# Resume Upload
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file is not None:

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    # Extract text from all pages
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Show Resume Content
    st.subheader("Resume Content")
    st.write(text)

    # Skills to check
    skills = [
        "python",
        "java",
        "c",
        "sql",
        "machine learning",
        "data science",
        "streamlit",
        "power bi",
        "excel",
        "git",
        "github",
        "html",
        "css"
    ]

    found_skills = []

    # Find skills in resume
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    # ATS Score
    score = len(found_skills) * 7

    if score > 100:
        score = 100

    st.subheader("ATS Resume Score")
    st.progress(score)
    st.success(f"Score: {score}/100")

    # Skills Found
    st.subheader("Skills Found")
    for skill in found_skills:
        st.write("✅", skill.title())

    # Missing Skills
    missing_skills = [
        s for s in skills if s not in found_skills
    ]

    st.subheader("Missing Skills")
    for skill in missing_skills:
        st.write("❌", skill.title())

    # Suggestions
    st.subheader("Suggestions")

    if score < 50:
        st.warning(
            "Add more technical skills, projects, GitHub profile and certifications."
        )
    elif score < 80:
        st.info(
            "Good resume. Add more projects and measurable achievements."
        )
    else:
        st.success(
            "Excellent resume! Ready for most internship applications."
        )

    # Job Description Matching
    if job_description:

        jd_words = job_description.lower().split()

        matching_words = 0

        for word in jd_words:
            if word in text.lower():
                matching_words += 1

        match_score = int(
            (matching_words / len(jd_words)) * 100
        )

        if match_score > 100:
            match_score = 100

        st.subheader("Job Match Score")
        st.progress(match_score)
        st.success(
            f"Resume matches {match_score}% of the Job Description"
        )