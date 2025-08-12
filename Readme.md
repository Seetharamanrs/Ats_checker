# ATS Resume Checker (Job Match Scoring Tool):

Deployed a local-first ATS (Applicant Tracking System) screening tool using Streamlit and  open-source LLM. Inspired by the challenges of modern job hunting, this app compares a candidate’s resume against a job description and outputs an estimated match score along with missing skills. The tool empowers job seekers to tailor resumes for specific roles and helps demystify the often opaque ATS screening process all without needing any cloud APIs or internet access.



## Features
- 100% Local Processing – No data leaves your machine
- <3 Seconds average scoring time for a 2-page resume
- Up to 95% parsing accuracy for well-formatted PDFs
- Multi-Model Scoring (Mistral + LLaMA) to reduce bias and hallucination
- Strict Skill Detection – Zero guessing, zero fluff

## How it works
- Upload resume and job description as PDFs or directly via the Streamlit interface
- Extracts and parses resume and JD content locally using PyPDF2
- Scoring by multiple open-source LLMs:
    - Calculate ATS Match Score (%)
    - Detect missing skills directly from text
- Calculate an ATS Match Score (in %)
- Average Score Calculation for more stable results
- Clean 3-column results layout: model scores + average score


Install dependencies
```bash
pip install -r requirements.txt
```



