FROM python:3.8-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
RUN poetry install

EXPOSE 80

ENTRYPOINT ["poetry", "run", "beam_server", "--host=0.0.0.0", "--port=80"]