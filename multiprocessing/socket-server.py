import socket
from handle_clients import receive

host = '127.0.0.1'
port = 9070

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    print('Server is listening')
    receive(sock)