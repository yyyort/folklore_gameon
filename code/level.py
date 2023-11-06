import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from intro import Intro
from item import ItemPlayer
from end import End

class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)
		self.item_player = ItemPlayer(self.animation_player)

		#intro
		self.game_state = 'intro'
		self.intro = Intro()
		self.end = End()

	def create_map(self):
		layouts = {
			'outer_wall': import_csv_layout('../map/new_map_layout/map_bounderies_lower.csv'),
			'inner_wall': import_csv_layout('../map/new_map_layout/map_bounderies_upper.csv'),
			'entities': import_csv_layout('../map/new_map_layout/map_entity_objects.csv')
		}
		graphics = {
			'grass': import_folder('../graphics/grass'),
			'objects': import_folder('../graphics/objects')
		}

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'outer_wall':
							Tile((x,y),[self.obstacle_sprites],'outer_wall')
						if style == 'inner_wall':
							Tile((x,y),[self.visible_sprites, self.obstacle_sprites],'inner_wall')
#						if style == 'grass':
#							random_grass_image = choice(graphics['grass'])
#							Tile(
#								(x,y),
#								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
#								'grass',
#								random_grass_image)
						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

						if style == 'entities':
							if col == '394':
								self.player = Player(
									(x, y),
									[self.visible_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic,
         							self.use_item)
							else:
								if col != '-1':
									if col == '390': monster_name = 'bamboo'
									elif col == '391': monster_name = 'spirit'
									elif col == '392': monster_name ='raccoon'
									else: monster_name = 'squid'
									Enemy(
										monster_name,
										(x,y),
										[self.visible_sprites,self.attackable_sprites],
										self.obstacle_sprites,
										self.damage_player,
										self.trigger_death_particles,
										self.add_exp,
										self.add_score)

	def create_attack(self):
		
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):
		if style == 'heal':
			self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

		if style == 'flame':
			self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

	def use_item(self,style,strength,cost):
		if style == 'molotov':
			self.item_player.molotov(self.player,cost,[self.visible_sprites,self.attack_sprites])

	def destroy_attack(self):
		if self.current_attack:
			self.current_attack.kill()
		self.current_attack = None

	def player_attack_logic(self):
		if self.attack_sprites:
			for attack_sprite in self.attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
				if collision_sprites:
					for target_sprite in collision_sprites:
						if target_sprite.sprite_type == 'grass':
							pos = target_sprite.rect.center
							offset = pygame.math.Vector2(0,75)
							for leaf in range(randint(3,6)):
								self.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
							target_sprite.kill()
						else:
							target_sprite.get_damage(self.player,attack_sprite.sprite_type)

	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

	def trigger_death_particles(self,pos,particle_type):

		self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

	def add_exp(self,amount):

		self.player.exp += amount   

	def add_score(self, amount):

		self.player.score += amount

	def toggle_menu(self):

		self.game_paused = not self.game_paused 

	def reset(self):
		#reset everthing
		# get the display surface 
		self.display_surface = pygame.display.get_surface()
		self.game_paused = False

		# sprite group setup
		self.visible_sprites = YSortCameraGroup()
		self.obstacle_sprites = pygame.sprite.Group()

		# attack sprites
		self.current_attack = None
		self.attack_sprites = pygame.sprite.Group()
		self.attackable_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		self.upgrade = Upgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()
		self.magic_player = MagicPlayer(self.animation_player)

		#intro
		self.intro = Intro()
		self.end = End()

	def run(self):
		if self.game_state == 'intro':
			self.intro.display()
			if self.intro.start_button():
				selected_character = self.intro.character
				selected_alis = self.intro.alias
				self.player.get_character(selected_character, selected_alias)
				if selected_character != '':
					self.game_state = 'game'

		elif self.game_state == 'game':
			self.visible_sprites.custom_draw(self.player)
			self.ui.display(self.player)
			self.visible_sprites.update()
			
			if self.game_paused:
				self.upgrade.display()
			else:
				self.visible_sprites.enemy_update(self.player)
				self.player_attack_logic()
			
			if self.player.health <= 0:
				self.game_state = 'end'
				self.end.add_to_leaderboard(self.player)
		
		""" if self.game_state == 'end':
			self.end.display(self.player)
			if self.end.restart_button():
				self.game_state = 'intro' """
    
		debug(f'Player Stats {self.player.health, self.player.stamina, self.player.speed}')

	def intro_state(self):
		if self.game_state == 'intro':
			self.intro.display()
			if self.intro.start_button():
				selected_character = self.intro.character
				selected_alias = self.intro.alias
				self.player.get_character(selected_character, selected_alias)
				if selected_character != '':
					self.game_state = 'game'
				
	def end_state(self):
		if self.game_state == 'end':
			self.end.display(self.player)
			if self.end.restart_button():
				self.game_state = 'intro'
				print('test')
				self.reset()

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2 
		self.offset = pygame.math.Vector2()

		# creating the floor
		self.floor_surf = pygame.image.load('../graphics/tilemap/map_image/map_3.png').convert()
		self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

	def custom_draw(self,player):

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
			pygame.draw.rect(self.display_surface, (255, 0, 0), rect_border, 2)			
   
			hitbox_border = sprite.hitbox.move(-self.offset.x, -self.offset.y)
			pygame.draw.rect(self.display_surface, (255, 215, 0), hitbox_border, 2)

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
