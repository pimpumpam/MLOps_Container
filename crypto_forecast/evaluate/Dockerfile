# Model Evaluate
FROM pytorch/pytorch

RUN apt-get update && apt-get install -y git

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DB_HOST=crypto_database
ENV DB_PORT=3306
ENV DB_USER=pimpumpam
ENV DB_PASSWORD=kwsxfk8332
ENV DB_NAME=crypto_currency

CMD ["python", "run.py"]

# 이미지 빌드
# $ docker build -t crypto_evaluate_image .

# 컨테이너 실행
# $ docker run -it --name crypto_evaluate -v static_volume:/app/static -v mlflow_volume:/app/mlruns --network crypto_network crypto_evaluate_image