import pygame as pg 
from sys import exit
from settings import *

from level import Level

class GAME:
    def __init__(self) -> None:
        
        pg.init()
        
        self.display = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Folk-Lore')
        
        self.clock = pg.time.Clock()
        
        self.font = pg.font.SysFont("Arial" , 18 , bold = True)
        
        self.level = Level()
    
    def fps_counter(self):
        fps = str(int(self.clock.get_fps()))
        fps_t = self.font.render(fps , 1, pg.Color("RED"))
        self.display.blit(fps_t,(100,100))

#    def key_input(self):
#        for event in pg.event.get():
#            if event.type == pg.KEYDOWN:
#                if event.key == pg.K_BACKSPACE:
#                    self.level.menu.character_alias_ = self.level.menu.character_alias_[:-1]
#                else:
#                    self.level.menu.character_alias_ += event.unicode
    
    def alt_f4(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
        
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
            self.alt_f4()
            
            self.level.run()
            if self.level.game_state == 'selection':
                for event in pg.event.get():
                    if event.type == pg.KEYUP:
                        if event.key == pg.K_BACKSPACE:
                            self.level.menu.alias = self.level.menu.alias[:-1]
                        elif event.unicode.isprintable():
                            self.level.menu.alias += event.unicode
                            
            
            self.level.run()
            self.level.debug()
            
            self.fps_counter()
            self.clock.tick(FPS)
            pg.display.flip()
            
game = GAME()
game.run()