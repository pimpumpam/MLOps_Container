# MLflow 서버 실행을 위한 기본 이미지 선택
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 패키지 설치
RUN pip install mlflow boto3 psycopg2-binary

# 환경 변수 설정 (MLflow 데이터 저장 위치 지정)
ENV BACKEND_STORE_URI=sqlite:////app/mlflow.db
ENV ARTIFACT_ROOT=/app/mlruns

# MLflow 서버 실행
CMD ["mlflow", "server", "--backend-store-uri", "sqlite:////app/mlflow.db", "--default-artifact-root", "/app/mlruns", "--host", "0.0.0.0", "--port", "8081"]


# 이미지 빌드
# $ docker build -t databricks/mlflow .

# 컨테이너 실행
# docker run -d --name mlfow -p 8081:8081 databricks/mlflow