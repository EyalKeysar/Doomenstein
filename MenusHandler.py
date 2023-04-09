import pygame as pg
from settings import *

class MenusHandler():
    def __init__(self, screen) -> None:
        self.saved_mouse_pos = (0, 0)
        self.was_visible = False
        self.screen = screen
    
    def mouse_init(self):
        self.saved_mouse_pos = pg.mouse.get_pos()
        self.was_visible = pg.mouse.get_visible()
        if(not self.was_visible):
            pg.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        pg.mouse.set_visible(True)
    def mouse_close(self):
        pg.mouse.set_visible(self.was_visible)
        pg.mouse.set_pos(self.saved_mouse_pos)

    def open_menu(self):
        self.mouse_init()
        
        buttons = {
            0: 'Start',
            1: 'Exit Game'
        }
        current = 0
        
        self.screen.fill('black')
        pg.font.init()
        text_font = pg.font.SysFont('Arial', 30)
        text_sur = text_font.render('Press ESC to exit', True, 'white')
        self.screen.blit(text_sur, (HALF_WIDTH - text_sur.get_width() // 2, HALF_HEIGHT - text_sur.get_height() // 2))
        pg.display.flip()
        
        run = True
        while run:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_a:
                        run = False
                        pg.mouse.set_visible(False)
                        pg.mouse.set_pos(self.saved_mouse_pos)
                    if event.key == FORWARD_KEY:
                        current += 1
        self.mouse_close()