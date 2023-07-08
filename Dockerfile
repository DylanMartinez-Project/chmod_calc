FROM python:3.9-slim-buster as build

WORKDIR /app

COPY Pipfile.lock .

RUN pip install pipenv && \
    pipenv requirements > requirements.txt

FROM python:3.9-slim-buster as runtime

WORKDIR /app

# Add the user "dielawn"
RUN groupadd -r dielawn && useradd --no-log-init -r -g dielawn dielawn

COPY --from=build /app/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Change the ownership to the user "dielawn"
RUN chown -R dielawn:dielawn /app

USER dielawn

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD ["--server.port", "8501","--server.address", "0.0.0.0",  "chmod.py"]
