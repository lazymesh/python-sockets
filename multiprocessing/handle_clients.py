import multiprocessing as mp
import time

clients = []

def broadcast(message):
    print("elients")
    for client in clients:
        client.send(message)

def handler(client):
    print('finding out error pint')
    while True:
        try:
            message = "message from server".encode('ascii')
            time.sleep(1)
            print(message)
            broadcast(message)
        except:
            clients.remove(client)
            client.close()
            break

    
def receive(sock):
    while True:
        print("receive is reached")
        client, address = sock.accept()
        print(f'Connected wtih {str(address)}')

        clients.append(client)

        client.send('Connected to the server'.encode('ascii'))
        
        mProcess = mp.Process(target=handler, args=(client,))
        mProcess.start()