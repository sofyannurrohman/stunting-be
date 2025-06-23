# Stage 1: Builder
FROM python:3.10-alpine AS builder

WORKDIR /code

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    linux-headers \
    g++ \
    openblas-dev

# Copy production requirements
COPY requirements-prod.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements-prod.txt

# Stage 2: Runtime
FROM python:3.10-alpine

WORKDIR /code

# Copy installed dependencies
COPY --from=builder /root/.local /root/.local

# Copy application files
COPY app.py .
COPY api/ ./api/
COPY db/ ./db/
COPY schemas/ ./schemas/
COPY services/ ./services/
COPY static/ ./static/
COPY utils/ ./utils/
COPY le_condition.joblib .
COPY model.joblib .
COPY scaler.joblib .

# Set PATH
ENV PATH=/root/.local/bin:$PATH

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]