# official py
FROM python:3.11-slim

# working dir
WORKDIR /app

# copy & install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the app
COPY ./app ./app

# start the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
