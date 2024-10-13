import socket
import _thread
import pickle
from game import Game

# Define the ip address of the server and the port
server = "192.168.1.91"
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
    conn.send(str.encode(str(p))) # Send the id of the player to the client

    reply = ""
    while True:
        try:
            data = conn.recv(2048*2).decode() # Receive data from the client
            if gameId in games: # If the game exists
                game = games[gameId] 

                if not data: # If we don't receive any data
                    break
                else:
                    if data == "reset": # If the client wants to reset the game
                        game.resetWent()
                    elif data != "get": # If the client is not asking for the data
                        game.player(p, data)

                    reply = game

                    conn.sendall(pickle.dumps(reply)) # Send data to the client
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
    p=0
    gameId = (idCount - 1)//2 # Every 2 people that connect to the server we are going to have a new game
    if idCount % 2 == 1: # If the number of clients connected is odd, we are going to create a new game
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    _thread.start_new_thread(threaded_client, (conn, p, gameId)) # Start a new thread for the client