import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import pdfplumber, docx, pptx, pytesseract
from PIL import Image

def extract_text(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted

        if len(text.strip()) == 0:
            raise ValueError("Scanned PDF detected. Please upload a text-based PDF or an image file for OCR.")

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif file_path.endswith(".pptx"):
        pres = pptx.Presentation(file_path)
        for slide in pres.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + "\n"

    elif file_path.lower().endswith((".png",".jpg",".jpeg")):
        img = Image.open(file_path)
        text += pytesseract.image_to_string(img)

    else:
        raise ValueError("Unsupported format")

    print("Extracted text length:", len(text))
    return text
