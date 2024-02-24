FROM python:3.9-alpine3.13

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# RUN apk add uvicorn
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# CMD ["gunicorn", "app.main:app","-w 4","-k uvicorn.workers.UvicornWorker","--reload", "-b 0.0.0.0:8000"]
CMD ["uvicorn", "app.main:app","--reload", "--host", "0.0.0.0", "--port", "8000"]