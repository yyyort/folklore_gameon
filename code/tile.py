import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type][1]
        x_offset = HITBOX_OFFSET[sprite_type][0]
        
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(x_offset, y_offset)

# class Boundary(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
#         super().__init__(groups)
#         self.sprite_type = sprite_type
#         
#         self.image = surface
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(0, 0)
#         
# class Mini(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
#         super().__init__(groups)
#         self.sprite_type = sprite_type
#         
#         self.image = surface
#         self.rect = self.image.get_rect(topleft=pos)
#         self.hitbox = self.rect.inflate(-48, -48)