import grpc
import click
import my_service_pb2
import my_service_pb2_grpc

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

    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()

    credentials = grpc.ssl_channel_credentials(
        root_certificates=certificate_chain
    )

    with grpc.secure_channel("Eduardo Machado:50051", credentials) as channel:
        stub = my_service_pb2_grpc.AuthenticationServiceStub(channel)
        request = my_service_pb2.AuthenticationRequest(username='username', password='password')
        response = stub.Authenticate(request)
        
        if (response.success):
            if (script_path):
                with open(script_path, "r") as file:
                    request = file.read()
            else:
                request = command
                
            stub = my_service_pb2_grpc.CommandServiceStub(channel)
            response = stub.RunCommand(my_service_pb2.CommandRequest(command=request))
            click.echo(response.output)
        else:
            click.echo("You are not authenticated!")

if __name__ == "__main__":
    run()