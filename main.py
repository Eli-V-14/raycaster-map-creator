import pygame
from settings import *
from button import Button
from pygame import Color


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

        pygame.display.flip()
        
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
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
            event = None

            if button1.clicked:
                self.gameStateManager.set_state('level')

            if button2.clicked:
                pygame.quit()
                exit()

            pygame.display.update()

        pygame.quit()

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    
    def run(self, event):
        # left_col = pygame.Rect()
        self.display.fill(Color('powderblue'))
        

class Start:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

        self.font = pygame.font.Font(None, int(WINDOW_HEIGHT * 0.15))
        self.text = self.font.render('Raycast Map Creator', True, Color('white'))
        self.rect = self.text.get_rect()

    def update(self, event):
        mouse_pos = pygame.mouse.get_pos()
        self.display.fill(Color('powderblue'))
        self.display.blit(self.text, ((WINDOW_WIDTH / 2) - self.rect.bottomright[0] * 1/2, int(WINDOW_HEIGHT * 0.25)))

        buttons = [button1, button2]

        for button in buttons:
            button.draw(self.display)
            button.update(mouse_pos)
            if event != None and button.on and event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                button.button_clicked()
                print(button.clicked)
    
    def run(self, event):
        self.update(event)

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState
    
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()