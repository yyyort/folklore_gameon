import pygame
from settings import *

class ItemPlayer:
    def __init__(self, animation_player):

        self.animation_player = animation_player

    def molotov(self, player, cost, groups):
        if player.stamina >= cost:
            player.stamina -= cost

        if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
        elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
        elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
        else: direction = pygame.math.Vector2(0,1)
        #move the projectile
        x = player.rect.centerx + 1
        y = player.rect.centery + 1

        for i in range(1,6):
            if direction.x: #horizontal
                x = player.rect.centerx + i
                y = player.rect.centery + i
                self.animation_player.create_projectile('molotov',(x,y),groups, player.status.split('_')[0])
            else: # vertical
                x = player.rect.centerx + i
                y = player.rect.centery + i
                self.animation_player.create_projectile('molotov',(x,y),groups, player.status.split('_')[0])