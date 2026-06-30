import streamlit as st
import PyPDF2

st.set_page_config(page_title="Smart Resume Analyzer", page_icon="📄", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }
    .stApp {
        background-color: #0f172a;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Smart Resume Analyzer")
st.caption("Upload your resume and get instant insights")

uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

if uploaded_file:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()

    st.success("Resume processed successfully 🚀")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📌 Resume Preview")
        st.text_area("", text[:1500], height=400)

    with col2:
        st.subheader("📊 Quick Info")
        st.write("✔ PDF uploaded")
        st.write("✔ Text extracted")
        st.write("✔ Ready for analysis")

    st.subheader("📄 Full Extracted Text")
    st.write(text)
