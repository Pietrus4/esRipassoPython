# 1: forward, 2: backward, 3: right, 4: left, value: 0/100, setPWMA, setPWMB
import socket

commands_list = {"forward": 1, "backward":2, "right":3, "left":4}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.136', 6971))
BUFFER_SIZE = 4092

client_socket.send(' '.encode("utf-8"))

while True:
    message = input("inserire comando valore : ")
    command, value = message.split(" ")
    while 0 < int(command) > 5 or 0 < int(value) > 100:
        print(f"oh scemo, metti uno fra questi comandi: {commands_list}")
        message = input("inserire comando valore : ")
        command, value = message.split(" ")

    try:
        client_socket.send(message.encode('utf-8'))
    except:
        print("Abbiamo un problema...")
        break

client_socket.close()