FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.8.2

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# entrypoint genérico (api) – o compose do worker sobrescreve
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
