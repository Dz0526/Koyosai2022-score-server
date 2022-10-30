FROM python:3.9-buster
ENV PYTHONUMBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY . ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

ARG PGDATABASE
ARG PGHOST
ARG PGPASSWORD
ARG PGPORT
ARG PGUSER
ENV PYTHONPATH=/src

ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
