# Start with a base Python image
FROM python:3.8-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code to the container
COPY . .

# Set the environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8000 \
    WORKERS_PER_CORE=1 \
    MAX_WORKERS=4

# Expose port 8000
EXPOSE 8000

# Start the application with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
