import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info):
	display_surface = pygame.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(center = (display_surface.get_size()[0]//2,display_surface.get_size()[1]//2-250))
	pygame.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)