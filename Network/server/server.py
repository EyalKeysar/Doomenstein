import socket
import threading
from player_client import PlayerClient

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        
    def start(self):
        self.server.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            conn, addr = self.server.accept()
            print(f"Client connected from {addr}")
            self.clients.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()
    
    def handle_client(self):
        
