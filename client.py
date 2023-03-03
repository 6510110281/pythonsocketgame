import socket

HOST = "127.0.0.1"
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    guess = input("Guess the number between 1 and 100: ")
    client_socket.send(guess.encode())
    hint = client_socket.recv(1024).decode()
    print(hint)
    if "Congratulations" in hint or "Sorry" in hint:
        break

client_socket.close()
