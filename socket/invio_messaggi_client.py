import socket

server_address = ('localhost', 6969)
BUFFER_SIZE = 4092

udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_DGRAM --> indica che è UDP
udp_server_socket.bind(server_address)
print("Server listening on")
data, address_client = udp_server_socket.recvfrom(BUFFER_SIZE) #bloccante finchè non riceve una risposta

print(f"Messaggio ricevuto {data.decode(encoding='utf-8')} da {address_client}")

response = "SMETTILA DI PINGARMI!"

udp_server_socket.sendto(response.encode('utf-8'), address_client)

udp_server_socket.close()
