from fastapi import FastAPI, UploadFile, File
import shutil
import os
from app.classification.model import classify_text
from app.ocr.ocr_engine import extract_text_from_pdf, extract_text_from_image
from app.db.session import SessionLocal
from app.db.models import Document

app = FastAPI()


# Folder to save uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Welcome to Document Processing System."}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):

        # Save uploaded file to local disk
        file_location = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Extract text using OCR (based on file type)
        if file.filename.lower().endswith(".pdf"):
            extracted_text = extract_text_from_pdf(file_location)
        else:
            extracted_text = extract_text_from_image(file_location)

        # Use classifier to get document type
        doc_type = classify_text(extracted_text)

        # Save to database
        db = SessionLocal()
        document = Document(
            filename=file.filename,
            content=extracted_text,
            doc_type=doc_type
        )

        # Save metadata to PostgreSQL
        db = SessionLocal()
        document = Document(
            filename=file.filename,
            content=extracted_text,
            doc_type=None  # Placeholder for classification
        )
        db.add(document)
        db.commit()
        db.close()

        # Return response to client
        return {
            "filename": file.filename,
            "document_type": doc_type,
            "message": "File processed and saved successfully",
            "excerpt": extracted_text[:200] + "..."
        }
