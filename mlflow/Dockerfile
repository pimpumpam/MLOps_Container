# MLFlow Server
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV BACKEND_STORE_URI=sqlite:////app/mlflow.db
ENV ARTIFACT_ROOT=/app/mlruns

EXPOSE 8081

CMD ["mlflow", "server", "--backend-store-uri", "sqlite:////app/mlflow.db", "--default-artifact-root", "/app/mlruns", "--host", "0.0.0.0", "--port", "8081"]


# 이미지 빌드
# $ docker build -t mlflow_image .

# 컨테이너 실행
# docker run -d --name mlflow --network crypto_network -p 8081:8081 mlflow_image