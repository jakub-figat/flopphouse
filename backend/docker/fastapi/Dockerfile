FROM python:3.9.5

ENV POETRY_VERSION=1.1.7

WORKDIR /backend

COPY ./pyproject.toml ./poetry.lock .
RUN pip install poetry==$POETRY_VERSION

RUN poetry install

COPY . .

CMD ["./main.py"]
