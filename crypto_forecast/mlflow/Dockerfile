# MLFlow Server

# docker-compose에서 컨테이너 띄울 때 아래 설정 값 사용
FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

RUN cd /tmp && \
    wget https://dl.min.io/client/mc/release/linux-amd64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc


# Dockerfile로 이미지와 컨테이너 띄울 때 아래 설정 값 사용
# FROM python:3.9

# RUN apt-get update && apt-get install -y git

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . /app

# ENV BACKEND_STORE_URI=sqlite:////app/mlflow.db
# ENV ARTIFACT_ROOT=/app/mlruns

# EXPOSE 8081

# CMD ["mlflow", "server", "--backend-store-uri", "sqlite:////app/mlflow.db", "--default-artifact-root", "/app/mlruns", "--host", "0.0.0.0", "--port", "8081"]


# 이미지 빌드
# $ docker build -t mlflow_image .

# 컨테이너 실행
# docker run -d --name mlflow --network crypto_network -p 8081:8081 -v mlflow_volume:/app/mlruns mlflow_image