import pygame
from settings import *
from button import Button
from pygame import Color

pygame.init()
print(MONITOR_WIDTH, MONITOR_HEIGHT)
print(WINDOW_WIDTH, WINDOW_HEIGHT)
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

run = True

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.flip()

font = pygame.font.Font(None, int(WINDOW_HEIGHT * 0.15))
text = font.render('Raycast Map Creator', True, Color('white'))
rect = text.get_rect()

def update(event):
    mouse_pos = pygame.mouse.get_pos()
    screen.fill(Color('powderblue'))
    screen.blit(text, ((WINDOW_WIDTH / 2) - rect.bottomright[0] * 1/2, int(WINDOW_HEIGHT * 0.25)))

    button1.draw(screen)
    button1.update(mouse_pos)
    if button1.on and event == pygame.MOUSEBUTTONDOWN:
        button1.button_clicked()

    button2.draw(screen)
    button2.update(mouse_pos)
    if button2.on and event == pygame.MOUSEBUTTONDOWN:
        button2.button_clicked()



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
    
    update(event.type)

    pygame.display.update()

pygame.quit()
