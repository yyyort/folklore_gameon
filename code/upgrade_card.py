import pygame
from settings import *

class Upgrade_card:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.leaderboard = []
        self.click_time = None
        self.can_click = True

    def show_stat(self):
        image = pygame.image.load('images/upgrade_card.png')
        