from pygame import Color
import pygame


class TextField:
    def __init__(self, x, y, width, height, font_size=0, font=None, text="", 
                 fill_color=(255,255,255), border_color = (0,0,0), 
                 invert_colors=False, numeric=False):
        
        self.on = False
        self.clicked = False
        self.upper_limit = 15
        self.lower_limit = 0

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.font = font
        self.text = text
        self.fill_color = fill_color
        self.border_current = fill_color
        self.border_change = border_color
        self.invert_colors = Color('black') if invert_colors else Color('white')
        self.numeric = numeric
        self.text_color = Color('white') if invert_colors else Color('black')

        
    
    def draw(self, screen):
        rect = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.border_current, rect)

        inner_rect = pygame.Rect((self.x + 3, self.y + 3, self.width - 6, self.height - 6))
        pygame.draw.rect(screen, self.fill_color, inner_rect)

        font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=rect.center)
        
        screen.blit(text, text_rect)
    
    def update(self, mouse_pos):
        if self.is_mouse_over(mouse_pos):
            if not self.on:
                cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
                pygame.mouse.set_cursor((8, 16), (0, 0), *cursor)
                self.on = True
        elif self.on:
            pygame.mouse.set_cursor()
            self.on = False
            
    def get_text(self):
        return self.text
    
    def set_text(self, event):
        # print(event.key)
        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        elif event.key == pygame.K_KP_ENTER:
            self.clicked = False
            self.border_current = self.fill_color
        elif self.numeric:
            if pygame.K_0 <= event.key <= pygame.K_9:
                number = self.text + chr(event.key)
                # print(number)
                if self.lower_limit <= int(number) <= self.upper_limit:
                    self.text = number
        else:
            self.text = self.text + chr(event.key)

    def set_upper(self, number):
        self.upper_limit = number

    def get_upper(self):
        return self.upper_limit
    
    def set_lower(self, number):
        self.lower_limit = number
    
    def get_lower(self):
        return self.lower_limit
    
    def is_mouse_over(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        return self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height
    
    def field_clicked(self):
        self.clicked = not self.clicked
        if self.clicked:
            self.border_current = self.border_change
        else:
            self.border_current = self.fill_color
    
    def update_fields(self, display, events):
        mouse_pos = pygame.mouse.get_pos()
        self.draw(display)
        self.update(mouse_pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.is_mouse_over(mouse_pos):
                    self.field_clicked()
                else:
                    self.clicked = False
                    self.border_current = self.fill_color

            if event.type == pygame.KEYDOWN:
                if self.clicked:
                    self.set_text(event)

            

            
    
