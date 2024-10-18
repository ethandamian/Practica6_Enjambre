import random
import socket
import _thread
import pickle
from game import Game

# Define the ip address of the server and the port
server = "localhost"
port = 5555 # Safe port

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port)) # Bind the server to the port
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")

connected = set() # Store the ip addresses of the connected clients
games = {} # Store the games that are being played
idCount = 0 # The number of clients connected


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))  # Send the id of the player (0 for human, 1 for AI)

    reply = ""
    while True:
        try:
            data = conn.recv(2048*2).decode()  # Receive data from the client
            if gameId in games:  # If the game exists
                game = games[gameId]

                if not data:  # If no data is received, exit the loop
                    break
                else:
                    if data == "reset":  # If the client wants to reset the game
                        game.resetWent()
                    elif data != "get":  # If the client is not asking for the game state
                        game.player(p, data)  # Player 0 makes their move

                        # If the AI needs to make a move
                        if p == 0 and not game.p2Went:
                            ai_move = random.choice(["Rock", "Paper", "Scissors"])
                            game.player(1, ai_move)  # AI is player 1

                    reply = game  # Update the game state

                    conn.sendall(pickle.dumps(reply))  # Send the updated game state to the client
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    idCount += 1
    p = 0  # Player 0 will always be the human player
    gameId = idCount - 1  # Create a new game for each connection

    games[gameId] = Game(gameId)
    games[gameId].ready = True  # AI is always "ready"

    print("Creating a new game with AI...")
    _thread.start_new_thread(threaded_client, (conn, p, gameId))  # Start a new thread for the client
