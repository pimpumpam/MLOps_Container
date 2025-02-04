FROM pytorch/pytorch

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV DB_HOST=mysql
ENV DB_PORT=3306
ENV DB_USER=pimpumpam
ENV DB_PASSWORD=kwsxfk8332
ENV DB_NAME=crypto_currency

CMD ["python", "run.py"]

# 이미지 빌드
# $ docker build -t crypto_train_image .

# 컨테이너 실행
# $ docker run -d --name crypto_train --link crypto_database:mysql crypto_train_image