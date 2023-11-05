import pygame as pg 
from settings import *

from support import import_csv_layout
from intro import Intro
from player import Player
from tile import *

class Game:
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        
        self.visible_sprites = YsortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        
        self.create_map()
        
        self.game_state = 'intro'
        self.intro = Intro()
        
    def create_map(self):
        layouts = {
            'boundary_normal' : import_csv_layout('../map/new_map_layout/map_bounderies_lower.csv'),
            'boundary_mini' : import_csv_layout('../map/new_map_layout/map_bounderies_upper.csv'),
            'entity' : import_csv_layout('../map/new_map_layout/map_entity_objects.csv')
        }
        
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tile_size
                        y = row_index * tile_size
                        if style == 'boundary_normal':
                            Wall((x, y), [self.visible_sprites, self.obstacle_sprites]),
                        elif style == 'boundary_mini':
                            Mini((x, y), [self.visible_sprites, self.obstacle_sprites]),
                        elif style == 'entity':
                            if col == '394':
                                self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
    
    def run(self):
        if self.game_state == 'intro':
            self.intro.display()
            if self.intro.start_button():
                player_name = self.intro.name
                selected_character = self.intro.character
                self.player.get_character(selected_character, player_name)
                if selected_character != '':
                    self.game_state = 'game'
        
        elif self.game_state == 'game':
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
    
class YsortCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

        # creating the floor
        self.floor_surf = pg.image.load('../graphics/tilemap/map_image/map_2.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):

        # getting the offset 
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

            rect_border = sprite.rect.move(-self.offset.x, -self.offset.y)
            pg.draw.rect(self.display_surface, (255, 0, 0), rect_border, 2)
            
            hitbox_border = sprite.hitbox.move(-self.offset.x, -self.offset.y)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox_border, 2)
        