# app/ocr/ocr_engine.py

from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import os
import tempfile

def extract_text_from_image(image_path: str) -> str:
    return pytesseract.image_to_string(Image.open(image_path))


def extract_text_from_pdf(pdf_path: str) -> str:
    text = ""
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path(pdf_path, output_folder=path)
        for i, image in enumerate(images):
            page_text = pytesseract.image_to_string(image)
            text += f"\n--- Page {i+1} ---\n" + page_text
    return text