import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server in ascolto su localhost:12345")

client_socket, client_address = server_socket.accept()
print(f"Connessione stabilita con: {client_address}")

while True:
    # Ricezione messaggio dal client
    try:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print("Il client si è disconnesso")
            break
        print(f"Client: {message}")
    except:
        print("Errore durante la ricezione del messaggio")
        break

    # Invio messaggio al client
    message = input("Server: ")
    try:
        client_socket.send(message.encode('utf-8'))
    except:
        print("Errore durante l'invio del messaggio")
        break

client_socket.close()
server_socket.close()