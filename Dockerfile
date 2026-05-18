FROM python:3.12-slim

WORKDIR /workspace

ENV PYTHONUNBUFFERED=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose a shell by default
CMD ["bash"]
