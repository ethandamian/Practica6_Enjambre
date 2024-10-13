import pickle
import socket
from _thread import *

from RPSGame import RPSGame

server = "10.11.250.207"
port = 5555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    socket.bind((server, port))
except Exception as e:
    str(e)

socket.listen()
print("[SERVER] Server Started")
print("[SERVER] Waiting for a connection...")

games = {}
idCount = 0

def connected_game(connection, player, gameID):
    """
    Start a new game depending of the sended data
    :param connection: Connection
    :param player: Int
    :param gameID: Int
    """
    global idCount
    connection.send(str.encode(str(player)))
    reply = ""

    while True:
        try:

            data = connection.recv(4096).decode()

            if gameID in games:
                game = games[gameID]

                if not data:
                    break
                else:
                    # If the server receives "reset", reset the moves of the game
                    if data == "reset":
                        game.reset_moves()
                    # If the server do not receive "get" and the game is not ready, set the move of the player
                    elif data != "get":
                        game.play(player, data)

                    reply = game

                    connection.sendall(pickle.dumps(reply))
            else:
                break
        except:
            break
    print("[SERVER] Lost connection")
    print("[SERVER] Closing game with ID", gameID)
    try:
        del games[gameID]
        print("[SERVER] Game closed")
    except:
        pass
    idCount -= 1
    connection.close()

while True:
    connection, adress = socket.accept()
    print("[SERVER] Connected to:", adress)

    idCount += 1
    player = 0 
    gameID = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameID] = RPSGame(gameID)
        print("[SERVER] Creating a new game...")
    else:
        games[gameID].ready = True
        player = 1

    start_new_thread(connected_game, (connection, player, gameID))