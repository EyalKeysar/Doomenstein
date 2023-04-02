import os
from settings import *
import pygame as pg

def open_map(mapdir, mapname):
    """Open a map file and return a list of lines each line is a list of characters"""
    map_file = open(os.path.join(mapdir, mapname), "r" )
    array = []
    for line in map_file:
        line = line.rstrip('\n')
        line_arr = []
        for some_char in line:
            line_arr.append(some_char)
        array.append( line_arr )
    map_file.close()
    return array

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        """Get the map from the map file"""
        for y, row in enumerate(mini_map):
            for x, value in enumerate(line):
                if(not (value == '0')):
                    self.world_map[(x, y)] = value

    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(self.game.screen, 'brown', (pos[0] * TILESIZE, pos[1] * TILESIZE, TILESIZE, TILESIZE))