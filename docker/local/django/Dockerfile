# Use a multi-stage build to reduce image size
FROM python:3.12-slim as base

# Set environment variables
# PYTHONUNBUFFERED ensures that Python output is sent directly to the terminal without buffering, useful for real-time logging.
# PYTHONDONTWRITEBYTECODE prevents Python from creating .pyc files, reducing unnecessary writes in the container.
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl ca-certificates gettext && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /src

# Copy dependency files
COPY alembic.ini uv.lock pyproject.toml alembic ./docker/local/django/entrypoint ./docker/local/django/start /src/
COPY alembic /src/alembic

# Install uv package manager
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Add uv to PATH
ENV PATH="/src/.venv/bin:/root/.local/bin:$PATH"

# Install Python dependencies
RUN uv sync

# Copy entrypoint and start scripts
RUN sed -i 's/\r$//g' /src/entrypoint /src/start && \
    chmod +x /src/entrypoint /src/start

# Expose application port
EXPOSE 8000


FROM base as production

# Copy application code
COPY app /src/app