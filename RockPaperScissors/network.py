import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555 
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() # Receive the id of the player
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data)) # Send data to the server
            return pickle.loads(self.client.recv(2048*2)) # Receive data from the server and decompose it to get the actual object
        except socket.error as e:
            print(e)


