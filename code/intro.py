import pygame as pg 
from settings import *

class Intro:
    def __init__(self) -> None:
        self.display_surface = pg.display.get_surface()
        self.font = pg.font.Font(font, font_size[0])
        
        self.name = ''
        self.character = ''
        
        self.can_click = True
        self.click_cooldown = 50
        self.click_time = None
    
    def input(self):
        mouse_click = pg.mouse.get_pressed()
        
        if self.can_click:
            if mouse_click[0]:
                self.click_time = pg.time.get_ticks()
                self.can_click = False
            
    def start_button(self):
        text_surf = self.font.render('Start',False,font_color[0])
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 + 300))
        self.display_surface.blit(text_surf,text_rect)
        if self.can_click and pg.mouse.get_pressed()[0] and text_rect.collidepoint(pg.mouse.get_pos()) and self.input_name != '':
            return True
        
    def male_button(self):
        text_surf = self.font.render('Male',False,font_color[0])
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2 - 50,self.display_surface.get_size()[1]//2 + 200))
        self.display_surface.blit(text_surf,text_rect)
        if text_rect.collidepoint(pg.mouse.get_pos()) or self.character == 'male':
            #change color
            text_surf = self.font.render('Male',False,font_color[1])
            text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2 - 50,self.display_surface.get_size()[1]//2 + 200))
            self.display_surface.blit(text_surf,text_rect)
            if pg.mouse.get_pressed()[0]:
                self.character = 'male'

    def female_button(self):
        text_surf = self.font.render('Female',False,font_color[0])
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2 + 50,self.display_surface.get_size()[1]//2 + 200))
        self.display_surface.blit(text_surf,text_rect)
        if text_rect.collidepoint(pg.mouse.get_pos()) or self.character == 'female':
            text_surf = self.font.render('Female',False,font_color[1])
            text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2 + 50,self.display_surface.get_size()[1]//2 + 200))
            self.display_surface.blit(text_surf,text_rect)
            if pg.mouse.get_pressed()[0]:
                self.character = 'female'

    def input_name(self):
        text_surf = self.font.render('Enter your name:',False,font_color[0])
        text_rect = text_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2))
        self.display_surface.blit(text_surf,text_rect)
        input_surf = self.font.render(self.name,False,font_color[0])
        input_rect = input_surf.get_rect(center = (self.display_surface.get_size()[0]//2,self.display_surface.get_size()[1]//2 + 20))
        self.display_surface.blit(input_surf,input_rect)

    def display_male(self):
        image = pg.image.load('../graphics/test/player.png').convert_alpha()
        image_rect = image.get_rect(center = (self.display_surface.get_size()[0]//2 - 50,self.display_surface.get_size()[1]//2 + 100))
        self.display_surface.blit(image,image_rect)
        
    def display_female(self):
        image = pg.image.load('../graphics/test/player.png').convert_alpha()
        image_rect = image.get_rect(center = (self.display_surface.get_size()[0]//2 + 50,self.display_surface.get_size()[1]//2 + 100))
        self.display_surface.blit(image,image_rect)

    def display_male_info(self):
        health = self.font.render('Health: 100',False,font_color[0])
        health_rect = health.get_rect(center = (self.display_surface.get_size()[0]//2 - 200,self.display_surface.get_size()[1]//2 + 100))
        self.display_surface.blit(health,health_rect)
        energy = self.font.render('Energy: 60',False,font_color[0])
        energy_rect = energy.get_rect(center = (self.display_surface.get_size()[0]//2 - 200,self.display_surface.get_size()[1]//2 + 120))
        self.display_surface.blit(energy,energy_rect)
        attack = self.font.render('Attack: 10',False,font_color[0])
        attack_rect = attack.get_rect(center = (self.display_surface.get_size()[0]//2 - 200,self.display_surface.get_size()[1]//2 + 140))
        self.display_surface.blit(attack,attack_rect)
        magic = self.font.render('Magic: 4',False,font_color[0])
        magic_rect = magic.get_rect(center = (self.display_surface.get_size()[0]//2 - 200,self.display_surface.get_size()[1]//2 + 160))
        self.display_surface.blit(magic,magic_rect)
        speed = self.font.render('Speed: 5',False,font_color[0])
        speed_rect = speed.get_rect(center = (self.display_surface.get_size()[0]//2 - 200,self.display_surface.get_size()[1]//2 + 180))
        self.display_surface.blit(speed,speed_rect)

    def display_female_info(self):
        health = self.font.render('Health: 80',False,font_color[0])
        health_rect = health.get_rect(center = (self.display_surface.get_size()[0]//2 + 200,self.display_surface.get_size()[1]//2 + 100))
        self.display_surface.blit(health,health_rect)
        energy = self.font.render('Energy: 80',False,font_color[0])
        energy_rect = energy.get_rect(center = (self.display_surface.get_size()[0]//2 + 200,self.display_surface.get_size()[1]//2 + 120))
        self.display_surface.blit(energy,energy_rect)
        attack = self.font.render('Attack: 8',False,font_color[0])
        attack_rect = attack.get_rect(center = (self.display_surface.get_size()[0]//2 + 200,self.display_surface.get_size()[1]//2 + 140))
        self.display_surface.blit(attack,attack_rect)
        magic = self.font.render('Magic: 6',False,font_color[0])
        magic_rect = magic.get_rect(center = (self.display_surface.get_size()[0]//2 + 200,self.display_surface.get_size()[1]//2 + 160))
        self.display_surface.blit(magic,magic_rect)
        speed = self.font.render('Speed: 6',False,font_color[0])
        speed_rect = speed.get_rect(center = (self.display_surface.get_size()[0]//2 + 200,self.display_surface.get_size()[1]//2 + 180))
        self.display_surface.blit(speed,speed_rect)
    
    def cooldown(self):
        current_time = pg.time.get_ticks()
        
        if not self.can_click:
            if current_time - self.click_time >= self.click_cooldown:
                self.can_click = True
            
    def display(self):
        self.input()
        self.input_name()
        self.display_male()
        self.display_female()
        self.display_male_info()
        self.display_female_info()
        self.male_button()
        self.female_button()
        self.cooldown()