# Smart Resume Analyzer

I built this project while learning Python and Streamlit. The idea was to create something that can read a resume (PDF) and give a basic ATS score based on skills matching.

It is not an advanced industry ATS system, but it gives a simple understanding of how resume screening works.

---

## What this project does
- Upload a resume in PDF format
- Extract text from the resume
- Check for basic technical skills
- Show matched and missing skills
- Give a simple ATS score out of 100

---

## Tech used
- Python
- Streamlit
- PyPDF2

---

## How it works (simple explanation)
First, the resume text is extracted from the PDF.  
Then the text is compared with a list of skills like Python, SQL, Machine Learning, etc.  
Each match contributes to the final score.

---

## Run this project

Clone the repo:
git clone https://github.com/your-username/resume-analyzer.git

Install requirements:
pip install -r requirements.txt

Run:
streamlit run app.py

---

## Live project
Add your Streamlit link here

---

## What I learned
- How Streamlit works
- How to handle PDF files in Python
- Basic logic building for scoring systems

---

## Author
Vanshika
