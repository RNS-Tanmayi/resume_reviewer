from crewai import Task
from agents import resume_reviewer, ats_checker, career_coach

def create_task(resume_text):
    roast_task = Task(
        description=f"""
        Review this resume and roast it honestly.
        Highlight weak bullet points and formatting problems.
        Resume:
        {resume_text}
        """,
        expected_output="A brutally honest review of the resume highlighting weak areas and suggestions.",
        agent=resume_reviewer
    )

    ats_task = Task(
        description=f"""
        Analyze this resume and decide if it is a good fit for the role.
        Provide:
        - ATS score out of 100
        Resume:
        {resume_text}
        """,
        expected_output="ATS score with explanation and decision on whether the resume is a good fit for the role.",
        agent=ats_checker
    )

    skill_task = Task(
        description=f"""
        Identify missing technical skills from this resume.
        Suggest improvements for software engineering roles.
        Resume:
        {resume_text}
        """,
        expected_output="List of missing skills and recommended improvements.",
        agent=career_coach
    )

    return [roast_task, ats_task, skill_task]
