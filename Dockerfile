FROM python:3.12.2-slim


ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc-dev \
    libreoffice \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .


RUN python -m pip install --upgrade pip==23.3.1 && python -m pip install -r requirements.txt


COPY main.py .
COPY docbot/ ./docbot/


CMD ["python", "main.py"]
