# Use a slim base image with Python
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set a working directory
WORKDIR /app

# Install system dependencies and cleanup after
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

EXPOSE 8002

# Use gunicorn for production or Django's runserver for development
CMD ["gunicorn", "-b", "0.0.0.0:8002", "backend.wsgi:application"]
