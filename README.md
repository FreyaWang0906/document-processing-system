# Document Processing System

This is an AI-powered document processing system built with **FastAPI**, **PyTorch**, and **PostgreSQL**.  
It supports **file upload**, **OCR (Optical Character Recognition)**, **document classification**, and **metadata storage**, fully containerized with **Docker**.

---

## Features

- Upload scanned documents (PDF or image)
- Extract text using Tesseract OCR
- Automatically classify documents (`resume`, `contract`, `invoice`)
- Store document metadata (filename, content, type, timestamp) in PostgreSQL
- FastAPI-based REST API with interactive docs
- Fully Dockerized and ready for deployment

---

## Tech Stack

- **Python 3.9**
- **FastAPI** (API framework)
- **PyTorch** (model logic - rule-based for now)
- **Tesseract OCR** (via `pytesseract`)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (metadata DB)
- **Docker** (containerization)

---

## Getting Started (Docker)

### 1. Clone the repository

```bash
git clone https://github.com/FreyaWang0906/document-processing-system.git
cd document-processing-system
```

### 2. Start PostgreSQL

```bash
docker network create doc-net

docker run --name docdb \
  --network doc-net \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin \
  -e POSTGRES_DB=docsys \
  -p 5432:5432 \
  -d postgres
```

### 3. Build and run the app

```bash
docker build -t doc-app .

docker run --name doc-api \
  --network doc-net \
  -p 8000:8000 \
  -d doc-app
```

### 4. Access the API

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

Try /upload/ to upload a document and receive predictions.

---

## Sample Response

```json
{
  "filename": "resume.pdf",
  "document_type": "resume",
  "message": "File processed and saved successfully",
  "excerpt": "Experience: Software Engineering Intern..."
}
```

---

## Future Improvements

- Replace rule-based classifier with real PyTorch model
- Add `/documents/` query endpoint
- Frontend UI for drag-and-drop upload
- Deploy to Railway or AWS ECS

---

## Author

Freya Wang  
[GitHub Profile](https://github.com/FreyaWang0906)
