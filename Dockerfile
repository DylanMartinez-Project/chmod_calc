FROM python:3.9-slim-buster as build

WORKDIR /app

COPY Pipfile.lock .

RUN pip install pipenv && \
    pipenv requirements > requirements.txt

FROM python:3.9-slim-buster as runtime

WORKDIR /app

COPY --from=build /app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["--server.port", "8501","--server.address", "0.0.0.0",  "chmod.py"]
