from MenuArc.abstract.Menu import Menu
import pygame as pg
from pygame_widgets import *
from settings import *

class SettingsMenu(Menu):
    def __init__(self, game):
        self.game = game
        self.sensitivity_slider = Slider(
            self.game.screen,
            SENSITIVITY_SLIDER_POS[0],
            SENSITIVITY_SLIDER_POS[1],
            min = MIN_SENSITIVITY,
            max = MAX_SENSITIVITY,
            step = SENSITIVITY_SLIDER_STEP
        )
        self.sensitivity_output = TextBox(
            self.game.screen, 
            SENSITIVITY_TEXT_POS[0], SENSITIVITY_TEXT_POS[1], 
            SENSITIVITY_TEXT_SIZE[0], SENSITIVITY_TEXT_SIZE[1], 
            text = str(self.game.settings.sensitivity)
        )
        
    def update(self):
        self.output.setText(self.sensitivity_slider.getValue())
        self.game.settings.sensitivity = self.sensitivity_slider.getValue()