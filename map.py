import os
from settings import *
import pygame as pg
from map_patterns import *

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = MAP_ONE
        self.world_map = {}
        self.get_map()

    def get_map(self):
        """Get the map from the map file"""
        for y, row in enumerate(self.mini_map):
            for x, value in enumerate(row):
                if(value):
                    self.world_map[(x, y)] = value

    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(self.game.screen, 'brown', (pos[0] * TILESIZE, pos[1] * TILESIZE, TILESIZE, TILESIZE), 2)