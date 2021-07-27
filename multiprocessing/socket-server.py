import socket
import threading
import time

host = '127.0.0.1'
port = 55555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

clients = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handler(client):
    while True:
        try:
            message = "message from server".encode('ascii')
            time.sleep(1)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

    
def receive():
    while True:
        client, address = sock.accept()
        print(f'Connected wtih {str(address)}')

        clients.append(client)

        client.send('Connected to the server'.encode('ascii'))
        
        thread = threading.Thread(target=handler, args=(client,))
        thread.start()

if __name__ == "__main__":
    print('Server is listening')
    receive()