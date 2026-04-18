import re

def extract_experience_section(resume_text):
    pattern = r'^[\s]*(experience|work experience|professional experience|employment|work history)[:\s]*\n+([\s\S]*?)(?=^[\s]*(education|skills|technical skills|certifications|projects|achievements|summary)[:\s]*$|\Z)'
    match = re.search(pattern,resume_text,re.IGNORECASE|re.DOTALL|re.MULTILINE)
    if match:
        return match.group(2)
    return resume_text

def extract_project_section(resume_text):
    pattern = r'^[\s]*(project|projects)[:\s]*\n+([\s\S]*?)(?=^[\s]*(experience|education|skills|technical skills|certifications|achievements|summary)[:\s]*$|\Z)'
    match = re.search(pattern,resume_text,re.IGNORECASE|re.DOTALL|re.MULTILINE)
    if match:
        return match.group(2)
    return resume_text

def remove_dates(text):
    # Remove date patterns
    text = re.sub(r'\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*[\s,]*\d{2,4}\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b(19|20)\d{2}\b', '', text)         # years: 2019, 2023
    text = re.sub(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', '', text)  # 01/03/2022
    text = re.sub(r'\b\d{4}\s*[-–]\s*(\d{4}|present)\b', '', text, flags=re.IGNORECASE)  # 2021-2023
    
    # Clean up extra whitespace left behind
    text = re.sub(r'\s+', ' ', text).strip()
    return text