import socket
import json

# Configurazione del client
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

# Funzione per inviare richieste al server
def send_request(command, data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        # Preparazione del messaggio
        message = json.dumps({"command": command, **data})
        client_socket.sendall(message.encode('utf-8'))

        # Ricezione della risposta
        response = client_socket.recv(1024)
        return json.loads(response.decode('utf-8'))

# Menu per interagire con il server
def client_menu():
    print("Client File Sharing")
    while True:
        print("\nOpzioni disponibili:")
        print("1. Verifica se un file esiste")
        print("2. Recupera il numero di frammenti di un file")
        print("3. Recupera l'host di un frammento di un file")
        print("4. Recupera tutti gli host di un file")
        print("5. Esci")
        choice = input("Scegli un'opzione: ")

        if choice == "1":
            file_name = input("Inserisci il nome del file: ")
            response = send_request("check_file", {"file_name": file_name})
            print(f"Esiste: {response.get('exists')}")

        elif choice == "2":
            file_name = input("Inserisci il nome del file: ")
            response = send_request("get_fragment_count", {"file_name": file_name})
            print(f"Numero di frammenti: {response.get('fragment_count')}")

        elif choice == "3":
            file_name = input("Inserisci il nome del file: ")
            fragment_number = int(input("Inserisci il numero del frammento: "))
            response = send_request("get_fragment_host", {"file_name": file_name, "fragment_number": fragment_number})
            print(f"Host del frammento: {response.get('host')}")

        elif choice == "4":
            file_name = input("Inserisci il nome del file: ")
            response = send_request("get_all_hosts", {"file_name": file_name})
            print(f"Host dei frammenti: {response.get('hosts')}")

        elif choice == "5":
            print("Chiusura del client.")
            break

        else:
            print("Scelta non valida. Riprova.")

# Avvio del client
if __name__ == "__main__":
    client_menu()
