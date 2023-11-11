import pygame
from settings import *

class Dialog:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font('../graphics/font/joystix.ttf', 8)
        self.font_color = (255, 255, 255)
        self.font_background_color = (0, 0, 0)

    def show_dialog(self, text):
        text_surf = self.font.render(text, False, self.font_color)
        text_rect = text_surf.get_rect(center=(self.display_surface.get_size()[0] / 2, self.display_surface.get_size()[1] - 100))
        pygame.draw.rect(self.display_surface, self.font_background_color, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    