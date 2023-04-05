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
        speed_factored_sin = speed * player_angle_sin
        speed_factored_cos = speed * player_angle_cos
        
        # Movement
        keys = pg.key.get_pressed()
        if(keys[FORWARD_KEY]):
            deltax += speed_factored_cos
            deltay += speed_factored_sin
        if(keys[BACKWARDS_KEY]):
            deltax -= speed_factored_cos
            deltay -= speed_factored_sin
        if(keys[LEFT_KEY]):
            deltax += speed_factored_sin
            deltay -= speed_factored_cos
        if(keys[RIGHT_KEY]):
            deltax -= speed_factored_sin
            deltay += speed_factored_cos

        # Check walls and move player accordingly.
        self.check_walls_collision(deltax, deltay)
        
        # Rotation        
        if(keys[ROT_LEFT_KEY]):
            self.angle -= PLAYER_ANG_VEL * self.game.delta_time
        if(keys[ROT_RIGHT_KEY]):
            self.angle += PLAYER_ANG_VEL * self.game.delta_time

        self.angle %= 2 * math.pi

    def check_walls(self, x, y):
        """
            Check if the coordinates are a wall.
            Returns True is its -NOT- a wall.
        """
        return (x, y) not in self.game.map.world_map
    
    def check_walls_collision(self, deltax, deltay):
        """
            Move player deltay in y axis and deltax in x axis and according to the walls in the map.
        """
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if(self.check_walls(int(self.x + deltax * scale), int(self.y))): # If the next position x axis is not a wall, move in the x axis.
            self.x += deltax
        if(self.check_walls(int(self.x), int(self.y + deltay * scale))): # If the next position y axis is not a wall, move in the y axis.
            self.y += deltay  
                  
    def draw(self):
        # pg.draw.line(self.game.screen, 'green', (self.x * TILESIZE, self.y * TILESIZE), 
        #             (self.x * TILESIZE + math.cos(self.angle) * WIDTH, 
        #             self.y * TILESIZE + math.sin(self.angle) * WIDTH), 2)
        pg.draw.circle(self.game.screen, 'blue', (int(self.x * TILESIZE), int(self.y * TILESIZE)), 15)

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if(my < MOUSE_BORDER_DOWN or my > MOUSE_BORDER_UP):
            pg.mouse.set_pos([mx, HALF_HEIGHT])
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
        
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    
