import grpc
import subprocess
from concurrent import futures
import my_service_pb2
import my_service_pb2_grpc


class AuthenticationService(my_service_pb2_grpc.AuthenticationServiceServicer):
    def Authenticate(self, request, context):
        success = request.username == 'username' and request.password == 'password'
        return my_service_pb2.AuthenticationResponse(success=success)

class CommandService(my_service_pb2_grpc.CommandServiceServicer):
    def RunCommand(self, request, context):
        try:
            result = subprocess.check_output(request.command.split(' '), stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        return my_service_pb2.CommandResponse(output=result)

def serve():
    with open('certs/server.key', 'rb') as f:
        private_key = f.read()
    with open('certs/server.crt', 'rb') as f:
        certificate_chain = f.read()
    
    credentials = grpc.ssl_server_credentials([(private_key, certificate_chain)])

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    my_service_pb2_grpc.add_AuthenticationServiceServicer_to_server(
        AuthenticationService(), server
    )

    my_service_pb2_grpc.add_CommandServiceServicer_to_server(CommandService(), server)
    
    server.add_secure_port("[::]:50051", credentials)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()