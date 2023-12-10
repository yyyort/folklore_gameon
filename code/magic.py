import pygame
from settings import *
from random import randint

class MagicPlayer:
	def __init__(self,animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'heal': pygame.mixer.Sound('../audio/heal.wav'),
		'flame':pygame.mixer.Sound('../audio/Fire.wav')
		}

	def heal(self,player,strength,cost,groups):
		if player.energy >= cost:
			self.sounds['heal'].play()
			player.health += strength
			player.energy -= cost
			if player.health >= player.stats['health']:
				player.health = player.stats['health']
			self.animation_player.create_particles('aura',player.rect.center,groups)
			self.animation_player.create_particles('heal',player.rect.center,groups)

	def flame(self,player,cost,groups):
		if player.energy >= cost:
			player.energy -= cost
			self.sounds['flame'].play()

			if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
			elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
			elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
			else: direction = pygame.math.Vector2(0,1)

			for i in range(1,6):
				if direction.x: #horizontal
					offset_x = (direction.x * i) * TILESIZE
					x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('flame',(x,y),groups)
				else: # vertical
					offset_y = (direction.y * i) * TILESIZE
					x = player.rect.centerx + randint(-TILESIZE // 3, TILESIZE // 3)
					y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
					self.animation_player.create_particles('flame',(x,y),groups)

	""" def projectile(self, player, cost, groups):
		self.sounds['flame'].play()

		if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
		elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
		elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
		else: direction = pygame.math.Vector2(0,1)

		#move the projectile
		for i in range(1,6):
			if direction.x: #horizontal
				x = player.rect.centerx + i
				y = player.rect.centery + i
				self.animation_player.create_particles('flame',(x,y),groups)
			else: # vertical
				x = player.rect.centerx + 1
				y = player.rect.centery + 1
				self.animation_player.create_particles('flame',(x,y),groups) """

	#changed for skill
	def normal(self, player,cost,groups):
		""" if player.energy >= cost:
			player.energy -= cost """
		self.sounds['flame'].play()

		if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
		elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
		elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
		else: direction = pygame.math.Vector2(0,1)
		#move the projectile
		for i in range(1,6):
			if direction.x: #horizontal
				x = player.rect.centerx + i 
				y = player.rect.centery + i 
				
				self.animation_player.create_projectile('flame',(x,y),groups, player.status.split('_')[0])
			else: # vertical
				x = player.rect.centerx + i 
				y = player.rect.centery + i
				self.animation_player.create_projectile('flame',(x,y),groups, player.status.split('_')[0])
		
				
