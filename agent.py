import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class HRAgent:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def analyze(self, resume_text, job_description):
        prompt = f"""
        You are an expert Technical Recruiter. Evaluate the following resume against the job description.
        
        Job Description:
        {job_description}
        
        Resume Content:
        {resume_text}
        
        Provide a detailed analysis including:
        1. A Match Score (0-100).
        2. Key Strengths (bullet points).
        3. Missing Skills or Gaps.
        4. Final Verdict (Proceed/Hold/Reject).
        
        Format your response clearly with headings.
        """
        response = self.model.generate_content(prompt)
        return response.text