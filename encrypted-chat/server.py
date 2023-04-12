import socket
import threading
import base64

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

s.listen()

clients = []

nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            index = clients.index(client)
            nickname = nicknames[index]

            message = client.recv(2048)
            decoded_message = nickname + ': ' + base64.b64decode(message).decode('ascii')
            encoded_message = base64.b64encode(decoded_message.encode('ascii'))
            broadcast(encoded_message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            message = f'{nickname} saiu do chat!'
            print(message)
            encoded_message = base64.b64encode(message.encode('ascii'))
            broadcast(encoded_message)
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = s.accept()
        print(f'Conectado com {str(address)}')

        encoded_message = base64.b64encode('Como voce prefere ser identificado?'.encode('ascii'))

        client.send(encoded_message)
        nickname = base64.b64decode(client.recv(2048)).decode('ascii')

        nicknames.append(nickname)
        clients.append(client)

        print(f'Nome do cliente eh {nickname}!')

        encoded_message = base64.b64encode(f'{nickname} entrou no chat!'.encode('ascii'))
        broadcast(encoded_message)

        encoded_message = base64.b64encode('Conectado ao servidor!'.encode('ascii'))
        client.send(encoded_message)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()