import pygame as pg 
from settings import *

class Menu:
    def __init__(self):
        
        self.font = pg.font.Font(FONT, FONT_SIZE[6])
        
        self.display_surface = pg.display.get_surface()
        
        self.can_click = True
        self.click_cooldown = 175
        self.click_time = None
        
        self.can_type = True
        self.input_cooldown = 500
        self.input_time = None
        
        self.clock = pg.time.Clock()
        
        self.character = ''
        self.alias = ''
        self.game_state = 'menu'
        self.leaderboard_list = []
        
    def input(self):
        self.mouse_click = pg.mouse.get_pressed()
        self.mouse_pos = pg.mouse.get_pos()
        
        if self.can_click:
            if self.mouse_click[0]:
                self.click_time = pg.time.get_ticks()
                self.can_click = False
                    
    def key_input(self):
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.alias = self.alias[:-1]
                elif event.unicode.isprintable():
                    self.alias += event.unicode
                    
    def cooldown(self):
        current_time = pg.time.get_ticks()
        
        if not self.can_click:
            if current_time - self.click_time >= self.click_cooldown:
                self.can_click = True

        if not self.can_type:
            if current_time - self.can_type >= self.input_cooldown:
                self.can_type = True
        
        if self.play_button():
            return None
        
        if self.restart_button():
            return None
    
    def background(self):
        surf = pg.Surface((WIDTH, HEIGHT))
        surf.fill((0, 0, 215))
        rect = surf.get_rect(topleft = (0, 0))
        
        self.display_surface.blit(surf, rect)
    
    def play_button(self):
        surf = self.font.render("PLAY", False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 100))
        hitbox = rect.inflate(10, 10)
        
        if hitbox.collidepoint(self.mouse_pos):
            surf = self.font.render("PLAY", False, FONT_COLOR[0])
        
        self.display_surface.blit(surf, rect)
        pg.draw.rect(self.display_surface, (255, 255, 255), hitbox, 3)
        
        if not self.can_click and self.mouse_click[0] and hitbox.collidepoint(self.mouse_pos):
            return True
        
    def exit_button(self):
        surf = self.font.render("EXIT", False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        hitbox = rect.inflate(10, 10)
        
        if hitbox.collidepoint(self.mouse_pos):
            surf = self.font.render("EXIT", False, FONT_COLOR[0])
        
        self.display_surface.blit(surf, rect)
        pg.draw.rect(self.display_surface, (255, 255, 255), hitbox, 3)
        
        if not self.can_click and self.mouse_click[0] and hitbox.collidepoint(self.mouse_pos):
            pg.quit()
            exit()
        
    def restart_button(self):
        surf = self.font.render("RESTART", False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 - 100))
        hitbox = rect.inflate(10, 10)
        
        if hitbox.collidepoint(self.mouse_pos):
            surf = self.font.render("RESTART", False, FONT_COLOR[0])
        
        self.display_surface.blit(surf, rect)
        pg.draw.rect(self.display_surface, (255, 255, 255), hitbox, 3)
        
        surf_input = self.font.render(self.alias, False, FONT_COLOR[4])
        rect_input = surf_input.get_rect(center = (WIDTH // 2, HEIGHT // 2 +350))
        
        self.display_surface.blit(surf, rect)
        self.display_surface.blit(surf_input, rect_input)
        
        if not self.can_click and self.mouse_click[0] and hitbox.collidepoint(self.mouse_pos):
            return True
    
    def leaderboard(self):
        
        leaderboard_surf = []
        
        sorted_leaderboard = sorted(self.leaderboard_list, key = lambda x: x[1], reverse = True)
        
        player_list  = 5
        for player, (alias, score) in enumerate(sorted_leaderboard[:player_list]):
            text = f'{player + 1}: {alias}: {score}'
            surf = self.font(text, False, FONT_COLOR[4])
            leaderboard_surf.append(surf)
            
        return leaderboard_surf
        
    def character_selection(self):
        surf = {
            'MALE' : self.font.render('MALE', False, FONT_COLOR[4]),
            'FEMALE' : self.font.render('FEMALE', False, FONT_COLOR[4])
        }
        rect = {
            'MALE' : surf['MALE'].get_rect(center = (WIDTH // 2 - 200, HEIGHT // 2)),
            'FEMALE' : surf['FEMALE'].get_rect(center = (WIDTH // 2 + 200, HEIGHT // 2)),
        }
        
        for character, character_rect in rect.items():
            hitbox = character_rect.inflate(10, 10)
            
            if hitbox.collidepoint(self.mouse_pos):
                surf[character] = self.font.render(character, False, FONT_COLOR[0])
                
            self.display_surface.blit(surf[character], character_rect)
            pg.draw.rect(self.display_surface, (255, 255, 255), hitbox, 3)
            
            if not self.can_click and self.mouse_click[0] and hitbox.collidepoint(self.mouse_pos):
                self.character = character
                print(self.character)
                return True
            
    def character_alias(self):
        
        surf = self.font.render('ENTER NAME:', False, FONT_COLOR[4])
        rect = surf.get_rect(center = (WIDTH // 2, HEIGHT // 2 + 200))
        
        surf_input = self.font.render(self.alias, False, FONT_COLOR[4])
        rect_input = surf_input.get_rect(center = (WIDTH // 2, HEIGHT // 2 +350))
        
        self.display_surface.blit(surf, rect)
        self.display_surface.blit(surf_input, rect_input)
    
        self.key_input()
    
    def display_menu(self):
        self.input()
        self.cooldown()
        self.background()
        self.play_button()
        self.exit_button()
        
    def display_character_selection(self):
        self.input()
        self.cooldown()
        self.background()
        self.character_alias()
        self.character_selection()
        
    def display_game_over(self):
        self.input()
        self.cooldown()
        self.background()
        self.restart_button()
        
        leaderboard_surface = self.leaderboard()
        
        x, y, gap = WIDTH // 2, HEIGHT // 2, 150
        for surf in leaderboard_surface:
            self.display_surface(surf, (x, y))
            y += gap