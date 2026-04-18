import pdfplumber
from docx import Document
import io
import re

def clean_text(text):
    # text = text.lower()
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def extract_docx_text(docx_file):
    full_text = ""

    doc = Document(docx_file)

    for para in doc.paragraphs:
        if para.text:
            full_text += para.text + "\n"

    return clean_text(full_text)

def extract_pdf_text(pdf_file):
    full_text = ''

    # pdf_file.seek(0)
    if isinstance(pdf_file,str):
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_txt = page.extract_text()
                if page_txt:
                    full_text += page_txt + '\n'
    else:
        with pdfplumber.open(io.BytesIO(pdf_file.read())) as pdf:
            for page in pdf.pages:
                page_txt = page.extract_text()
                if page_txt:
                    full_text += page_txt + '\n'
    
    return full_text.strip()