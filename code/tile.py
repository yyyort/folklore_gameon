import pygame as pg 
from settings import *

class Wall(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.surface = pg.Surface((tile_size, tile_size))
        self.image = self.surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, 0)
        
class Mini(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.surface = pg.Surface((tile_size, tile_size))
        self.image = self.surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-32, -32)