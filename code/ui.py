import pygame
from settings import * 

class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)
		

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)

		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			magic = pygame.image.load(magic['graphic']).convert_alpha()
			self.magic_graphics.append(magic)

		# convert item dictionary
		self.item_graphics = []
		for item in item_data.values():
			item = pygame.image.load(item['graphic']).convert_alpha()
			self.item_graphics.append(item)
	
	def show_exp(self,level,exp,exp_cap):
		text_surf = self.font.render(f'Level:{level}:EXP:{exp}/{exp_cap:.2f}',False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 20
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,(255, 255, 255),text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
  
	def show_score(self,score):
		text_surf = self.font.render(f'Score:{score}',False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 20
		y = self.display_surface.get_size()[1] - 70
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,(255, 255, 255),text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
	
	def show_hitpoints(self, hitpoint, max_hitpoint):
			text_surf = self.font.render(f'Hitpoint:{hitpoint}/{max_hitpoint}',False,TEXT_COLOR)
			x = 20
			y = 20
			text_rect = text_surf.get_rect(topleft = (x,y))
	
			pygame.draw.rect(self.display_surface,(255, 255, 255),text_rect.inflate(20, 20))
			self.display_surface.blit(text_surf, text_rect)
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR, text_rect.inflate(20,20),3)
  
	def show_energy(self, energy, max_energy):
		text_surf = self.font.render(f'energy:{energy:.0f}/{max_energy}',False,TEXT_COLOR)
		x = 20
		y = 70
		text_rect = text_surf.get_rect(topleft = (x,y))
  
		pygame.draw.rect(self.display_surface,(255, 255, 255),text_rect.inflate(20, 20))
		self.display_surface.blit(text_surf, text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR, text_rect.inflate(20,20),3)


	#changed, switch ui
	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(20,HEIGTH - 100,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def magic_overlay(self,magic_index,has_switched):
		bg_rect = self.selection_box(110,HEIGTH - 100,has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf,magic_rect)
	
	#changed
	def item_overlay(self,item_index,has_switched):
		bg_rect = self.selection_box(200,HEIGTH - 100,has_switched)
		item_surf = self.item_graphics[item_index]
		item_rect = item_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(item_surf,item_rect)

	def display(self, player):
		#player health and energy
		self.show_hitpoints(player.health, player.stats['health'])
		self.show_energy(player.energy, player.stats['energy'])

		self.show_exp(player.level, player.exp, player.exp_cap)
		self.show_score(player.score)

		self.weapon_overlay(player.weapon_index,not player.can_switch_weapon)
		self.magic_overlay(player.magic_index,not player.can_switch_magic)
		self.item_overlay(player.item_index,not player.can_switch_item)

		#enemy health bar
		#self.show_bar(enemy.health,enemy.health,self.enemy_health_bar_rect,HEALTH_COLOR)
		