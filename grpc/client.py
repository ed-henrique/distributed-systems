import grpc
import command_service_pb2
import command_service_pb2_grpc

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        request = input("Command to run: ")
        stub = command_service_pb2_grpc.CommandServiceStub(channel)
        response = stub.RunCommand(command_service_pb2.CommandRequest(command=request))
        print(response.output)

if __name__ == "__main__":
    run()