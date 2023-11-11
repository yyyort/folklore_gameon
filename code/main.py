import pygame, sys
from settings import *
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('FOLK-LORE')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('../audio/main.ogg')
		main_sound.set_volume(0)
		#main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if self.level.state == 'intro':
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_BACKSPACE:
							self.level.intro.input = self.level.intro.input[:-1]
						else:
							self.level.intro.input += event.unicode
				if self.level.state == 'game':
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_m:
							self.level.toggle_menu()
						if event.key == pygame.K_ESCAPE:
							self.level.toggle_upgrade()
       
			self.screen.fill(WATER_COLOR)
			self.level.run()

			pygame.display.flip()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()
 
print("Press Enter to exit...")
input()