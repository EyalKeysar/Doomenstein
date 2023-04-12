import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from MenuArc.SettingsMenu import *
from sprite_object import *

class Game:
    def __init__(self):
        pg.init()
        self.mouse_sensitivity = MOUSE_SENSITIVITY
        pg.mouse.set_visible(False) # Hide the mouse cursor.
        pg.display.set_icon(pg.image.load(LOGO_NAME)) # Set the icon.
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.was_in_menu = False
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        
        pg.display.flip()  # Updates the screen with what we've drawn.
        self.delta_time = self.clock.tick(FPS)
        # Title.
        pg.display.set_caption("Doomenstein -FPS: " + str(self.clock.get_fps()))
    
    
    def draw(self):
        self.screen.fill('grey')
        
        self.object_renderer.draw()
        pg.draw.circle(self.screen, AIM_BAR_COLOR, (HALF_WIDTH, HALF_HEIGHT), 5, 5)
        
        # Draw helth bar.
        pg.draw.rect(self.screen, HEALTH_BAR_COLOR, (HEALTH_BAR_DIST, HEALTH_BAR_HEIGHT, self.player.health * (WIDTH - HEALTH_BAR_DIST*2)/PLAYER_HEALTH, HEALTH_BAR_WIDTH))
        # Draw health text.
        pg.font.init()
        text_font = pg.font.SysFont('Arial', 30)
        text_sur = text_font.render(str(self.player.health), True, HEALTH_TEXT_COLOR)
        self.screen.blit(text_sur, ((self.player.health * (WIDTH - HEALTH_BAR_DIST*2)/PLAYER_HEALTH)/2 - text_sur.get_width()/2, HEALTH_BAR_HEIGHT))
        

        # self.map.draw()
        # self.player.draw()
        
    def events(self):
        # Check for exit keys.wwww
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if(event.type == pg.KEYDOWN):
                if(event.key == pg.K_ESCAPE):
                    pg.quit()
                    sys.exit()
            if(event.type == pg.MOUSEMOTION):
                if(pg.mouse.get_pos()[0] < HALF_WIDTH/2 or pg.mouse.get_pos()[0] > HALF_WIDTH + HALF_WIDTH/2 or pg.mouse.get_pos()[1] < HALF_HEIGHT/2 or pg.mouse.get_pos()[1] > HALF_HEIGHT + HALF_HEIGHT/2):
                    pg.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
                
                    
    
    def run(self):
        i = 0
        while True:
            self.events()
            self.update()
            self.draw()
            
            
if __name__ == '__main__':
    g = Game()
    g.run()