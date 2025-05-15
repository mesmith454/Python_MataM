#Stage 1: Build Stage
FROM python:3.13-slim AS builder

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3.13-slim
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

#copy dependencies from build stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /app

#Copy app code
COPY --chown=appuser:appuser . .

#set env vars to optimize python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# switch to non root user
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "docker_django_app.wsgi:application"]