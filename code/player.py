import pygame as pg 
from settings import *

# Import Classes
from entity import Entity
from support import import_folder

class Player(Entity):
    def __init__(self, pos, group, create_attack, destroy_attack, obstacle_sprites):
        super().__init__(group)
        self.image = pg.image.load('../graphics/test/player_1.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-4, -24)
        
        self.gender = ''
        self.status = 'down'
        self.character_path = ''
        
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites
        
        # Initialize stats based on gender
        self.stats = player_data['']
        
        # Initialize other stats
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        self.damage = self.stats['damage']
        self.range = self.stats['range']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
        
        self.running = False
        self.running_time = None
            
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
        if not self.attacking:
            
            # Y axis input
            if keys[pg.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pg.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
                
            # X axis input
            if keys[pg.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pg.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.direction.x = 0
            
            if not self.running:
                if keys[pg.K_LSHIFT]:
                    self.running = True
                    if self.running:
                        self.speed *= self.sprint
            else:
                if not keys[pg.K_LSHIFT]:
                    self.running = False
                    self.speed = self.stats['speed']
                
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
                
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')
                
    def get_character(self, selected_gender):
        if selected_gender == 'female':
            self.character_path = '../graphics/player/'
            self.stats = player_data['female']
        else:
            self.character_path = '../graphics/player_alt/'
            self.stats = player_data['male']
            
        self.health = self.stats['health']
        # self.stamina = self.stats['stamina']
        self.damage = self.stats['damage']
        self.range = self.stats['range']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
            
        self.gender = selected_gender
            
    def animate(self):
        animation = self.animations[self.status]

        # loop over the frame index 
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        # set the image
        self.image = animation[int(self.frame_index)]
        self.image = pg.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def cooldowns(self):
        current_time = pg.time.get_ticks()
        
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown: # Insert weapon stats here
                self.attacking = False
                self.destroy_attack()

    def update(self):
        self.import_player_assets()
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)      