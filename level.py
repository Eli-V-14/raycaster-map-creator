from settings import *
from map import Map
from button import Button
from textfield import TextField
from pygame import Color
import pygame

BUTTON_WIDTH = WINDOW_WIDTH * 0.1
BUTTON_HEIGHT = WINDOW_HEIGHT * 0.08

HALF_BUTTON_WIDTH = BUTTON_WIDTH * 1/2
HALF_BUTTON_HEIGHT = BUTTON_HEIGHT * 1/2

text1 = TextField(WINDOW_WIDTH * 1/12 - 100, WINDOW_HEIGHT * 1/5, 200, 75, font_size=40, numeric=True)
text2 = TextField(WINDOW_WIDTH * 1/12 - 100, WINDOW_HEIGHT * 2/5, 200, 75, font_size=40, numeric=True)
button1 = Button(WINDOW_WIDTH * 1/12 - HALF_BUTTON_WIDTH, 
                 WINDOW_HEIGHT * 3/5, 
                 BUTTON_WIDTH, 
                 BUTTON_HEIGHT, 
                 int(WINDOW_HEIGHT * 0.05))

button1.set_border_color(Color('white'))
button1.set_fill_color(Color('navyblue'))
button1.set_text('Enter', Color('white'))

button2 = Button(WINDOW_WIDTH * 1/12 - HALF_BUTTON_WIDTH, 
                 WINDOW_HEIGHT * 4/5, 
                 BUTTON_WIDTH, 
                 BUTTON_HEIGHT, 
                 int(WINDOW_HEIGHT * 0.05))

button2.set_border_color(Color('white'))
button2.set_fill_color(Color('navyblue'))
button2.set_text('Print', Color('white'))

class Level:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.map = Map(self.display)
        self.rows = ''
        self.col = ''
        self.fields = [text1, text2]
        self.buttons = [button1, button2]

        self.font_sizes = [int(WINDOWN_HALF_WIDTH * 0.05), int(WINDOWN_HALF_WIDTH * 0.03), int(WINDOWN_HALF_WIDTH * 0.03)]
        self.texts = ['Settings', 'Number of Rows', 'Number of Columns']
        self.text_y = [WINDOW_HEIGHT * 0.05, WINDOW_HEIGHT * 1/5 * 0.90 , WINDOW_HEIGHT * 2/5 * 0.95]
    
    def run(self, events):
        
        left_col = pygame.Rect(0, 0, WINDOW_WIDTH * 1/6, WINDOW_HEIGHT)

        self.display.fill(Color('powderblue'))
        pygame.draw.rect(self.display, Color('dodgerblue4'), left_col)

        
        for text, y, size in zip(self.texts, self.text_y, self.font_sizes):
            self.display_text(self.display, text, size, left_col, y)

        for field in self.fields:
            field.update_fields(self.display, events)

        for button in self.buttons:
            button.update_buttons(self.display, events)

        if button1.clicked and button1.on:
            self.map = Map(self.display)
            row = text1.get_text()
            col = text2.get_text()
            if (row and col) and (int(row) or int(col) != 0):
                    self.map.set_rows(int(row))
                    self.map.set_columns(int(col))
                    self.map.make_map()
            button1.button_clicked()
        
        if button2.clicked and button2.on:
            self.map.print_map()
            button2.button_clicked()

        self.map.update(events)
    
    def display_text(self, display, text, font_size, shape, y):
        font = pygame.font.Font(None, font_size)
        title = font.render(text, True, Color('white'))
        title_rect = title.get_rect(center=shape.center)
        title_rect.y = y
        display.blit(title, title_rect)
        