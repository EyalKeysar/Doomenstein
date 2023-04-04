import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        
    def draw(self):
        self.render_game_objects()
        
    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)
        
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        return pg.transform.scale(pg.image.load(path).convert_alpha(), res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture(TEXTURES_DIR + '1.png'),
            2: self.get_texture(TEXTURES_DIR + '2.png'),
        }