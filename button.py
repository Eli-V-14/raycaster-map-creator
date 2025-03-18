import pygame

class Button():
    def __init__(self, x, y, width, height, font_size=0, font=None, text='', text_color=(0,0,0),
                 border_color=(0,0,0), fill_color=(255,255,255), scale=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        
        self.text = text
        self.text_color = text_color
        self.font = font
        self.font_size = font_size
        self.border_color = border_color
        self.fill_color = fill_color
        self.scale = scale

    def draw(self, screen):
        # Create the outer rectangle
        outer_rect = pygame.Rect((self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.border_color, outer_rect)
        
        # Create the inner rectangle
        inner_rect = pygame.Rect((self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        pygame.draw.rect(screen, self.fill_color, inner_rect)
        
        # Render the text
        font = pygame.font.Font(self.font, self.font_size)
        text = font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=outer_rect.center)
        
        # Draw the text on the screen
        screen.blit(text, text_rect)

    def set_fill_color(self, fill_color):
        self.fill_color = fill_color

    def set_border_color(self, border_color):
        self.border_color = border_color
    
    def set_font(self, font, font_size=None):
        self.font = font
        self.font_size = font_size

    def set_text(self, text, text_color=(0,0,0)):
        self.text = text
        self.text_color = text_color