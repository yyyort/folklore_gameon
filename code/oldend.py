import pygame
from settings import *

class End:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.click_time = None
        self.can_click = True   
  
    def click_cooldown(self):
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= 300:
                self.can_click = True
    
    def restart_button(self):
        text_surf = self.font.render('Restart',False,TEXT_COLOR)
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 + 300))
        self.display_surface.blit(text_surf,text_rect)
        if self.can_click and pygame.mouse.get_pressed()[0] and text_rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def disclaimer(self):
        text = self.font.render('ONLY CLICK RESTART ONCE', False, TEXT_COLOR)
        text2 = self.font.render('GAME WILL TAKE TIME TO LOAD PLEASE BE PATIENT', False, TEXT_COLOR)

        rect = text.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 + 100))
        rect2 = text2.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2))

        self.display_surface.blit(text, rect)
        self.display_surface.blit(text2, rect2)

    def display(self):
        self.restart_button()
        self.disclaimer()
        self.click_cooldown()
