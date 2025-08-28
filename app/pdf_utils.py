import fitz 

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.
    Input: pdf_file (Uploaded file object from Streamlit)
    Output: Extracted text as a string
    """
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page in pdf_document:
        text += page.get_text()
    return text
