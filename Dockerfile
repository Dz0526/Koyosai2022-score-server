FROM python:3.9-buster
ENV PYTHONUMBUFFERED=1

WORKDIR /src

RUN pip install poetry

COPY project.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f project.toml ]; then poetry install; fi

ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
