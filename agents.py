import streamlit as st
from dotenv import load_dotenv
from crewai import Agent,LLM
import os

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=api_key,
    temperature=0.5,
    max_tokens=800
)

resume_reviewer=Agent(
    role="Senior Tech Recruiter",
    goal="Give brutally honest resume feedback",
    backstory="You are a FAANG recruiter reviewing resumes",
    llm=llm,
    verbose=True
)
ats_checker=Agent(
    role="ATS Expert",
    goal="Analyse ATS compatibility",
    backstory="You understand how ATS work and can help you decide if a candidate is a good fit",
    llm=llm,
    verbose=True
)
career_coach=Agent(
    role="Career Coach",
    goal="Suggest improvements and missing skills",
    backstory="You help engineers improve their resumes",
    llm=llm,
    verbose=True
)

