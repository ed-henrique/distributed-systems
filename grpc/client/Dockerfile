FROM python:3-slim

WORKDIR /app

RUN apt-get install -y openssl && \
    mkdir /app/certs

COPY client/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY client/test.sh ./test.sh
COPY client/client.py ./client.py
COPY proto/my_service_pb2.py ./my_service_pb2.py
COPY proto/my_service_pb2_grpc.py ./my_service_pb2_grpc.py

RUN echo "alias client='python /app/client.py'" >> ~/.bashrc

EXPOSE 50051

VOLUME /app/certs