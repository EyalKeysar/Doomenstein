import pygame as pg

RES = WIDTH, HEIGHT = 1600, 900
FPS = 60
MAPNAME = 'map1.txt'
MAPSDIR = 'maps'
TILESIZE = 100

PLAYER_POS = 1.5, 5  # MiniMap coordinates
PLAYER_ANG = 0
PLAYER_SPD = 0.003
PLAYER_ANG_VEL = 0.002


# Keys
FORWARD_KEY = pg.K_w
BACKWARDS_KEY = pg.K_s
LEFT_KEY = pg.K_a
RIGHT_KEY = pg.K_d

ROT_LEFT_KEY = pg.K_LEFT
ROT_RIGHT_KEY = pg.K_RIGHT