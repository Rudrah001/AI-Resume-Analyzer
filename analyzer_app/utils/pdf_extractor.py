import pdfplumber
import io

def extract_pdf_text(pdf_file):
    full_text = ''

    pdf_file.seek(0)
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