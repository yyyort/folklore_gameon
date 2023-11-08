import pygame
from settings import *
import json

""" 
json format:
{
    "players": {
        "player1": {
            "exp": 10,
            "time": 0
        },
        "player2": {
            "exp": 0,
            "time": 1
        }
    }
}
 """

class End:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)
        self.leaderboard = {}

        with open('leaderboard.json','r') as f:
            self.leaderboard = json.load(f)
            f.close()

        self.players = self.leaderboard['players']
        self.sorted_players = sorted(self.players.items(), key=lambda item: item[1]['exp'], reverse=True)

    def show_leaderboard(self):
        for player in self.sorted_players:
            text_surf = self.font.render(f"{player[0]} {player[1]['exp']}",False,TEXT_COLOR)
            text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 - 100 + self.sorted_players.index(player)*50))
            self.display_surface.blit(text_surf,text_rect)

    
        

    
    def display(self, player):
        self.show_leaderboard()