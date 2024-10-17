import socket
import _thread
import pickle
from game import HangmanGame

# Servidor que maneja los clientes


def threaded_client(conn, game):
    # Enviar el estado inicial del juego
    conn.send(pickle.dumps(game.__dict__))

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            else:
                if data == "reset":
                    game.reset()
                elif data != "get":
                    game.guess(data)
                # Enviar el estado actualizado
                conn.sendall(pickle.dumps(game.__dict__))
        except:
            break

    conn.close()


# Configuración del servidor
# server = "10.215.9.175"#"192.168.1.91"
server = "localhost"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Esperando conexión... Servidor iniciado.")

while True:
    conn, addr = s.accept()
    print("Conectado a:", addr)

    game = HangmanGame()  # Crear un nuevo juego para cada cliente
    _thread.start_new_thread(threaded_client, (conn, game))
