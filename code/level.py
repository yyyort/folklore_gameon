import pygame as pg
from settings import *
from debug import debug

from support import *
from tile import Tile
from player import Player
from menu import Menu

class Level:
    def __init__(self) -> None:
        self.display_surface = pg.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        
        self.game_pause = False
        
        self.current_attack = None
        self.current_item = None
        
        self.attack_sprite = pg.sprite.Group() # For Entities
        self.attackable_sprite = pg.sprite.Group() # For map objects (ex. Grass)
        
        self.create_map()
        
        self.menu = Menu()
        
        self.game_state = 'menu'
        
    def create_map(self):
        layouts = {
            'outer_border' : import_csv('../map/map_bounderies_lower.csv'),
            'inner_border' : import_csv('../map/map_bounderies_upper.csv'),
            'entities' : import_csv('../map/map_entities.csv')
        }
        
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if col != '-1':
                        if style == 'outer_border':
                            Tile((x, y), [self.obstacle_sprites], 'outer_border')
                        if style == 'inner_border':
                            Tile((x, y), [self.obstacle_sprites], 'inner_border')
                        if style == 'entities':
                            if col == '394':
                                self.player = Player((x, y),
                                                     [self.visible_sprites],
                                                     self.obstacle_sprites)
                            else: pass
    
    def reset(self):
        self.display_surface = pg.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        
        self.game_pause = False
        
        self.current_attack = None
        self.current_item = None
        
        self.attack_sprite = pg.sprite.Group() # For Entities
        self.attackable_sprite = pg.sprite.Group() # For map objects (ex. Grass)
        
        self.create_map()
        self.game_state = 'menu'
        
    def run(self):
        
        if self.game_state == 'menu':
            self.menu.update()
            if self.menu.state == 'selection':
                self.game_state = 'selection'
            elif self.menu.exit_button():
                pg.quit()
                exit()
        
        if self.game_state == 'selection':
            self.menu.update()
            if self.menu.state == 'gameplay':
                self.player.get_character(self.menu.character, self.menu.alias)
                self.game_state = 'gameplay'
        
        if self.game_state == 'gameplay':
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            
#            self.menu.update()
#            if self.menu.state == 'menu':
#                self.game_state = 'menu'
        
    def debug(self):
        debug(f'Health:{self.player.health:.0f}', 10, 10)
        debug(f'Stamina:{self.player.stamina:.0f}', 10, 10*4)
        debug(f'Speed:{self.player.speed:.0f}', 10, 10*7)
        debug(f'Level:{self.player.level:.0f}|EXP:{self.player.exp:.0f}/{self.player.exp_cap:.0f}', 10, 10*10)
        debug(f'Score:{self.player.score:.0f}|Accumulated Score:{self.player.total_score:.0f}', 10, 10*13)
        debug(f'Score:{self.player.alias}', 10, 10*16)
        debug(f'Gamestate:{self.game_state}', 10, 10*19)
        debug(f'Button press:{self.menu.can_click}', 10, 10*22)
        debug(f'Menu State:{self.menu.play_button()},', 10, 10*25)
        debug(f'Menu State:{self.menu.state},', 10, 10*28)
        
class YSortCameraGroup(pg.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        
        self.display_surface = pg.display.get_surface()
        self.width = self.display_surface.get_size()[0] // 2
        self.height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()
        
        
        self.image = pg.image.load('../graphics/tilemap/map_image/map_6.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0, 0))
        
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.width
        self.offset.y = player.rect.centery - self.height
        
        image_offset_pos = self.rect.topleft - self.offset
        self.display_surface.blit(self.image, image_offset_pos)
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
            
            rect = sprite.rect.move(-self.offset.x, -self.offset.y)
            hitbox = sprite.hitbox.move(-self.offset.x, -self.offset.y)
            pg.draw.rect(self.display_surface, (255, 0, 0), rect, 2)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox, 2)