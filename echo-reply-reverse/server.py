import socket
import threading

def handle_client(client_socket, addr):
    print(f"Client {addr} connected.")
    while True:
        message = client_socket.recv(16384).decode("utf-8")
        if not message:
            break
        inverted_message = message[::-1]
        client_socket.sendall(inverted_message.encode("utf-8"))
    print(f"Client {addr} disconnected.")
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")
    while True:
        client_socket, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()