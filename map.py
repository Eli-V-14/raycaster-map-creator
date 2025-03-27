from settings import *
from button import Button
from pygame import Color
import pygame
import numpy as np


class Map:
    def __init__(self, display, rows, cols):
        self.display = display
        self.rows = rows
        self.cols = cols
    
        # Button Inital Padding
        self.x_pad = WINDOW_WIDTH * 5 / 6 * 1 / 16
        self.y_pad = WINDOW_HEIGHT * 1 / 16
        self.settings_pad = WINDOW_WIDTH * 1 / 6

        # Calculated Measures for Padding and Display
        self.display_width = WINDOW_WIDTH * 35 / 48
        self.display_height = WINDOW_HEIGHT * 7 / 8

        # Button Dimensions
        self.button_x = self.display_width / self.cols * 0.9
        self.button_y = self.display_height / self.rows * 0.9

        # Button Padding
        self.button_x_pad = (self.display_width - self.button_x) / (self.cols - 1)
        self.button_y_pad =  (self.display_height - self.button_y) / (self.rows - 1)

        self.buttons = []

        self.map = self.make_map()

    def make_map(self):
        map = np.full((self.rows, self.cols), None)
        current_y = self.y_pad
        for row in range(self.rows):
            current_x = self.x_pad + self.settings_pad
            for col in range(self.cols):
                button = Button(current_x, current_y, self.button_x, self.button_y, border_color=Color('white'), fill_color=Color('black'), switch=True)
                self.buttons.append(button)
                map[row][col] = button.clicked
                current_x += self.button_x_pad
            current_y += self.button_y_pad
        return map

    
    def update(self, events):
        for button in self.buttons:
            Button.update_buttons(self.display, events, button)

    def get_map(self):
        return self.map
                
