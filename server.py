import socket


HOST = "127.0.0.1"
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()

print("Server started. Waiting for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Client connected:", client_address)
