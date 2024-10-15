import socket
import _thread
import pickle
from game import Game


def threaded_client(conn, p, gameId):
    global games
    conn.send(str.encode(str(p)))  # Send player ID (0 = human)

    while True:
        try:
            data = conn.recv(2048).decode()

            if gameId in games:
                game = games[gameId]

                if data == "get":
                    conn.sendall(pickle.dumps(game))  # Send the game state
                elif data == "reset":
                    print("Reiniciando juego...")
                    game.reset()
                    # Send the reset game state
                    conn.sendall(pickle.dumps(game))
                else:
                    # Human move
                    # Player is human
                    if game.turn == 0 and game.make_move(0, int(data)):
                        if game.check_winner():  # Check if human won
                            game.turn = -1  # Game over, no more moves
                        else:
                            # AI makes its move
                            game.turn = 1  # Switch to AI
                            ai_move = game.best_move()  # MinMax AI calculates the best move
                            game.make_move(1, ai_move)  # AI makes its move

                            if game.check_winner():  # Check if AI won
                                game.turn = -1  # Game over
                            else:
                                game.turn = 0  # Switch back to human turn

                    # Send the updated game state
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    del games[gameId]  # Clean up the game if disconnected
    conn.close()


# Server settings
server = "localhost"  # Localhost for testing
port = 5555  # Port number

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen()

print("Servidor de Connect 4 iniciado...")

games = {}  # Dictionary to hold all active games
idCount = 0  # Game ID counter

while True:
    conn, addr = s.accept()
    print(f"Conectado a: {addr}")

    idCount += 1  # Increment game ID for each new connection
    games[idCount] = Game(idCount)  # Create a new game
    games[idCount].ready = True  # Mark the game as ready

    # Start a new thread for the client connection
    _thread.start_new_thread(
        threaded_client, (conn, 0, idCount))  # Human is player 0
