from socket import *

server_port = 9999
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('127.0.0.1',server_port))

while True:
    message, client_addr = server_socket.recvfrom(1024)
    print(message.decode())
    server_socket.sendto((message.decode().upper()).encode(), client_addr)
server_socket.close()