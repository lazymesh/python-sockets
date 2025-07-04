import socket

def receive(connectedClient):
    message = "waiting to receive data"
    while True and len(message) != 0:
        try:
            message = connectedClient.recv(1024).decode('ascii')
            print(message)
        except:
            print('An error occured')
            connectedClient.close()
            break
    print("connection to server broken")

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9070))
    receive(client)