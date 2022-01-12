from socket import *

server_addr = '127.0.0.1'
server_port = 9999
client_socket = socket(AF_INET, SOCK_DGRAM)

message = 'hello world'

client_socket.sendto(message.encode(),(server_addr, server_port))
message, recv_addr = client_socket.recvfrom(1024)

print(message.decode())
client_socket.close()