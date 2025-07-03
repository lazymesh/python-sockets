import socket
from handle_clients import receive

host = '127.0.0.1'
port = 9071

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

if __name__ == "__main__":
    print('Server is listening')
    receive(sock)