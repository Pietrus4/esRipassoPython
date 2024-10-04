import socket
BUFFER_SIZE = 4092

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.1.136', 6969)

message = "TI STO PINGANDO"

#mandare 10 messaggi
for i in range(10):
    client_socket.sendto(message.encode(), server_address)

data, server = client_socket.recvfrom(BUFFER_SIZE)
print(f"Risposta dal server: {data.decode('utf-8')}")

client_socket.close()