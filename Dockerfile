FROM python:3.12-slim

# Set a working directory inside the container
WORKDIR /workspace

# Keep Python output unbuffered for logs
ENV PYTHONUNBUFFERED=1

# Install Python dependencies from requirements
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose a shell by default for development
CMD ["bash"]
