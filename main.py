import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False) # Hide the mouse cursor.
        pg.display.set_icon(pg.image.load(LOGO_NAME)) # Set the icon.
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.flip()  # Updates the screen with what we've drawn.
        self.delta_time = self.clock.tick(FPS)
        # Title.
        pg.display.set_caption("Doomenstein -FPS: " + str(self.clock.get_fps()))
    
    
    def draw(self):
        self.screen.fill('black')    
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()
        
    def events(self):
        # Check for exit keys.
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