from settings import *
from button import Button
from pygame import Color
import pygame
import numpy as np


class Map:
    def __init__(self, display, rows=10, cols=10):
        self.display = display
        self.rows = rows
        self.cols = cols

        self.buttons = []
        self.map = None
        
    def make_map(self):
        # Button Inital Padding
        x_pad = WINDOW_WIDTH * 5 / 6 * 1 / 16
        y_pad = WINDOW_HEIGHT * 1 / 16
        settings_pad = WINDOW_WIDTH * 1 / 6

        # Calculated Measures for Padding and Display
        display_width = WINDOW_WIDTH * 35 / 48
        display_height = WINDOW_HEIGHT * 7 / 8

        # Button Dimensions
        button_x = display_width / self.cols * 0.9
        button_y = display_height / self.rows * 0.9

        # Button Padding
        button_x_pad = (display_width - button_x) / (self.cols - 1 if self.cols != 1 else 1)
        button_y_pad =  (display_height - button_y) / (self.rows - 1 if self.rows != 1 else 1)

        self.map = np.full((self.rows, self.cols), None)
        current_y = y_pad
        for row in range(self.rows):
            current_x = x_pad + settings_pad
            for col in range(self.cols):
                button = Button(current_x, current_y, button_x, button_y, border_color=Color('white'), fill_color=Color('black'), switch=True)
                self.buttons.append(button)
                self.map[row][col] = button
                current_x += button_x_pad
            current_y += button_y_pad
        

    def update(self, events):
        for button in self.buttons:
            button.update_buttons(self.display, events)

    def print_map(self):
        updated_map = np.full((self.rows, self.cols), None)

        for row in range(self.rows):
            for col in range(self.cols):
                updated_map[row][col] = 1 if self.map[row][col].clicked else 0
                
        print(updated_map)
    
    def set_rows(self, rows):
        self.rows = rows
    
    def set_columns(self, cols):
        self.cols = cols
                
