FROM python:3.9.18-alpine3.19


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1


COPY . /app

WORKDIR /app/server

EXPOSE 8000

CMD ["python3", "mini_server.py"]
