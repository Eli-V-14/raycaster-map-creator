from settings import *
from map import Map
from textfield import TextField
from pygame import Color
import pygame

text1 = TextField(WINDOW_WIDTH * 1/12 - 100, WINDOW_HEIGHT * 1/4, 200, 75, font_size=40, numeric=True)
text2 = TextField(WINDOW_WIDTH * 1/12 - 100, WINDOW_HEIGHT * 1/2, 200, 75, font_size=40, numeric=True)

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.map = Map(self.display, 8, 8)
        self.rows = ''
        self.col = ''
        self.fields = [text1, text2]
    
    def run(self, events):
        
        left_col = pygame.Rect(0, 0, WINDOW_WIDTH * 1/6, WINDOW_HEIGHT)

        self.display.fill(Color('powderblue'))
        pygame.draw.rect(self.display, Color('dodgerblue4'), left_col)

        font = pygame.font.Font(None, int(WINDOWN_HALF_WIDTH * 0.05))
        title = font.render('Settings', True, Color('white'))
        title_rect = title.get_rect(center=left_col.center)
        title_rect.y = WINDOW_HEIGHT * 0.05
        
        self.display.blit(title, title_rect)
        for field in self.fields:
            field.update_fields(self.display, events)

        self.map.update(events)
        