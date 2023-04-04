import pygame as pg
import math
from settings import *


class RayCasting:
    
    # This is a classic raycasting algorithm.
    
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.object_to_render = []
        self.textures = self.game.object_renderer.wall_textures
        
    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values
            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else:
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                wall_column = pg.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)
                
            
            self.objects_to_render.append((depth, wall_column, wall_pos))
        
    def ray_cast(self):
        self.ray_casting_result = []
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
                    texture_hor = self.game.map.world_map[tile_hor]
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
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += deltax
                y_vert += deltay
                depth_vert += delta_depth
            
            # Find closest depth    
            if(depth_vert < depth_hor):
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if(cos_a > 0) else (1 - y_vert)
            else:
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if(sin_a > 0) else (x_hor)
                
            # pg.draw.line(self.game.screen, 'green', (ox * TILESIZE, oy * TILESIZE),
            #             (ox * TILESIZE + depth * cos_a * TILESIZE, oy * TILESIZE + sin_a * TILESIZE * depth), 2)
            
            
            # Fisheye effect fix
            depth *= math.cos(self.game.player.angle - ray_angle)
            
            # Projection
            proj_height = SCREEN_DIST / (depth + 0.0001)
            
            # raycasting result
            
            self.ray_casting_result.append((depth, proj_height, texture, offset))
            

            ray_angle += DELTA_ANG
            
    def update(self):
        self.ray_cast()
        self.get_objects_to_render()