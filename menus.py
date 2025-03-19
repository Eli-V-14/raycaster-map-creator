from settings import *
from pygame import Color
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
        mouse_pos = pygame.mouse.get_pos()

        self.display.fill(Color('powderblue'))
        self.display.blit(self.text, ((WINDOW_WIDTH / 2) - self.rect.bottomright[0] * 1/2, int(WINDOW_HEIGHT * 0.25)))

        for button in self.buttons:
            button.draw(self.display)
            button.update(mouse_pos)
            if event != None and button.on and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button.button_clicked()
                print(button.clicked)
    
    def run(self, event):
        self.update(event)