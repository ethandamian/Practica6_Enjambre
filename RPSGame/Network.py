import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.11.250.207"
        self.port = 5555
        self.address = (self.server, self.port)
        self.player = self.connect()
    
    def getPlayer(self):
        return self.player
    
    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass
    
    def send(self,data):
        """
        Send data to the server 
        :param data: str
        """
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except Exception as e:
            print(e)