import sys
import socket
import threading


HOST = '127.0.0.1'
PORT = 7538
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    while True:
        client_socket, address = server.accept()
        print('connected:', address)
        server_send(client_socket)
def server_send(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        else:
            client_socket.send(f"serverwrite: {data}".encode("utf-8"))
    client_socket.close()

start_server()