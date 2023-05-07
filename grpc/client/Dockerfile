FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY test.sh /usr/src/app/test.sh
COPY client.py /usr/src/app/client.py
COPY command_service_pb2.py /usr/src/app/command_service_pb2.py
COPY command_service_pb2_grpc.py /usr/src/app/command_service_pb2_grpc.py

CMD [ "python", "/usr/src/app/client.py", "-c", "\"ls -al\"" ]
CMD [ "python", "/usr/src/app/client.py", "-s", "test.sh" ]