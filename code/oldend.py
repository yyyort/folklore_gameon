import pygame
from settings import *
import json

class End:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.click_time = None
        self.can_click = True   

        with open('leaderboard.json','r') as f:
            self.leaderboard = json.load(f)
            f.close()
            
        self.leaderboard = sorted(self.leaderboard,key=lambda x:x['exp'],reverse=True)
            #print(self.leaderboard)
  
    def click_cooldown(self):
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= 300:
                self.can_click = True

    def add_to_leaderboard(self,player):
        self.leaderboard.append({'name':player.name,'exp':player.exp})

    def show_leaderboard(self):
      pass

    """ for player in self.leaderboard:
              text_surf = self.font.render(f"{player['name']} {player['exp']}",False,TEXT_COLOR)
              text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 - 100 + self.leaderboard.index(player)*50))
              self.display_surface.blit(text_surf,text_rect) """

    def current_player(self,player):
        text_surf = self.font.render(f"{player.name} {player.exp}",False,TEXT_COLOR)
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2))
        self.display_surface.blit(text_surf,text_rect)
    
    def restart_button(self):
        text_surf = self.font.render('Restart',False,TEXT_COLOR)
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 + 300))
        self.display_surface.blit(text_surf,text_rect)
        if self.can_click and pygame.mouse.get_pressed()[0] and text_rect.collidepoint(pygame.mouse.get_pos()):
            return True


    def display(self, player):
        self.show_leaderboard()
        self.current_player(player)
        self.restart_button()
        self.click_cooldown()