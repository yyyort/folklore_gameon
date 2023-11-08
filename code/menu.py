import pygame as pg
from settings import *

class Menu():
    def __init__(self) -> None:
        self.display_surface = pg.display.get_surface()
        self.big_font = pg.font.Font(FONT, FONT_SIZE[7])
        self.mid_font = pg.font.Font(FONT, FONT_SIZE[5])
        self.font = pg.font.Font(FONT, FONT_SIZE[3])
        
        self.character = ''
        self.alias = ''
        self.leaderboard = []
    
        self.state = 'menu'
    
        self.can_click = True
        self.click_time = None
        self.click_cooldown = 150
        
    def handle_event(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_press = pg.mouse.get_pressed()        
        self.key = pg.key.get_pressed()
        
        if self.key[pg.K_ESCAPE]:
            self.state = 'menu'
        
        if self.mouse_press[0]:
            self.click_time = pg.time.get_ticks()
            self.can_click = False
    
    def cooldown(self):
        current_time = pg.time.get_ticks()
    
        if not self.can_click:
            if current_time - self.click_time >= self.click_cooldown:
                self.can_click = True
                
    def background(self, x, y):
        surf = pg.Surface((WIDTH, HEIGHT))
        rect = surf.get_rect(topleft = (x, y))
        
        self.display_surface.blit(surf, rect)
    
    def back_button(self, back):
        text = 'BACK'
        surf = self.font.render(text, False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH - 100, 50))
        hitbox = rect.inflate(10, 10)
        
        if hitbox.collidepoint(self.mouse_pos):
            surf = self.font.render(text, False, FONT_COLOR[0])
        
        self.display_surface.blit(surf, rect)
        pg.draw.rect(self.display_surface, (225, 215, 0), hitbox, 2)
        
        if hitbox.collidepoint(self.mouse_pos) and self.mouse_press[0] and not self.can_click:
            self.state = back
            return self.state
    
    def play_button(self):
        text = 'PLAY'
        surf = self.big_font.render(text, False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 50))
        hitbox = rect.inflate(10, 10)
        
        if self.state == 'menu':
            if hitbox.collidepoint(self.mouse_pos):
                surf = self.big_font.render(text, False, FONT_COLOR[0])
            
            self.display_surface.blit(surf, rect)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox, 2)
        
            if hitbox.collidepoint(self.mouse_pos) and self.mouse_press[0] and not self.can_click:
                self.state = 'selection'
                return self.state
        
    def exit_button(self):
        text = 'EXIT'
        surf = self.big_font.render(text, False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 50))
        hitbox = rect.inflate(10, 10)
        
        if self.state == 'menu':
            if hitbox.collidepoint(self.mouse_pos):
                surf = self.big_font.render(text, False, FONT_COLOR[0])
                
            self.display_surface.blit(surf, rect)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox, 2)
            
            if hitbox.collidepoint(self.mouse_pos) and self.mouse_press[0] and not self.can_click:
                pg.quit()
                exit()
    
    def male_button(self):
        text = '> male <'
        surf = self.font.render(text, False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2 - 300, HEIGHT // 2 + 300))
        hitbox = rect.inflate(10, 10)
        
        if self.state == 'selection':
            
            if hitbox.collidepoint(self.mouse_pos):
                surf = self.font.render(text, False, FONT_COLOR[0])
                
            self.display_surface.blit(surf, rect)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox, 3)
            
            if hitbox.collidepoint(self.mouse_pos) and self.mouse_press[0] and not self.can_click:
                self.state = 'gameplay'
                self.character = 'MALE'
    
    def female_button(self):
        text = '> female <'
        surf = self.font.render(text, False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2 + 300, HEIGHT // 2 + 300))
        hitbox = rect.inflate(10, 10)
        
        if self.state == 'selection':
            
            if hitbox.collidepoint(self.mouse_pos):
                surf = self.font.render(text, False, FONT_COLOR[0])
                
            self.display_surface.blit(surf, rect)
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox, 3)
            
            if hitbox.collidepoint(self.mouse_pos) and self.mouse_press[0] and not self.can_click:
                self.state = 'gameplay'
                self.character = 'FEMALE'
    
    def character_image(self):
        image = {
            'MALE' : pg.transform.scale(pg.image.load('../graphics/test/player_.png').convert_alpha(), (192, 192)),
            'FEMALE' : pg.transform.scale(pg.image.load('../graphics/test/player.png').convert_alpha(), (192, 192)),
        }
        
        rect = {
            'MALE' : image['MALE'].get_rect(midbottom = (WIDTH // 2 - 300, HEIGHT // 2 + 75)),
            'FEMALE' : image['FEMALE'].get_rect(midbottom = (WIDTH // 2 + 300, HEIGHT // 2 + 75)),
        }
    
        for image_surf, image_rect in rect.items():
            self.display_surface.blit(image[image_surf], image_rect)
    
    def character_stats(self):
        male = player_data['male']
        female = player_data['female']
        
#        health = male['health']
#        stamina = male['stamina']
#        speed = male['speed']
#        
#        health = female['health']
#        stamina = female['stamina']
#        speed = female['speed']
        
        surf = {
            '00' : self.font.render(f'Health: {male["health"]}', False, FONT_COLOR[4]),
            '01' : self.font.render(f'Stamina: {male["stamina"]}', False, FONT_COLOR[4]),
            '02' : self.font.render(f'Speed: {male["speed"]}', False, FONT_COLOR[4]),
            
            '10' : self.font.render(f'Health: {female["health"]}', False, FONT_COLOR[4]),
            '11' : self.font.render(f'Stamina: {female["stamina"]}', False, FONT_COLOR[4]),
            '12' : self.font.render(f'Speed: {female["speed"]}', False, FONT_COLOR[4]),
        }
    
        rect = {
            '00' : surf['00'].get_rect(midleft = (WIDTH // 2 - 375, HEIGHT // 2 +   75 + 90)),
            '01' :  surf['01'].get_rect(midleft = (WIDTH // 2 - 375, HEIGHT // 2 + 75 + 120 + 10)),
            '02' :  surf['02'].get_rect(midleft = (WIDTH // 2 - 375, HEIGHT // 2 +   75 + 150 + 10 + 10)),
            
            '10' : surf['10'].get_rect(midleft = (WIDTH // 2 + 200, HEIGHT // 2 +   75 + 90)),
            '11' :  surf['11'].get_rect(midleft = (WIDTH // 2 + 200, HEIGHT // 2 + 75 + 120 + 10)),
            '12' :  surf['12'].get_rect(midleft = (WIDTH // 2 + 200, HEIGHT // 2 +   75 + 150 + 10 + 10)),
        }
        
        hitbox = {key: rect[key].inflate(10, 10) for key in rect}

        for key, hitbox_rect in hitbox.items():
            self.display_surface.blit(surf[key], rect[key])
            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox_rect, 2)
    
#        hitbox = {
#            '00' : rect['00'].inflate(10, 10),
#            '01' : rect['01'].inflate(10, 10),
#            '02' : rect['02'].inflate(10, 10),
#            
#            '10' : rect['10'].inflate(10, 10),
#            '11' : rect['11'].inflate(10, 10),
#            '12' : rect['12'].inflate(10, 10),
#        }
#    
#        for text_surf, text_rect in rect.items():
#            self.display_surface.blit(surf[text_surf], text_rect)
#            
#        for hitbox_rect in hitbox.items():
#            pg.draw.rect(self.display_surface, (255, 215, 0), hitbox_rect, 2)
    
    def update(self):
        self.handle_event()
        self.cooldown()
        if self.state == 'menu' or self.state == 'selection':
            self.background(0, 0)
        
        if self.state == 'menu':
            self.back_button('selection')
            self.play_button()
            self.exit_button()
            
        if self.state == 'selection':
            self.back_button('menu')
            self.character_image()
            self.character_stats()
            self.male_button()
            self.female_button()
            
#        if self.state == 'gameplay':
#            self.back_button('menu')