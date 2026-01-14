# 🤖 AI Agentic Resume Screener

An intelligent resume screening system powered by **Google Gemini 2.5** and **Streamlit**. Unlike traditional ATS (Applicant Tracking Systems) that rely on simple keyword matching, this agent uses Large Language Models to **reason** about a candidate's experience, impact, and cultural fit.

---

## 🌟 Key Features

- **Semantic Analysis:** Understands context (e.g., knows that "React Developer" fits a "Frontend Engineer" role).
- **Agentic Reasoning:** Provides a detailed "Pros and Cons" list and a final hiring verdict (Proceed/Hold/Reject).
- **Skill Gap Identification:** Automatically identifies missing technical or soft skills required for the role.
- **Privacy First:** Designed to run locally with secure API key management.
- **Modern UI:** Clean, interactive dashboard built with Streamlit.

---

## 🏗️ Project Architecture



1. **Extraction:** Uses `PyPDF` to convert unstructured PDF data into clean text.
2. **Context Injection:** Combines the Job Description and Resume into a specialized "HR Specialist" prompt.
3. **Inference:** Google Gemini analyzes the depth of experience and technical stack.
4. **Structured Output:** Displays a professional recruitment report.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **AI Brain:** Google Gemini 2.5 Flash API
- **Frontend:** Streamlit
- **PDF Engine:** PyPDF
- **Environment Management:** Python-Dotenv

---

## 🚀 Getting Started

### 1. Prerequisites
- A Google Cloud / AI Studio Account.
- [Get your Gemini API Key here](https://aistudio.google.com/).

### 2. Installation
```bash
# Clone the repository
git clone [https://github.com/yourusername/ai-resume-screener.git](https://github.com/yourusername/ai-resume-screener.git)
cd ai-resume-screener

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt