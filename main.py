import pygame as pg
import sys
from settings import *
from map import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game() #3:38
        
    def new_game(self):
        self.map = Map(self)
        pass
    
    def update(self):
        pg.display.flip()  # Updates the screen with what we've drawn.
        self.clock.tick(FPS) # Limits the game to 60 FPS.
        pg.display.set_caption("FPS: " + str(self.clock.get_fps()))
    
    def draw(self):
        self.screen.fill('blue')
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    
    def run(self):
        while True:
            self.events()
            self.update()
            self.draw()
            
if __name__ == '__main__':
    g = Game()
    g.run()