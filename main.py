import pygame
from settings import *
from button import Button
from pygame import Color

from menus import Start
from level import Level
from gameStateManager import GameStateManager

BUTTON_WIDTH = WINDOW_WIDTH * 0.13
BUTTON_HEIGHT = WINDOW_HEIGHT * 0.1

HALF_BUTTON_WIDTH = BUTTON_WIDTH * 1/2
HALF_BUTTON_HEIGHT = BUTTON_HEIGHT * 1/2

# 1st way of defining the button and its features
button1 = Button(WINDOWN_HALF_WIDTH - HALF_BUTTON_WIDTH, 
                 WINDOW_HALF_HEIGHT + HALF_BUTTON_HEIGHT, 
                 BUTTON_WIDTH, 
                 BUTTON_HEIGHT, 
                 int(WINDOW_HEIGHT * 0.05))

button1.set_border_color(Color('white'))
button1.set_fill_color(Color('dodgerblue4'))
button1.set_text('Play', Color('white'))

# 2nd way of defining the button and its features
button2 = Button(WINDOWN_HALF_WIDTH - HALF_BUTTON_WIDTH, 
                 WINDOW_HALF_HEIGHT + BUTTON_HEIGHT * 1.75, 
                 BUTTON_WIDTH, BUTTON_HEIGHT, 
                 int(WINDOW_HEIGHT * 0.05), 
                 text='Exit',
                 text_color=Color('white'), 
                 fill_color=Color('dodgerblue4'), 
                 border_color=Color('white'))


class Game:
    def __init__(self):
        pygame.init()    
        self.running = True
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        buttons = [button1, button2]

        pygame.display.flip()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager, buttons)
        self.level = Level(self.screen, self.gameStateManager)

        self.states = {'start':self.start,
                       'level':self.level}
        
    
    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or (event.key == pygame.K_ESCAPE if event.type == pygame.KEYDOWN else False):
                    pygame.quit()
                    exit()
            
            self.states[self.gameStateManager.get_state()].run(event)
            

            if button1.clicked:
                self.gameStateManager.set_state('level')

            if button2.clicked:
                pygame.quit()
                exit()

            event = None
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()