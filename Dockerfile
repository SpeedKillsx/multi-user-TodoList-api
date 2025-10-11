FROM python:3.12.0-slim-bullseye

WORKDIR /app


COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*


COPY src ./src
COPY .env .
COPY log_config.yml .
COPY main.py .

EXPOSE 8000
CMD [ "uvicorn", "main:app" ,"--host", "0.0.0.0", "--port", "8000"]