import socket
import threading
import time

def send_messages(sock):
    while True:
        message = input()
        sock.sendall(message.encode("utf-8"))

def receive_messages(sock):
    while True:
        response = sock.recv(16384).decode("utf-8")
        if not response:
            break
        print(f"Server response: {response}")

def simulate_dos_attack(sock):
    while True:
        message = "a" * 16384
        sock.sendall(message.encode("utf-8"))
        time.sleep(0.01)

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    
    mode = input("Choose mode (1 - Normal, 2 - DOS attack): ")
    if mode == "1":
        print("Enter your messages and the server will reply :)")
        send_thread = threading.Thread(target=send_messages, args=(client_socket,))
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    elif mode == "2":
            send_thread = threading.Thread(target=simulate_dos_attack, args=(client_socket,))
            receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    else:
        print("Invalid mode.")
        exit(1)

    send_thread.start()
    receive_thread.start()
    send_thread.join()
    receive_thread.join()
    client_socket.close()
