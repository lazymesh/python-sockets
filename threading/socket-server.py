import socket
import threading

host = '127.0.0.1'
port = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handler(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

    
def receive():
    while True:
        client, address = sock.accept()
        print(f'Connected wtih {str(address)}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('utf-8')
        print(nickname)
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to the server'.encode('ascii'))
        
        thread = threading.Thread(target=handler, args=(client,))
        thread.start()

print('Server is listening')
receive()