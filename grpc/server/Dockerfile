FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py /usr/src/app/server.py
COPY command_service_pb2.py /usr/src/app/command_service_pb2.py
COPY command_service_pb2_grpc.py /usr/src/app/command_service_pb2_grpc.py

CMD [ "python", "/usr/src/app/server.py" ]