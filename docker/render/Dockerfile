FROM python:3.12-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


# Install poetry and python packages
COPY poetry.lock pyproject.toml ./
RUN curl -sSL https://install.python-poetry.org | python3.12 \
    && python3 -m venv /opt/venv \
    && python3 -m pip install pip --upgrade \
    && rm -rf /var/cache/yum /Python-3.12
ENV PATH="/opt/venv/bin:/root/.poetry/bin:/opt/app-root/src/.poetry/bin/:/root/.local/bin:${PATH}"
RUN . /opt/venv/bin/activate \
    && /opt/venv/bin/python3.12 -m pip install --upgrade pip \
    && /opt/venv/bin/pip install poetry gunicorn uvicorn \
    && /opt/venv/bin/poetry install


COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
EXPOSE 8000

RUN alembic upgrade head
ENTRYPOINT uvicorn app.main:app --reload --port 8011
