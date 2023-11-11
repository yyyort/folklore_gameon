import pygame 
#utilities
from settings import *
from tile import Tile
from debug import debug
from support import *
from random import choice, randint
from ui import UI
from particles import AnimationPlayer
import json

#player
from player import Player
from weapon import Weapon
from magic import MagicPlayer
from item import ItemPlayer
from item import Item
#from old_upgrade import Upgrade
from new_upgrade import NewUpgrade


#enemy
from enemy import Enemy


#game states
from intro import Intro
from oldend import End

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
		self.enemy_attack_sprites = pygame.sprite.Group()	
		self.player_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		#self.upgrade = Upgrade(self.player)
		self.new_upgrade = NewUpgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()

		self.magic_player = MagicPlayer(self.animation_player)
		self.item_player = ItemPlayer(self.animation_player)

		#enemy
		self.enemy = []

		#phases
		self.state = 'menu'
		self.intro = Intro()
		self.end = End()

	def create_map(self):
		layouts = {
			'boundary': import_csv_layout('../folklore/layout/_boundary.csv'),
#			'inner_wall': import_csv_layout('../map/map_bounderies_upper.csv'),
			'entities': import_csv_layout('../folklore/layout/_entity.csv')
		}
		graphics = {
			'grass': import_folder('../graphics/grass'),
			'objects': import_folder('../graphics/objects')
		}

		#changed
		""" layouts = {
			'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
			'grass': import_csv_layout('../map/map_Grass.csv'),
			'object': import_csv_layout('../map/map_Objects.csv'),
			'entities': import_csv_layout('../map/map_Entities.csv')
		}
		graphics = {
			'grass': import_folder('../graphics/grass'),
			'objects': import_folder('../graphics/objects')
		} """

		for style,layout in layouts.items():
			for row_index,row in enumerate(layout):
				for col_index, col in enumerate(row):
					if col != '-1':
						x = col_index * TILESIZE
						y = row_index * TILESIZE
						if style == 'boundary':
							Tile((x,y),[self.obstacle_sprites],'invisible')
						if style == 'grass':
							random_grass_image = choice(graphics['grass'])
							Tile(
								(x,y),
								[self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
								'grass',
								random_grass_image)

						if style == 'object':
							surf = graphics['objects'][int(col)]
							Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)

						if style == 'entities':
							if col == '15':
								self.player = Player(
									(x,y),
									[self.visible_sprites, self.player_sprites],
									self.obstacle_sprites,
									self.create_attack,
									self.destroy_attack,
									self.create_magic,
									self.use_item,
									self.create_item,
									)
							else:
								if col == '38': monster_name = 'Dwende'
								elif col == '14': monster_name = 'Engkanto'
								elif col == '12': monster_name ='Tiyanak'
								else: monster_name = 'Kapre'
								""" if col == '390': monster_name = 'bamboo'
								elif col == '391': monster_name = 'spirit'
								elif col == '392': monster_name ='raccoon'
								else: monster_name = 'squid' """
								Enemy(
									monster_name,
									(x,y),
									[self.visible_sprites,self.attackable_sprites],
									self.obstacle_sprites,
									self.damage_player,
									self.enemy_magic_player,
									self.trigger_death_particles,
									self.add_exp,
         							self.add_score)
								
	
	#write a function where if player is in the range of the enemy, dialogue will appear
	def create_dialog(self):
		pass

	#player function
	def create_attack(self):
		self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

	def create_item(self):
		self.current_attack = Item(self.player,[self.visible_sprites,self.attack_sprites])

	def create_magic(self,style,strength,cost):
		if style == 'heal':
			self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])

		if style == 'flame':
			self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

		#changed for skill 
		if style == 'normal':
			self.magic_player.normal(self.player,cost,[self.visible_sprites,self.attack_sprites])

	def use_item(self,style,strength,cost):
		if style == 'molotov':
			self.item_player.molotov(self.player,cost,[self.visible_sprites,self.attack_sprites]) 
		if style == 'gun':
			self.item_player.gun(self.player,cost,[self.visible_sprites,self.attack_sprites])

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
						
							

							#change item effect
							if attack_sprite.sprite_type == 'gun':
								attack_sprite.kill()

							if attack_sprite.sprite_type == 'molotov':
								attack_sprite.kill()
								posx = target_sprite.rect.centerx
								posy = target_sprite.rect.centery
									
								for _ in range(10):	
									
									#target_sprite.skill_damage(self.player,20, 2000)
									
									# Calculate a random position around the projectile's center
									offset_x = randint(-50, 50)  # Adjust the offset values as needed
									offset_y = randint(-50, 50)  # Adjust the offset values as needed
									spawn_position = (posx + offset_x, posy + offset_y)
									
									self.item_player.animation_player.create_particles('molotov',spawn_position,[self.visible_sprites, self.attack_sprites])
									#self.item_player.molotov(self.player,20,[self.visible_sprites,self.attack_sprites])

	#enemy function
	def damage_effect(self,attack_type):
		if attack_type == 'leaf_attack':
			self.player.debuff('slow',3,10000) #slow for 10 seconds


	def damage_player(self,amount,attack_type):
		if self.player.vulnerable:
			#changed for skill enemey attack effect
			self.damage_effect(attack_type)
			self.player.health -= amount
			self.player.vulnerable = False
			self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

	def enemy_magic_player(self,amount,attack_type, pos, direction, can_attack):
		if can_attack and self.player.vulnerable:
			#self.damage_effect(attack_type)
			#self.player.vulnerable = False
			#self.player.hurt_time = pygame.time.get_ticks()
			self.animation_player.create_monster_flame(pos,
											   		direction,
												 	attack_type,
												   	[self.visible_sprites, self.enemy_attack_sprites],
													amount)
			#q: how can i fix so that create_monster_flame will be called once only?
			#a: create a new function for enemy magic player


	def enemy_attack_logic(self):
		if self.enemy_attack_sprites:
			for enemy_attack in self.enemy_attack_sprites:
				collision_sprites = pygame.sprite.spritecollide(enemy_attack,self.player_sprites,False)
				if collision_sprites:
					if self.player.vulnerable:
						self.damage_effect(enemy_attack.sprite_type)
						print(enemy_attack.sprite_type)
						self.player.vulnerable = False
						self.player.health -= enemy_attack.damage
						self.player.hurt_time = pygame.time.get_ticks()
						
						enemy_attack.kill()

	def trigger_death_particles(self,pos,particle_type):
		#change for death animation
		pass
		#self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

	def add_exp(self,amount):
		self.player.exp += amount
  
	def add_score(self, amount):
		self.player.score += amount

	#interaction function
	def dialog_logic(self):
		pass

	#ui function
	def toggle_menu(self):

		self.game_paused = not self.game_paused

	def toggle_upgrade(self):
		
		self.game_paused = not self.game_paused 

	#game state function
	def reset(self):

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
		self.enemy_attack_sprites = pygame.sprite.Group()	
		self.player_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

		# user interface 
		self.ui = UI()
		#self.upgrade = Upgrade(self.player)
		self.new_upgrade = NewUpgrade(self.player)

		# particles
		self.animation_player = AnimationPlayer()

		self.magic_player = MagicPlayer(self.animation_player)
		self.item_player = ItemPlayer(self.animation_player)

		#enemy
		self.enemy = []

		#phases
		self.state = 'menu'
		self.intro = Intro()
		self.end = End()

	def run(self):
     
		if self.state == 'menu':
			self.intro.display()
			if self.intro.start_button():
				self.player.get_character(self.intro.select)
				self.state = 'game'
     
		elif self.state == 'game_over':
			self.end.display()
			if self.end.restart_button():
				self.reset()
     
		elif self.state == 'game':
			self.visible_sprites.custom_draw(self.player)
			self.ui.display(self.player)
			#print(self.player.debuffs)
			
			if self.game_paused:
				
				#self.upgrade.display()
				self.new_upgrade.display()
			else:
				self.visible_sprites.update()
				self.visible_sprites.enemy_update(self.player)
				self.player_attack_logic()
				self.enemy_attack_logic()

		if self.player.health <= 0:
			self.state = 'game_over'

#		debug(self.player.health, 400, 400)

	def intro_state(self):
		if self.state == 'intro':
			self.intro.display()
			if self.intro.start_button():
				self.player.name = self.intro.input
				self.player.gender = self.intro.select
				self.state = 'game'
				
	def end_state(self):
		if self.state == 'end':
			self.end.display(self.player)
			""" if self.end.restart_button():
				self.state = 'intro'
				#print('test')
				self.reset() """

class YSortCameraGroup(pygame.sprite.Group):
	def __init__(self):

		# general setup 
		super().__init__()
		self.display_surface = pygame.display.get_surface()
		self.half_width = self.display_surface.get_size()[0] // 2
		self.half_height = self.display_surface.get_size()[1] // 2
		self.offset = pygame.math.Vector2()

		# creating the floor
		#self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
		#changed
		self.floor_surf = pygame.image.load('../folklore/map.png').convert()
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

	def enemy_update(self,player):
		enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
		for enemy in enemy_sprites:
			enemy.enemy_update(player)
