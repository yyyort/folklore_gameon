import pygame as pg 
from sys import exit
class Settings:
    WIDTH = 1280
    HEIGHT = 720
    FPS = 60
    
class Game:
    def __init__(self):
        pg.init()
        
        self.display = pg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
        pg.display.set_caption("Test")
        self.clock = pg.time.Clock()
        
        self.sprite_sheet = pg.image.load('../gdsc_game_on/graphics/test/player_sheet.png').convert_alpha()
        self.sheet = self.sprite_sheet        
        
        self.animation_list = []
        self.animation_step = 4
    
    def animation(self):
            for x in range(self.animation_step):
                self.animation_list.append(self.get_image(x, 16, 16, 4, ((0, 0, 0))))       
    
    def get_image(self, frame, width, height, scale, color):
        image = pg.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (0, (frame * height), width, height))
        image = pg.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
        
    def update(self):
        self.animation()
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
            self.display.fill((75, 75, 75,))            
            
            self.update()
            
            for x in range(self.animation_step):
                self.display.blit(self.animation_list[x], (x * 72, 0))
            
            # self.display.blit(self.frame_0, (0, 0))
            # self.display.blit(self.frame_1, (64, 0))
            # self.display.blit(self.frame_2, (64*2, 0))
            # self.display.blit(self.frame_3, (64*3, 0))
            
            self.clock.tick(Settings.FPS)
            pg.display.flip()
            
if __name__ == '__main__':
    game = Game()
    game.run()