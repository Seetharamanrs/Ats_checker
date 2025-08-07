import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from PyPDF2 import PdfReader

st.header("Resume ATS Match & Missing Skills Checker")

resume_text = st.file_uploader("Upload a resume in PRD format", type=["pdf"])
jd_text = st.text_area("Paste Job Description text here", height=100)


def extracting_pdf(r_t):
    if r_t is not None:
        r=PdfReader(r_t)
        text=""
        for i in r.pages:
            text +=i.extract_text() or ""
            return text.strip()
    return ""
resume_text=extracting_pdf(resume_text)

if resume_text and jd_text:
    prompt = ChatPromptTemplate([
        ("system", "You are a helpful assistant specializing in resume screening."),
        ("user", 
         """Given a resume and a job description, only respond with:
         1. ATS Match Score as a percentage
         2. Key missing skills (comma separated)
        IMPORTANT:
            - Do not guess or assume any information that is not explicitly stated in the resume.
            - If something is unclear or missing, treat it as missing.
            - If all key skills match, say "None" for Missing Skills.
            - Be objective and literal — do not embellish or add extra commentary.

         
         Format exactly like this (no extra text):

         Match Score: XX%
         Missing Skills: skill1, skill2, skill3

         Resume:
         \"{resume}\"

         Job Description:
         \"{jd}\"
         """)
    ])

if st.button("Check the Score"):
   
    output_parser = StrOutputParser()
    chain = prompt | output_parser
    
    mistral_llm = Ollama(model="mistral")
    mistral_inputs = {"resume": resume_text, "jd": jd_text}
    mistral_chain=prompt|mistral_llm|output_parser
    mistral_result = mistral_chain.invoke(mistral_inputs)

    mistral_match_score = mistral_result.split("Match Score: ")[1].split("%")[0]
    mistral_missing_skills = mistral_result.split("Missing Skills: ")[1].strip()
    
    llama_llm = Ollama(model="mistral")
    llama_input = {"resume": resume_text, "jd": jd_text}
    llama_chain=prompt|llama_llm|output_parser
    llama_result = llama_chain.invoke(llama_input)

    llama_match_score = llama_result.split("Match Score: ")[1].split("%")[0]
    llama_missing_skills = llama_result.split("Missing Skills: ")[1].strip()
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ATS Screening Result")
        st.text(f"Match Score: {mistral_match_score}%")
        st.text(f"Missing Skills: {mistral_missing_skills}")
    with col1:
        st.markdown("### ATS Screening Result")
        st.text(f"Match Score: {llama_match_score}%")
        st.text(f"Missing Skills: {llama_missing_skills}")
