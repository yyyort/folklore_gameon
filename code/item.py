import pygame
from settings import *

class Item(pygame.sprite.Sprite):
	def __init__(self,player,groups):
		super().__init__(groups)
		self.sprite_type = 'item'
		direction = player.status.split('_')[0]

		# graphic
		full_path = f'../graphics/items/{player.item}/{direction}.png'
		self.image = pygame.image.load(full_path).convert_alpha()
		
		# placement
		if direction == 'right':
			self.rect = self.image.get_rect(midleft = player.rect.midright + pygame.math.Vector2(0,16))
		elif direction == 'left': 
			self.rect = self.image.get_rect(midright = player.rect.midleft + pygame.math.Vector2(0,16))
		elif direction == 'down':
			self.rect = self.image.get_rect(midtop = player.rect.midbottom + pygame.math.Vector2(-10,0))
		else:
			self.rect = self.image.get_rect(midbottom = player.rect.midtop + pygame.math.Vector2(-10,0))


class ItemPlayer:
    def __init__(self, animation_player):

        self.animation_player = animation_player


    def molotov(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

            self.animation_player.create_projectile('molotov', player.rect.center, groups, player.status.split('_')[0])
            #after last frame, create particles


    """ def molotov(self, player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost

        if player.status.split('_')[0] == 'right':
            direction = pygame.math.Vector2(1, 0)
        elif player.status.split('_')[0] == 'left':
            direction = pygame.math.Vector2(-1, 0)
        elif player.status.split('_')[0] == 'up':
            direction = pygame.math.Vector2(0, -1)
        else:
            direction = pygame.math.Vector2(0, 1)

        x, y = player.rect.centerx, player.rect.centery  # Initial position of the projectile

        for i in range(1, 6):
            x += direction.x * 20  # Adjust the multiplier for the desired speed of the projectile
            y += direction.y * 20  # Adjust the multiplier for the desired speed of the projectile
            self.animation_player.create_projectile('molotov', (x, y), groups, player.status.split('_')[0]) """

    def gun(self, player, cost, groups):
        if player.energy >= 50:
            if player.energy >= cost:
                player.energy -= cost

            if player.status.split('_')[0] == 'right':
                direction = pygame.math.Vector2(1,0)

            elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
            elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
            else: direction = pygame.math.Vector2(0,1)

            #move the projectile
            x = player.rect.centerx 
            y = player.rect.centery


            if direction.x:
                x = player.rect.centerx + (TILESIZE * 3) * direction.x
                self.animation_player.create_gun_projectile('gun',(x,y),groups, player.status.split('_')[0])
            else:
                y = player.rect.centery + (TILESIZE * 3) * direction.y
                self.animation_player.create_gun_projectile('gun',(x,y),groups, player.status.split('_')[0])
                
