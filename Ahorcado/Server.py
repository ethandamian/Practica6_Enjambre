import socket
import _thread
import pickle
from game import HangmanGame

# Servidor que maneja los clientes
def threaded_client(conn, game):
    conn.send(pickle.dumps(game.__dict__))  # Enviar el estado inicial del juego

    while True:
        try:
            data = conn.recv(2048).decode()
            if not data:
                break
            else:
                if data != "get":
                    game.guess(data)
                conn.sendall(pickle.dumps(game.__dict__))  # Enviar el estado actualizado
        except:
            break

    conn.close()

# Configuración del servidor
server = "192.168.1.91"
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
