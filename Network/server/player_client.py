

class PlayerClient:
    def __init__(self, pos, client_socket):
        self.pos = pos
        self.client_socket = client_socket
    
    def send(self, data):
        self.client_socket.send(data.encode())