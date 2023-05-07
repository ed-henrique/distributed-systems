import grpc
import click
import command_service_pb2
import command_service_pb2_grpc

@click.command()
@click.option('-c', '--command', 'command', help='Command to execute.')
@click.option('-s', '--script', 'script_path', default=None, help='Path to script file.', show_default=True)
def run(command, script_path):
    """A client program to execute commands remotely on a Linux server. Use --script to pass a script file to run, or simply pass your command between double quotes.\n
    Examples:\n
        client.py "COMMAND"\n
          Pass  a command to execute on the server.\n
        client.py --script="SCRIPT_PATH"\n
          Pass script as a command to execute on the server.
    """

    with grpc.insecure_channel("localhost:50051") as channel:
        if (script_path):
            with open(script_path, "r") as file:
                request = file.read()
        else:
            request = command
            
        stub = command_service_pb2_grpc.CommandServiceStub(channel)
        response = stub.RunCommand(command_service_pb2.CommandRequest(command=request))
        click.echo(response.output)

if __name__ == "__main__":
    run()