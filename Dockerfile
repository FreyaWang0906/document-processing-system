# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for uvicorn
EXPOSE 8000

# Default command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]