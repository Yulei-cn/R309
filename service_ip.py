import socket
import threading
from functools import partial


SERVER_HOST = '10.128.200.7'
SERVER_PORT = 8000
BUFFER_SIZE = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f'[*] Écoute du port {SERVER_PORT}')

clients = []

def handle_message(sender_name, sender_ip, msg, sender_socket):
    formatted_msg = f'[{sender_name} - {sender_ip}] {msg}'
    for client in clients:
        client_socket, _, name, _ = client
        if client_socket != sender_socket:
            client_socket.send(formatted_msg.encode())

def handle_client(client_socket, client_address):
    name = client_socket.recv(BUFFER_SIZE).decode()
    print(f'[*] {name} Connecté depuis {client_address[0]}:{client_address[1]}')
    welcome = f'Bienvenue dans le salon de discussion, {name}!\n'.encode()
    client_socket.send(welcome)
    clients.append((client_socket, client_address, name, ""))

    while True:
        msg = client_socket.recv(BUFFER_SIZE)
        if msg.decode() == 'bye':
            print(f'[*] {name} Déconnecté depuis {client_address[0]}:{client_address[1]}')
            client_socket.close()
            clients.remove((client_socket, client_address, name, ""))
            break
        elif msg.decode() == 'arret':
            print('Fermeture du serveur')
            for client in clients:
                client_socket, client_address, name, _ = client
                client_socket.close()
            server_socket.close()
            break
        elif msg.decode() != 'bye' and msg.decode() != 'arret':
            print(f'[*] Envoi d\'un message au client {name}')
            partial_message = partial(handle_message, name, client_address[0], msg.decode(), client_socket)
            thread_message = threading.Thread(target=partial_message)
            thread_message.start()

def server_send_messages():
    while True:
        server_msg = input("Envoi d'un message au client：")
        split_msg = server_msg.split(' ', 1)
        if len(split_msg) == 2:
            recipient_ip, actual_msg = split_msg
            sent = False
            for client in clients:
                client_socket, client_address, _, _ = client
                if client_address[0] == recipient_ip:
                    client_socket.send(actual_msg.encode())
                    sent = True
                    break
            if not sent:
                print(f"Aucun client avec l'adresse IP {recipient_ip} trouvé.")
        else:
            print("Format incorrect. Utilisez la syntaxe suivante : 'ip message'.")

while True:
    client_socket, client_address = server_socket.accept()
    

    thread_client = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread_client.start()

    server_msg_thread = threading.Thread(target=server_send_messages)
    server_msg_thread.start()
