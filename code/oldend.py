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
        
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            text_surf = self.font.render('Restart',False,(255, 0, 0))
            
        self.display_surface.blit(text_surf,text_rect)
        
        if self.can_click and pygame.mouse.get_pressed()[0] and text_rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def show_stats(self, exp, score, level):
        score = self.font.render(f'Your score: {score}', False, TEXT_COLOR)
        level = self.font.render(f'Your level: {level}', False, TEXT_COLOR)
        exp = self.font.render(f'Your exp: {exp}', False, TEXT_COLOR)
        
        score_rect = score.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 + 100))
        level_rect = score.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 + 150))
        exp_rect = score.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 + 200))
        
        self.display_surface.blit(score, score_rect)
        self.display_surface.blit(level, level_rect)
        self.display_surface.blit(exp, exp_rect)

    def disclaimer(self):
        text = self.font.render('ONLY CLICK RESTART ONCE', False, (255, 0 , 0))
        text2 = self.font.render('GAME WILL TAKE TIME TO LOAD PLEASE BE PATIENT', False, (255, 0, 0))

        rect = text.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 - 150))
        rect2 = text2.get_rect(center = (self.display_surface.get_size()[0] // 2, self.display_surface.get_size()[1] // 2 - 200))

        self.display_surface.blit(text, rect)
        self.display_surface.blit(text2, rect2)

    def display(self, player):
        self.restart_button()
        self.disclaimer()
        self.show_stats(player.exp, player.score, player.level)
        self.click_cooldown()
