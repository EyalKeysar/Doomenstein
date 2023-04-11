from abstract.Button import Button
import pygame as pg
import sys

class ExitButton(Button):
    def __init__(game, self, text: str, font_size: int, font_color: tuple(int, int, int), pos: tuple(int, int), width: int, height: int, color: tuple(int, int, int), ) -> None:
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.pos = pos
        self.width = width
        self.height = height
        self.color = color
    
    def on_click(self):
        pg.quit()
        sys.exit()
    
    def draw(self):
        pg.draw.rect(game.screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))
        pg.font.init()
        text_font = pg.font.SysFont('Arial', self.font_size)
        text_sur = text_font.render(self.text, True, self.font_color)
        game.screen.blit(text_sur, (self.pos[0] + self.width // 2 - text_sur.get_width() // 2, self.pos[1] + self.height // 2 - text_sur.get_height() // 2))