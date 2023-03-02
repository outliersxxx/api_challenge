# Imagen de producción para api_challenge
ARG PYTHON_TAG=3.7

FROM python:${PYTHON_TAG} as poetry

RUN pip install poetry

RUN poetry config virtualenvs.create false

WORKDIR /app
COPY ./api_challenge ./api_challenge
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

## Install model requeriments
COPY ./model_environments ./model_environments
RUN pip install -r model_environments/requirements.txt

ENTRYPOINT [ "sh" ] 
CMD [ "-c", "serve" ]
