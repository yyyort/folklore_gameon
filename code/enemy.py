import pygame
from settings import *
from entity import Entity
from support import *
from dialog import Dialog
from magic import MagicPlayer
from particles import AnimationPlayer

class Enemy(Entity):
	def __init__(self,monster_name,pos,groups,obstacle_sprites,damage_player,magic_player,trigger_death_particles,add_exp,add_score):

		# general setup
		super().__init__(groups)
		self.sprite_type = 'enemy'
		self.skill_damage_timer = None

		# graphics setup
		self.import_graphics(monster_name)
		self.status = 'idle'
		self.image = self.animations[self.status][self.frame_index]
		#resize the image to TILESIZExTILESIZE
		self.image = pygame.transform.scale(self.image, (64,64))
		self.flipped_image = pygame.transform.flip(self.image,True,False)
		
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font('../graphics/font/joystix.ttf', 8)
		self.font_color = (255, 255, 255)
		self.font_background_color = (0, 0, 0)

		# movement
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-10)
		self.obstacle_sprites = obstacle_sprites


		# stats
		self.monster_name = monster_name
		monster_info = monster_data[self.monster_name]
		self.health = monster_info['health']
		self.exp = monster_info['exp']
		self.score = monster_info['score']
		self.speed = monster_info['speed']
		self.attack_damage = monster_info['damage']
		self.resistance = monster_info['resistance']
		self.attack_radius = monster_info['attack_radius']
		self.notice_radius = monster_info['notice_radius']
		self.attack_type = monster_info['attack_type']

		#magic
		self.magic_player = magic_player
		#self.facing_direction = None
		#self.direction = pygame.math.Vector2()
		""" self.animation_player = AnimationPlayer()	
		self.magic_player = MagicPlayer(self.animation_player)
 """
		# player interaction
		self.can_attack = True
		self.attack_time = None
		self.attack_cooldown = monster_info['attack_cooldown']
		self.damage_player = damage_player
		self.trigger_death_particles = trigger_death_particles
		self.add_exp = add_exp
		self.add_score = add_score
		self.facing_direction = None

		
		# dialog
		self.dialog_data = dialog_data[self.monster_name]

		# invincibility timer
		self.vulnerable = True
		self.hit_time = None
		self.invincibility_duration = 500
		self.sound = SOUDN_VOLUME

		# sounds
		self.death_sound = pygame.mixer.Sound('../audio/death.wav')
		self.hit_sound = pygame.mixer.Sound('../audio/hit.wav')
		self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
		self.death_sound.set_volume(self.sound)
		self.hit_sound.set_volume(self.sound)
		self.attack_sound.set_volume(self.sound)

		self.max_health = monster_info['health'] # Store the maximum health
		self.health_bar_width = 50
		self.health_bar_height = 10
		self.health_bar_rect = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
		self.health_bar_color = (0, 255, 0)

	
	#action related
	""" def create_magic(self):
		if self.attack_type == 'magic':
			self.magic_player.flame(self,10,10,self.groups) """
	
	def get_player_distance_direction(self,player):
		enemy_vec = pygame.math.Vector2(self.rect.center)
		player_vec = pygame.math.Vector2(player.rect.center)
		distance = (player_vec - enemy_vec).magnitude()

		if distance > 0:
			direction = (player_vec - enemy_vec).normalize()
		else:
			direction = pygame.math.Vector2()

		return (distance,direction)

	#change for status, attack, move, idle, dialog
	def get_status(self, player):
		distance = self.get_player_distance_direction(player)[0]

		#check facing
		if self.rect.centerx > player.rect.centerx:
			self.facing_direction = 'left'
		else:
			self.facing_direction = 'right' 

		#for melee attack
		if distance <= self.attack_radius and self.can_attack:
			if self.status != 'attack':
				self.frame_index = 0
			self.status = 'attack'
		elif distance <= self.notice_radius:
			self.status = 'move'
		else:
			self.status = 'idle'
		

	def actions(self,player):
		if self.attack_type == 'magic' or self.attack_type == 'flame':
			if self.status == 'attack':
				self.attack_time = pygame.time.get_ticks()			
				direction = self.get_player_distance_direction(player)[1]
				self.magic_player(
					self.attack_damage,
					self.attack_type,
					self.rect.center,
					direction,
					self.can_attack)	
				self.can_attack = False
				self.attack_sound.play()
			elif self.status == 'move':
				distance = self.get_player_distance_direction(player)[0]
				if distance <= 150:
					self.direction = pygame.math.Vector2()
				else:
					self.direction = self.get_player_distance_direction(player)[1]
				""" if distance <= self.attack_radius:
					self.status = 'attack'
				else:
					self.direction = self.get_player_distance_direction(player)[1] """
			else:
				self.direction = pygame.math.Vector2()
		else:
			if self.status == 'attack':
				self.attack_time = pygame.time.get_ticks()
				self.damage_player(self.attack_damage,self.attack_type)
				self.attack_sound.play()
			elif self.status == 'move':
				self.direction = self.get_player_distance_direction(player)[1]
				#get enemy direction movement

			else:
				self.direction = pygame.math.Vector2()

	def cooldowns(self):
		current_time = pygame.time.get_ticks()
		if not self.can_attack:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.can_attack = True

		if not self.vulnerable:
			if current_time - self.hit_time >= self.invincibility_duration:
				self.vulnerable = True

	#to change skill/attack
	def get_damage(self,player,attack_type):
		if self.vulnerable:
			self.hit_sound.play()
			self.direction = self.get_player_distance_direction(player)[1]
			if attack_type == 'weapon':
				self.health -= player.get_full_weapon_damage()
			elif attack_type == 'item':
				self.health -= player.get_full_item_damage()
			else:
				self.health -= player.get_full_item_damage()
			self.hit_time = pygame.time.get_ticks()
			self.vulnerable = False
	
	def skill_damage(self, player, damage, duration):
		if self.vulnerable:
			self.hit_sound.play()
			self.direction = self.get_player_distance_direction(player)[1]
			self.health -= damage
			self.hit_time = pygame.time.get_ticks()
			self.vulnerable = False

	def check_death(self):
		if self.health <= 0:
			self.kill()
			self.trigger_death_particles(self.rect.center,self.monster_name)
			self.add_exp(self.exp)
			self.add_score(self.score)
			self.death_sound.play()

	def hit_reaction(self):
		if not self.vulnerable:
			self.direction *= -self.resistance

	#ui related
	def import_graphics(self,name):
		self.animations = {'idle':[],'move':[],'attack':[]}
		main_path = f'../graphics/monsters/{name}/'
		for animation in self.animations.keys():
			self.animations[animation] = import_folder(main_path + animation)

	def animate(self):
		animation = self.animations[self.status]
		
		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			if self.status == 'attack':
				self.can_attack = False
			self.frame_index = 0
	

		self.image = animation[int(self.frame_index)]
		#RESIZE THE IMAGE TO TILESIZExTILESIZE

		
		if self.facing_direction == 'left':
			self.image = self.flipped_image

		self.image = pygame.transform.scale(self.image, (64,64))
		
		self.rect = self.image.get_rect(center = self.hitbox.center)

		if not self.vulnerable:
			alpha = self.wave_value()
			self.image.set_alpha(alpha)
		else:
			self.image.set_alpha(255)

	#dialog function
	def dialog(self,player):
		distance = self.get_player_distance_direction(player)[0]

		if distance <= self.notice_radius:
			for dialog in self.dialog_data:
				#draw a dialog rectangle in the screen
				Dialog().show_dialog(dialog)

	#health bar
	def draw_health_bar(self):
		if self.health < self.max_health:
			# Create a separate surface for the health bar
			health_bar_surface = pygame.Surface((self.health_bar_width, self.health_bar_height))
			health_bar_surface.set_alpha(255)

			# Calculate health ratio
			ratio = self.health / self.max_health

			# Calculate width of red bar
			current_width = self.health_bar_width * ratio
			current_rect = pygame.Rect(0, 0, current_width, self.health_bar_height)

			# Draw the red bar on the health bar surface
			pygame.draw.rect(health_bar_surface, (255, 0, 0), current_rect)

			# Draw the black border on the health bar surface
			border_rect = pygame.Rect(0, 0, self.health_bar_width, self.health_bar_height)
			border_rect.width += 2
			border_rect.height += 2
			pygame.draw.rect(health_bar_surface, (0, 0, 0), border_rect, 1)

			# Blit the health bar surface onto the enemy's image
			self.image.blit(health_bar_surface, self.health_bar_rect)

	def update(self):
		self.hit_reaction()
		#self.get_facing_direction(self.direction)
		self.move(self.speed)
		self.animate()
		self.cooldowns()
		self.check_death()
		self.draw_health_bar()

	def enemy_update(self,player):
		self.get_status(player)
		self.actions(player)
		self.dialog(player)
		