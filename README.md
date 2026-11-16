# AI-Powered Resume Reviewer

An AI-powered resume analysis application that uses multiple specialized AI agents to review resumes, evaluate ATS compatibility, and identify missing technical skills.

## Overview

The AI Resume Reviewer automates parts of the resume evaluation process using a multi-agent architecture built with CrewAI and Groq-powered Large Language Models (LLMs).

Users can upload their resumes in PDF format and receive feedback from three specialized AI agents, each focusing on a different aspect of resume evaluation.

## Features

- **Resume Review:** Evaluates resume content and highlights weak bullet points, formatting issues, and areas for improvement.
- **ATS Compatibility Analysis:** Provides an AI-generated ATS compatibility assessment with an indicative score out of 100 and supporting feedback.
- **Missing Skills Identification:** Identifies potential technical skill gaps and recommends improvements for software engineering roles.
- **PDF Processing:** Extracts resume text from uploaded PDF documents using PyPDF.
- **Interactive Interface:** Provides a simple interface for uploading resumes and viewing the analysis through Streamlit.

## Multi-Agent Architecture

The application uses three specialized AI agents:

| Agent | Role | Responsibility |
|---|---|---|
| Resume Reviewer | Senior Tech Recruiter | Reviews resume quality and provides constructive criticism |
| ATS Checker | ATS Expert | Evaluates ATS compatibility and provides an indicative score |
| Career Coach | Career Coach | Identifies missing technical skills and suggests improvements |

CrewAI coordinates the agents and their assigned tasks to generate the final review.

## Tech Stack

- **Programming Language:** Python
- **AI Agent Framework:** CrewAI
- **LLM Provider:** Groq
- **Language Models:** Groq-supported LLM
- **Frontend:** Streamlit
- **PDF Processing:** PyPDF
- **Environment Management:** Python Virtual Environment
- **Version Control:** Git and GitHub

## Project Structure

```text
resume_reviewer/
│
├── agents.py
├── tasks.py
├── crew_setup.py
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RNS-Tanmayi/resume_reviewer.git
cd resume_reviewer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Obtain an API key through the Groq developer console.

**Important:** Never upload your `.env` file or expose your API key in public repositories.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use

1. Launch the application.
2. Upload a resume in PDF format.
3. Click the **Review Resume** button.
4. Wait for the AI agents to complete their analysis.
5. View the resume review, ATS compatibility assessment, and missing skills recommendations.

## Performance and Testing

The application was tested using 10 unique PDF resumes.

| Metric | Result |
|---|---|
| Number of unique resumes tested | 10 |
| Average review time | 12.12 seconds |
| Minimum review time | 8.42 seconds |
| Maximum review time | 23.44 seconds |

Review time represents the end-to-end execution time of the multi-agent review process. Results are based on an initial test set and may vary with resume complexity, model response times, and network conditions.

## Future Improvements

- Add automated unit and integration tests.
- Improve error handling for invalid, empty, and scanned PDF files.
- Add downloadable resume analysis reports.
- Introduce job-description-based resume matching.
- Evaluate the consistency and relevance of AI-generated recommendations.

## Disclaimer

The ATS compatibility score is an AI-generated estimate and is not an actual score from a commercial Applicant Tracking System. The feedback is intended to assist with resume improvement and should be reviewed by the user.

## Author

**Tanmayi Rajulapudi**

[GitHub Repository](https://github.com/RNS-Tanmayi/resume_reviewer)
