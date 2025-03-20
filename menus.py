from settings import *
from pygame import Color
from button import Button
import pygame

class Start:
    def __init__(self, display, gameStateManager, buttons):
        self.display = display
        self.gameStateManager = gameStateManager
        self.buttons = buttons

        self.font = pygame.font.Font(None, int(WINDOW_HEIGHT * 0.15))
        self.text = self.font.render('Raycast Map Creator', True, Color('white'))
        self.rect = self.text.get_rect()

    def update(self, event):
        self.display.fill(Color('powderblue'))
        self.display.blit(self.text, ((WINDOW_WIDTH / 2) - self.rect.bottomright[0] * 1/2, int(WINDOW_HEIGHT * 0.25)))
        Button.update_buttons(self.display, event, self.buttons)
        
    def run(self, event):
        self.update(event)