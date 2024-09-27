import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
BUFFER_SIZE = 4092

while True:
    # Invio messaggio al server
    message = input("Client: ")
    try:
        client_socket.send(message.encode('utf-8'))
    except:
        print("Errore durante l'invio del messaggio")
        break

    # Ricezione messaggio dal server
    try:
        message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        if not message:
            print("Il server si è disconnesso")
            break
        print(f"Server: {message}")
    except:
        print("Errore durante la ricezione del messaggio")
        break

client_socket.close()
