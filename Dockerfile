FROM python:3

WORKDIR /usr/src/app

# COPY REQUIREMENTS.txt to the working directory
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]