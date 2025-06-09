# Stage 1: Builder (install dependencies)
FROM python:3.9-slim-buster as builder

WORKDIR /app
COPY requirements.txt .

# Install system dependencies first
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --user -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-alpine
WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Set environment variables
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]