from settings import *
from map import Map
from pygame import Color
import pygame

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.map = Map(self.display, 8, 8)
        self.map.make_map()
        self.rows = ''
        self.col = ''
    
    def run(self, event):
        
        left_col = pygame.Rect(0, 0, WINDOW_WIDTH * 1/6, WINDOW_HEIGHT)

        self.display.fill(Color('powderblue'))
        pygame.draw.rect(self.display, Color('dodgerblue4'), left_col)

        font = pygame.font.Font(None, int(WINDOWN_HALF_WIDTH * 0.05))
        title = font.render('Settings', True, Color('white'))
        title_rect = title.get_rect(center=left_col.center)
        title_rect.y = WINDOW_HEIGHT * 0.05
        
        self.display.blit(title, title_rect)

        self.map.update(event)
        