import pygame
from settings import *
from button import Button
from pygame import Color

pygame.init()

# 1st way of defining the button and its features
button1 = Button(100, 100, 250, 100, 60)

button1.set_border_color(Color('white'))
button1.set_fill_color(Color('darkgoldenrod1'))
button1.set_text('Click Me', Color('white'))

# 2nd way of defining the button and its features
button2 = Button(600, 100, 250, 100, 60, text='You Can\'t',
                text_color=Color('white'), 
                fill_color=Color('darkgoldenrod1'), 
                border_color=Color('white')
                )


run = True

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.flip()

def update(events):
    screen.fill((128, 128, 128))
    button1.draw(screen)
    button2.draw(screen)

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    
    update(events)

    pygame.display.update()

pygame.quit()
