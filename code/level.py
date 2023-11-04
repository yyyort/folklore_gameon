import pygame as pg
from settings import *

# Importing Classes
from tile import Boundary
from player import Player
from intro import Intro

class Level():
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        
        self.state = 'intro'
        self.intro = Intro()
        
        self.create_map()
        
    def create_map(self):
            for row_index, row in enumerate(WORLD_MAP):
                for col_index, col in enumerate(row):
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    if col == 'x':
                        Boundary((x, y), [self.visible_sprites, self.obstacle_sprites])
                    elif col == 'y':
                        self.player = Player((x, y), [self.visible_sprites])
                   
    def run(self):
        
        if self.state == 'intro':
            self.intro.display()
            if self.intro.start_button():
                self.player.gender = self.intro.select
                self.state = 'game'
                
        elif self.state == 'game':
            self.visible_sprites.custom_draw(self.player)
        
    
        self.visible_sprites.update()

class YSortCameraGroup(pg.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pg.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pg.math.Vector2()

		# creating the floor
		# self.floor_surf = pg.image.load('../graphics/tilemap/_map_partial_detailed_1.png').convert()
		# self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

		# getting the offset 
		self.offset.x = player.rect.centerx - self.half_width
		self.offset.y = player.rect.centery - self.half_height

		# drawing the floor
		# floor_offset_pos = self.floor_rect.topleft - self.offset
		# self.display_surface.blit(self.floor_surf,floor_offset_pos)

		# for sprite in self.sprites():
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset
			self.display_surface.blit(sprite.image,offset_pos)
   
			rect_border = sprite.rect.move(-self.offset.x, -self.offset.y)
			pg.draw.rect(self.display_surface, (255, 0, 0), rect_border, 2)
			
			hitbox_border = sprite.hitbox.move(-self.offset.x, -self.offset.y)
			pg.draw.rect(self.display_surface, (255, 215, 0), hitbox_border, 2)