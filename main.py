from Game import *
from Network.server.server import Server
import threading
import time

if __name__ == '__main__':
    server = Server('localhost', 5000)
    game = Game()
    
    
    server_thread = threading.Thread(target=server.start)
    game_thread = threading.Thread(target=game.run)
    
    game_thread.start()
    
    
    # try:
    #     game_thread.start()
        
    #     game_thread.join()
    # except Exception as e:
    #     print("error: " + e)