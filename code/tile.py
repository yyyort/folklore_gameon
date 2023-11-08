import pygame as pg 
from settings import *

class Tile(pg.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface = pg.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        
        offset_x = HITBOX_OFFSET[sprite_type][1]
        offset_y = HITBOX_OFFSET[sprite_type][0]
        
        self.image = surface
#       if sprite_type == 'object':
#           self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - TILZESIZE))
#       else:
#           self.rect = self.image.get_rect(topleft = pos)
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(offset_x, offset_y)