import grpc
import subprocess
from concurrent import futures
import command_service_pb2
import command_service_pb2_grpc

class CommandService(command_service_pb2_grpc.CommandServiceServicer):
    def RunCommand(self, request, context):
        try:
            result = subprocess.check_output(request.command.split(' '), stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            result = e.output
        return command_service_pb2.CommandResponse(output=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    command_service_pb2_grpc.add_CommandServiceServicer_to_server(CommandService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()