FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install click flask
EXPOSE 80
ENTRYPOINT [ "python", "app.py", "--host=0.0.0.0", "--port=80" ]