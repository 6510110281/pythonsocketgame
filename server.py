import socket
import random 

HOST = "127.0.0.1"
PORT = 8888

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen()

print("Server started. Waiting for connections...")

class NumberGuessingGame:
    def __init__(self):
        self.number = None
        self.attempts = 0

    def play_game(self, client):
        self.number = random.randint(1, 100)
        self.attempts = 0
        print("Client connected:", client_address)
        while self.attempts < 10:
            guess = client.recv(1024).decode()
            print("Client {} says: {}".format(client.getpeername(), guess))
            if guess == str(self.number):
                client.send("Congratulations! You guessed the number in {} attempts!".format(self.attempts+1).encode())
                return
            else:
                self.attempts += 1
                if self.attempts < 10:
                    if int(guess) < self.number:
                        client.send("Try a higher number. You have {} attempts left.".format(10-self.attempts).encode())
                    else:
                        client.send("Try a lower number. You have {} attempts left.".format(10-self.attempts).encode())
                else:
                    client.send("Sorry, you have run out of attempts. The number was {}.".format(self.number).encode())

while True:
    client_socket, client_address = server_socket.accept()
    game = NumberGuessingGame()
    game.play_game(client_socket)