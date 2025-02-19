import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

#Test with a sample PDF
pdf_file = "resume.pdf" # Replace with your file
resume_text = extract_text_from_pdf(pdf_file)
print(resume_text)

