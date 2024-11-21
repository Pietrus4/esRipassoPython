import socket
import threading
import sqlite3
import json

# Configurazione del server
HOST = '127.0.0.1'
PORT = 65432
DB_PATH = "file.db"  # Percorso al database SQLite

# Funzione per gestire ogni client
def handle_client(conn, addr):
    print(f"Connessione stabilita con {addr}")
    try:
        while True:
            # Ricezione dati dal client
            data = conn.recv(1024)
            if not data:
                break

            # Decodifica e parsing del messaggio
            message = json.loads(data.decode('utf-8'))
            command = message.get("command")
            response = {}

            # Connettersi al database
            with sqlite3.connect(DB_PATH) as conn_db:
                cursor = conn_db.cursor()

                # Gestione delle varie richieste
                if command == "check_file":
                    # Controlla se un file esiste
                    file_name = message.get("file_name")
                    cursor.execute("SELECT id_file FROM files WHERE nome = ?", (file_name,))
                    result = cursor.fetchone()
                    response = {"exists": result is not None}

                elif command == "get_fragment_count":
                    # Recupera il numero di frammenti di un file
                    file_name = message.get("file_name")
                    cursor.execute("SELECT tot_frammenti FROM files WHERE nome = ?", (file_name,))
                    result = cursor.fetchone()
                    response = {"fragment_count": result[0] if result else None}

                elif command == "get_fragment_host":
                    # Recupera l'host di un frammento specifico
                    file_name = message.get("file_name")
                    fragment_number = message.get("fragment_number")
                    cursor.execute("""
                        SELECT f.host FROM frammenti f
                        JOIN files fi ON fi.id_file = f.id_file
                        WHERE fi.nome = ? AND f.n_frammento = ?
                    """, (file_name, fragment_number))
                    result = cursor.fetchone()
                    response = {"host": result[0] if result else None}

                elif command == "get_all_hosts":
                    # Recupera tutti gli host che ospitano i frammenti di un file
                    file_name = message.get("file_name")
                    cursor.execute("""
                        SELECT f.host FROM frammenti f
                        JOIN files fi ON fi.id_file = f.id_file
                        WHERE fi.nome = ?
                    """, (file_name,))
                    result = cursor.fetchall()
                    response = {"hosts": [row[0] for row in result] if result else []}

                else:
                    response = {"error": "Comando non riconosciuto"}

            # Invio della risposta al client
            conn.sendall(json.dumps(response).encode('utf-8'))

    except Exception as e:
        print(f"Errore nella connessione con {addr}: {e}")
    finally:
        conn.close()

# Configurazione del server TCP
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server in ascolto su {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            # Gestione di ogni connessione in un thread separato
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"Thread avviato per {addr}")

# Avvio del server
if __name__ == "__main__":
    start_server()
