import multiprocessing as mp
import time



def broadcast(message, clients):
    for client in clients:
        client.send(message)

def handler(clients, client):
    while True:
        try:
            message = f"message from server {client}".encode('ascii')
            time.sleep(1)
            broadcast(message, clients)
        except:
            clients.remove(client)
            client.close()
            break

    
def receive(sock):
    with mp.Manager() as manager:
        clients = manager.list()
        while True:
            print("receive is reached")
            client, address = sock.accept()
            print(f'Connected wtih {str(address)}')

            clients.append(client)

            client.send('Connected to the server'.encode('ascii'))
            
            mProcess = mp.Process(target=handler, args=(clients, client))
            mProcess.start()