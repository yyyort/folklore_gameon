import pygame as pg
from sys import exit

from settings import *
from game import Game

class Main:
    def __init__(self):
        pg.init()
        self.display = pg.display.set_mode((d_width, d_height))
        pg.display.set_caption('Folk-Lore')
        self.clock = pg.time.Clock()
        
        self.game = Game()
        
    def run(self):
        while True:
            self.display.fill((125, 125, 125))
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                    
            self.game.run()
                    
            self.clock.tick(fps)
            pg.display.flip()
            
if __name__ == '__main__':
    main = Main()
    main.run()