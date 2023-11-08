import pygame as pg 
from settings import *
from support import import_folder

from entity import Entities

class Player(Entities):
    def __init__(self,
                 pos,
                 groups,
                 obstacle,
#                attack,
#                destroy
                ):
        super().__init__(groups)
        self.sprite_type = 'player'
        offset = HITBOX_OFFSET['player_hitbox']
        
        self.image = pg.image.load('../graphics/test/player_.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(offset[0], offset[1])
        
        self.alias = ''
        self.character = ''
        self.condition = ''
        self.folder_path = ''
        
        self.stats = player_data['']
        
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
        self.regen = self.stats['regen']
        
        self.player_info = player_info
        
        self.exp = self.player_info['exp']
        self.level = self.player_info['level']
        self.score = self.player_info['score']
        self.total_score = self.player_info['total_score']
        self.exp_cap = self.player_info['exp_cap']
        
        self.interacting = False
#       self.walking = False
        self.running = False
        
        self.status = 'down'
        
#        self.create_item = attack
#        self.destroy_item = destroy
        self.item_index = 0
        self.weapon = list(weapon_data.keys())
        
        self.obstacle_sprites = obstacle
                
    def import_sprite(self):
        self.animations = {
            'up' : [],
            'down' : [],
            'left' : [],
            'right' : [],
            'up_idle' : [],
            'down_idle' : [],
            'left_idle' : [],
            'right_idle' : [],
            'up_attack' : [],
            'down_attack' : [],
            'left_attack' : [],
            'right_attack' : [],
        }
    
        for animation in self.animations.keys():
            file_path = self.folder_path + animation
            self.animations[animation] = import_folder(file_path)
    
    def input(self,):
        if not self.interacting:
            keys = pg.key.get_pressed()
            
            if keys[pg.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pg.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0
                self.walking = False
                
            if keys[pg.K_a]:
                self.direction.x = -1
                self.status = 'left'
            elif keys[pg.K_d]:
                self.direction.x = 1
                self.status = 'right'
            else:
                self.walking = False
                self.direction.x = 0

            if not self.running and self.stamina > 1:
                if keys[pg.K_LSHIFT]:
                    self.running = True
                    self.speed *= self.sprint
                else:
                    self.running = False
            else:
                if not keys[pg.K_LSHIFT] or self.stamina < 1:
                    self.running = False
                    self.speed = self.stats['speed']

            if self.running:
                self.stamina -= 0.5 * 1

            if keys[pg.K_0]:
                self.health = 0

#            if keys[pg.K_SPACE]:
#                self.interacting = True
#                self.attack_time = pg.time.get_ticks()
#                self.create_item()
                
    def get_character(self, character, alias):
        self.character = character
        self.alias = alias
        
        if character == 'MALE':
            self.stats = player_data['male']
            self.folder_path = '../graphics/player_alt/'
        elif character == 'FEMALE':
            self.stats = player_data['female']
            self.folder_path = '../graphics/player/'
        
        self.health = self.stats['health']
        self.stamina = self.stats['stamina']
        self.speed = self.stats['speed']
        self.sprint = self.stats['sprint']
        self.regen = self.stats['regen']
    
    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
                
        if self.interacting:
            self.direction.x = 0
            self.direction.y = 0
            
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
                    
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')
                
    def animate(self):
        animation = self.animations[self.status]
        
        self.frame_index += self.animation_speed
        if self.frame_index > len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.image = pg.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def score_(self):
        pass

    def level_(self):
        if self.exp >= self.exp_cap:
            self.level += 1
            self.exp_cap *= 1.25
            self.exp = self.player_info['exp']
    
    def stamina_regen(self):
        if not self.running:
            if self.stamina < self.stats['stamina']:
                self.stamina += 0.1 * self.stats['regen']
            else:
                self.stamina = self.stats['stamina']
            
    def cooldowns(self):
        current_time = pg.time.get_ticks()
        pass
    
    def update(self):
        self.input()
        self.import_sprite()
#       self.get_charater()
        self.get_status()
        self.stamina_regen()
        self.level_()
        self.animate()
        self.move(self.speed)
        self.cooldowns()
        
#       self.health -= 0.001 + 1
#       self.exp += 0.5 + 1