from settings import *
import pygame as pg

def mouse_init(self):
        self.saved_mouse_pos = pg.mouse.get_pos()
        self.was_visible = pg.mouse.get_visible()
        if(not self.was_visible):
            pg.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
        pg.mouse.set_visible(True)
def mouse_close(self):
        pg.mouse.set_visible(self.was_visible)
        pg.mouse.set_pos(self.saved_mouse_pos)