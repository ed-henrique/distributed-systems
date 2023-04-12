import sys
import socket
import threading
import base64

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

def receive():
    while True:
        try:
            data = s.recv(2048)
            
            if not data:
                break
            else:
                decoded_data = base64.b64decode(data).decode('ascii')
                sys.stdout.write('\033[K' + decoded_data + '\r\n')
        except:
            s.close()
            exit()

def send():
    while True:
        try:
            message = input().encode('ascii')
            base64_bytes = base64.b64encode(message)
            s.sendall(base64_bytes)
        except:
            s.close()
            exit()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
