from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANG
    
    def movement(self):
        player_angle_sin = math.sin(self.angle)
        player_angle_cos = math.cos(self.angle)
        deltax, deltay = 0, 0
        speed = PLAYER_SPD * self.game.delta_time
        speed_sin = speed * player_angle_sin
        speed_cos = speed * player_angle_cos
        
        # Movement
        keys = pg.key.get_pressed()
        if(keys[FORWARD_KEY]):
            deltax += speed_cos
            deltay += speed_sin
        if(keys[BACKWARDS_KEY]):
            deltax -= speed_cos
            deltay -= speed_sin
        if(keys[LEFT_KEY]):
            deltax -= speed_sin
            deltay += speed_cos
        if(keys[RIGHT_KEY]):
            deltax += speed_sin
            deltay -= speed_cos

        self.check_walls_collision(deltax, deltay)
        
        # Rotation        
        if(keys[ROT_LEFT_KEY]):
            self.angle -= PLAYER_ANG_VEL * self.game.delta_time
        if(keys[ROT_RIGHT_KEY]):
            self.angle += PLAYER_ANG_VEL * self.game.delta_time

        self.angle %= 2 * math.pi

    def check_walls(self, x, y):
        return (x, y) not in self.game.map.world_map
    def check_walls_collision(self, deltax, deltay):
        if(self.check_walls(int(self.x + deltax), int(self.y))):
            self.x += deltax
        if(self.check_walls(int(self.x), int(self.y + deltay))):
            self.y += deltay  
            
                  
    def draw(self):
        pg.draw.line(self.game.screen, 'green', (self.x * TILESIZE, self.y * TILESIZE), 
                    (self.x * TILESIZE + math.cos(self.angle) * WIDTH, 
                    self.y * TILESIZE + math.sin(self.angle) * WIDTH), 2)
        pg.draw.circle(self.game.screen, 'blue', (int(self.x * TILESIZE), int(self.y * TILESIZE)), 15)

    def update(self):
        self.movement()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    
