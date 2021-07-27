import socket
import multiprocessing as mp

def receive(connectedClient):
    while True:
        try:
            message = connectedClient.recv(1024).decode('ascii')
            print(message)
        except:
            print('An error occured')
            connectedClient.close()
            break

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))
    client_process = mp.Process(target=receive, args=(client))
    client_process.start()