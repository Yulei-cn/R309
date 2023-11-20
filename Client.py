import socket
import threading
import sys

#SERVER_HOST = 'localhost'
SERVER_HOST = '10.128.200.7'
SERVER_PORT = 8000
BUFFER_SIZE = 1024

def handle_input(client_socket):
    """处理用户输入"""
    try:
        while True:
            msg = input(f'[{name}] ')
            client_socket.send(msg.encode())
            if msg == 'bye':
                break
    except EOFError:
        pass


def handle_output(client_socket):
    """处理消息输出"""
    while True:
        msg = client_socket.recv(BUFFER_SIZE)
        if msg.decode() == 'bye':
            break
        print(msg.decode())

if __name__ == '__main__':
    name = input("S'il vous plaît, entrez votre nom: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # 发送昵称
    name_bytes = name.encode()
    client_socket.send(name_bytes)

    # 开启线程用来接收服务器发送的消息
    thread_output = threading.Thread(target=handle_output, args=(client_socket,))
    thread_output.start()

    # 开启线程用来处理用户输入的消息
    thread_input = threading.Thread(target=handle_input, args=(client_socket,))
    thread_input.start()

