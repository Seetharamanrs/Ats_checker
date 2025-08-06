# ATS Resume Checker (Job Match Scoring Tool):

Built a local-first ATS (Applicant Tracking System) screening tool using Streamlit and  open-source LLM. Inspired by the challenges of modern job hunting, this app compares a candidate’s resume against a job description and outputs an estimated match score along with missing skills. The tool empowers job seekers to tailor resumes for specific roles and helps demystify the often opaque ATS screening process — all without needing any cloud APIs or internet access.

## Features
- Upload resume and job description as PDFs directly via the Streamlit interface
- Extracts and parses resume and JD content locally using PyPDF2
- Now Checking with several other models 
- Calculate an ATS Match Score (in %)
- Identify missing skills based on job requirements
- Enforces strict model prompting to avoid hallucination and false positives
- Built-in file size validation (2 MB max) for secure, lightweight uploads
- Clean and HR-friendly UI for non-technical users

Install dependencies
```bash
pip install -r requirements.txt
```



