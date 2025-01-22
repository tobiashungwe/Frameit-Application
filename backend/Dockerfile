# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements_api.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements_api.txt

# Copy the entire project into the container
COPY .. .

# Ensure the Python path includes the backend folder
ENV PYTHONPATH=/app

# Expose the default FastAPI port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
