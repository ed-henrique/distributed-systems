FROM python:3-slim

WORKDIR /app

RUN apt-get install -y openssl && \
    mkdir -p /app/certs && \
    openssl req -newkey rsa:2048 -nodes -keyout /app/certs/server.key -x509 -days 365 -out /app/certs/server.crt -subj "/CN=server"

COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server/server.py ./server.py
COPY proto/my_service_pb2.py ./my_service_pb2.py
COPY proto/my_service_pb2_grpc.py ./my_service_pb2_grpc.py

EXPOSE 50051

VOLUME /app/certs

CMD [ "python", "/app/server.py" ]
