import socket
import _thread
import pickle
from game import Game


def threaded_client(conn, p, gameId):
    global games
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(2048).decode()
            if gameId in games:
                game = games[gameId]

                if data == "get":
                    conn.sendall(pickle.dumps(game))
                elif data == "reset":
                    print("Reiniciando juego...")
                    game.reset()
                    conn.sendall(pickle.dumps(game))
                else:
                    # Humano
                    if game.turn == 0 and game.make_move(0, int(data)):
                        game.turn = 1  # Turno de la IA
                        if not game.check_winner():
                            ai_move = game.best_move()
                            game.make_move(1, ai_move)  # IA hace su movimiento
                            if game.check_winner():
                                game.turn = -1
                            game.turn = 0

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    del games[gameId]
    conn.close()


# server = "192.168.1.91"
server = "localhost"
port = 5555


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen()

print("Servidor iniciado...")

games = {}
idCount = 0

while True:
    conn, addr = s.accept()
    print(f"Conectado a: {addr}")

    idCount += 1
    games[idCount] = Game(idCount)
    games[idCount].ready = True

    # 0 representa al jugador humano
    _thread.start_new_thread(threaded_client, (conn, 0, idCount))
