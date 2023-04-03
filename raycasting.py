import pygame as pg
import math
from settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game
        
    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            
            #hors
            y_hor, deltay =  (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
            
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            
            delta_depth = deltay / sin_a
            deltax = delta_depth * cos_a
            
            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if(tile_hor in self.game.map.world_map):
                    break
                x_hor += deltax
                y_hor += deltay
                depth_hor += delta_depth
                
            
            # verts
            x_vert, deltax = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            
            delta_depth = deltax / cos_a
            deltay = delta_depth * sin_a
            
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if(tile_vert in self.game.map.world_map):
                    break
                x_vert += deltax
                y_vert += deltay
                depth_vert += delta_depth
            
            # Find closest depth    
            if(depth_vert < depth_hor):
                depth = depth_vert
            else:
                depth = depth_hor
                
            # pg.draw.line(self.game.screen, 'green', (ox * TILESIZE, oy * TILESIZE),
            #             (ox * TILESIZE + depth * cos_a * TILESIZE, oy * TILESIZE + sin_a * TILESIZE * depth), 2)
            
            # Projection
            proj_height = SCREEN_DIST / (depth + 0.0001)
            color = [255 / (1 + depth ** 5 * 0.0001)]*3
            pg.draw.rect(self.game.screen, color, 
                         (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            
            
            ray_angle += DELTA_ANG
            
    def update(self):
        self.ray_cast()