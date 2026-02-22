FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --target=/app

FROM python:3.13-slim AS runtime

WORKDIR /app

COPY --from=builder /app /app

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]