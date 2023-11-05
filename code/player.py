import pygame as pg
import math
from settings import *

from support import import_folder
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load('../graphics/player_alt/down_idle/down_idle_0.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-16, -16)
        
        self.character_name = ''
        self.character = ''
        self.character_path = ''
                
        self.stats = player_data['']
        
        # Initialize other stats
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        self.damage = self.stats['damage']
        self.range = self.stats['range']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
        
        self.import_player_assets()
        self.status = 'down'
        
        self.obstacle_sprites = obstacle_sprites
        
    def import_player_assets(self):
        
        self.animations = { 
                        'up': [],
                        'down': [],
                        'left': [],
                        'right': [],
                        'up_idle':[],
                        'down_idle':[],
                        'left_idle':[],
                        'right_idle':[],
                        'right_attack':[],
                        'left_attack':[],
                        'down_attack':[],
                        'up_attack':[],
                        }

        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def input(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pg.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0
            
        if keys[pg.K_a]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pg.K_d]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0
            
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status:
                self.status = 'down_idle'
    
    def get_character(self, selected_character, player_name):
        if selected_character == 'male':
            self.character_name = player_name
            self.character = selected_character
            self.character_path = '../graphics/player_alt/'
            self.stats = player_data[selected_character]
        elif selected_character == 'female':
            self.character_name = player_name
            self.character = selected_character
            self.character_path = '../graphics/player/'
            self.stats = player_data[selected_character]
                    
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        self.damage = self.stats['damage']
        self.range = self.stats['range']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
    
    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.image = pg.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(center = self.hitbox.center)
        
    def update(self):
        self.import_player_assets()
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)