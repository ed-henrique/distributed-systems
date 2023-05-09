FROM python:3

WORKDIR /usr/src/app

RUN apt-get install -y openssl

COPY client/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY client/test.sh ./test.sh
COPY client/client.py ./client.py
COPY proto/my_service_pb2.py ./my_service_pb2.py
COPY proto/my_service_pb2_grpc.py ./my_service_pb2_grpc.py
COPY keys/server.crt ./server.crt

CMD [ "python", "/usr/src/app/client.py", "-c", "\"ls -al\"" ]
CMD [ "python", "/usr/src/app/client.py", "-s", "test.sh" ]