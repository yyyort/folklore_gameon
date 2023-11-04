import pygame as pg
from sys import exit 
from settings import *

# Importing Classes
from level import Level

class Game:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Folk-Lore")
        self.clock = pg.time.Clock()
        
        self.level = Level()
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.display.fill((0, 0, 0))
            
            self.level.run()
                    
            self.clock.tick(FPS)
            pg.display.flip()
            
if __name__ == '__main__':
    game = Game()
    game.run()