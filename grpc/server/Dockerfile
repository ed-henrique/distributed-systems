FROM python:3

WORKDIR /usr/src/app

RUN apt-get install -y openssl

COPY server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server/server.py ./server.py
COPY proto/my_service_pb2.py ./my_service_pb2.py
COPY proto/my_service_pb2_grpc.py ./my_service_pb2_grpc.py
COPY keys/server.key ./server.key
COPY keys/server.crt ./server.crt

EXPOSE 50051

CMD [ "python", "/usr/src/app/server.py" ]