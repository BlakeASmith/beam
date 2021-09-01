FROM python:3.8-slim

WORKDIR /app

COPY . .
RUN pip install /app

EXPOSE 80

ENTRYPOINT ["beam-server", "--host=0.0.0.0", "--port=80"]