import pygame
from settings import *

class NewUpgrade:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        
        self.cards = []

        # card setup
        self.card_pos = [(CARD_WIDTH + CARD_SPACING) * i +
                         CARD_SPACING for i in range(4)]
        self.card_pos_y = [CARD_SPACING for i in range(4)]
        self.card_text = [
            'health',
            'defense',
            'attack',
            'speed']
        self.card_value = [
            self.player.health,
            self.player.defense,
            self.player.attack,
            self.player.speed]

    def create_cards(self):
        for i in range(len(self.card_pos)):
            self.cards.append(Card((self.card_pos[i], self.card_pos_y[i]),
                              self.card_text[i], self.card_value[i], self.player, self.display_surface))

    def display(self):
        self.create_cards()
        for card in self.cards:
            card.update()
        


class Card:
    def __init__(self, pos, text, value, player, display_surface):
        self.pos = pos
        self.text = text
        self.value = value
        self.player = player
        self.display_surface = display_surface
        self.hover = False
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # stats
        if text == 'health':
            self.icon = pygame.image.load(
                '../graphics/ui/health.png').convert_alpha()
        elif text == 'defense':
            self.icon = pygame.image.load(
                '../graphics/ui/defense.png').convert_alpha()
        elif text == 'attack':
            self.icon = pygame.image.load(
                '../graphics/ui/attack.png').convert_alpha()
        elif text == 'speed':
            self.icon = pygame.image.load(
                '../graphics/ui/speed.png').convert_alpha()
        elif text == 'knife':
            self.icon = pygame.image.load(
                '../graphics/ui/knife.png').convert_alpha()
        elif text == 'bolo':
            self.icon = pygame.image.load(
                '../graphics/ui/bolo.png').convert_alpha()
        elif text == 'molotov':
            self.icon = pygame.image.load(
                '../graphics/ui/molotov.png').convert_alpha()

        # plus and minus buttons
        self.plus_button = pygame.image.load('../graphics/ui/plus.png').convert_alpha()
        self.minus_button = pygame.image.load('../graphics/ui/minus.png').convert_alpha()
        #resize buttons 32x32
        self.plus_button = pygame.transform.scale(self.plus_button, (32, 32))
        self.minus_button = pygame.transform.scale(self.minus_button, (32, 32))

        self.add_btn = Button((self.pos[0] + CARD_WIDTH/2 - self.plus_button.get_width()/2 + 50,
             self.pos[1] + CARD_HEIGHT/2 - self.plus_button.get_height()/2 + 100), self.plus_button, self.display_surface)
        self.minus_btn = Button((self.pos[0] + CARD_WIDTH/2 - self.minus_button.get_width()/2 - 50,
             self.pos[1] + CARD_HEIGHT/2 - self.minus_button.get_height()/2 + 100), self.minus_button, self.display_surface)
     


    def draw(self):
        # draw card
        pygame.draw.rect(self.display_surface,
                         CARD_BG_COLOR,
                         (self.pos[0], self.pos[1], CARD_WIDTH, CARD_HEIGHT))
        pygame.draw.rect(self.display_surface,
                         CARD_BORDER_COLOR,
                         (self.pos[0], self.pos[1], CARD_WIDTH, CARD_HEIGHT), CARD_BORDER)

        # draw icon center of card
        self.display_surface.blit(self.icon,
                                  (self.pos[0] + CARD_WIDTH/2 - self.icon.get_width()/2,
                                   self.pos[1] + CARD_HEIGHT/2 - self.icon.get_height()/2))

        # draw text above of icon padding 30
        text = self.font.render(self.text, False, TEXT_COLOR)
        self.display_surface.blit(text,
                                  (self.pos[0] + CARD_WIDTH/2 - text.get_width()/2,
                                   self.pos[1] + CARD_HEIGHT/2 - text.get_height()/2 - 100))

        # draw plus and minus buttons below of icon
        self.minus()
        self.add()

        #draw value between plus and minus buttons
        value = self.font.render(str(self.value), False, TEXT_COLOR)
        self.display_surface.blit(value,
                                    (self.pos[0] + CARD_WIDTH/2 - value.get_width()/2,
                                     self.pos[1] + CARD_HEIGHT/2 - value.get_height()/2 + 50))

    def check_hover(self):
        # check if mouse is hovering over card
        mouse_pos = pygame.mouse.get_pos()
        """ if mouse_pos[0] > self.pos[0] and mouse_pos[0] < self.pos[0] + CARD_WIDTH and mouse_pos[1] > self.pos[1] and mouse_pos[1] < self.pos[1] + CARD_HEIGHT:
            self.hover = True
        else:
            self.hover = False """
        
        #use collidepoint instead
        if pygame.Rect(self.pos[0], self.pos[1], CARD_WIDTH, CARD_HEIGHT).collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

    def draw_hover(self):
        # draw hover border
        pygame.draw.rect(self.display_surface, CARD_BORDER_COLOR_ACTIVE,
                         (self.pos[0], self.pos[1], CARD_WIDTH, CARD_HEIGHT), CARD_BORDER)
        
    def add(self):
        self.add_btn.draw()
        #check if clicked and update value and player stat
        if self.add_btn.clicked:
            print('test')
            self.value += 1
            if self.text == 'health':
                self.player.health += 1
            elif self.text == 'defense':
                self.player.defense += 1
            elif self.text == 'attack':
                self.player.attack += 1
            elif self.text == 'speed':
                self.player.speed += 1
            """ elif self.text == 'knife':
                self.player.knife += 1
            elif self.text == 'bolo':
                self.player.bolo += 1
            elif self.text == 'molotov':
                self.player.molotov += 1 """
            self.draw()

    def minus(self):
        self.minus_btn.draw()
        #check if clicked and update value and player stat
        if self.minus_btn.clicked and self.value > 0:
            print('test')
            self.value -= 1
            if self.text == 'health':
                self.player.health -= 1
            elif self.text == 'defense':
                self.player.defense -= 1
            elif self.text == 'attack':
                self.player.attack -= 1
            elif self.text == 'speed':
                self.player.speed -= 1
            """ elif self.text == 'knife':
                self.player.knife -= 1
            elif self.text == 'bolo':
                self.player.bolo -= 1
            elif self.text == 'molotov':
                self.player.molotov -= 1 """
            self.draw()

        
    """ def add(self):
        # draw plus button below icon
        self.display_surface.blit(
            self.plus_button,
            (self.pos[0] + CARD_WIDTH/2 - self.plus_button.get_width()/2 + 50,
             self.pos[1] + CARD_HEIGHT/2 - self.plus_button.get_height()/2 + 100))
        # if clicked add update value and player text
        if self.check_hover and self.can_click:
            if pygame.mouse.get_pressed()[0] :
                #update value and player stat
                self.value += 1
                if self.text == 'health':
                    self.player.health += 1
                elif self.text == 'defense':
                    self.player.defense += 1
                elif self.text == 'attack':
                    self.player.attack += 1
                elif self.text == 'speed':
                    self.player.speed += 1

                #reset click cooldown
                self.can_click = False
                self.click_time = pygame.time.get_ticks()
                
                print('test plus')
                self.draw()

    def minus(self):
        # draw minus button below icon
        self.display_surface.blit(
            self.minus_button,
            (self.pos[0] + CARD_WIDTH/2 - self.minus_button.get_width()/2 - 50,
             self.pos[1] + CARD_HEIGHT/2 - self.minus_button.get_height()/2 + 100))

        # if clicked minus update value and player text
        if self.check_hover and self.can_click:
            if pygame.mouse.get_pressed()[0] and self.value > 0:
                #update value and player stat
                self.value -= 1
                if self.text == 'health':
                    self.player.health -= 1
                elif self.text == 'defense':
                    self.player.defense -= 1
                elif self.text == 'attack':
                    self.player.attack -= 1
                elif self.text == 'speed':
                    self.player.speed -= 1
               
                #reset click cooldown
                self.can_click = False
                self.click_time = pygame.time.get_ticks()
                
                print('test minus')
                self.draw()
                #q: why is it still clicking even i dont hover over the card?
                #a: 


                #q: why the player stat is reseting when i click the card?
 """

    def update(self):
        self.draw()
        self.check_hover()
        if self.hover:
            self.draw_hover()


class Button:
    def __init__(self, pos, image, display_surface):
        self.pos = pos
        self.image = image
        self.display_surface = display_surface
        self.hover = False
        self.click_time = None
        self.click_cooldown = 1000  # Set cooldown period in milliseconds (1000 = 1 second)
        self.can_click = True
        self.clicked = False

    def check_hover(self):
        # Check if mouse is hovering over the button
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height()).collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False

    def draw_hover(self):
        # Draw hover border
        pygame.draw.rect(self.display_surface, CARD_BORDER_COLOR_ACTIVE,
                         (self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height()), CARD_BORDER)

    def check_click(self):
        self.check_hover()
        if self.hover and self.can_click:
            if pygame.mouse.get_pressed()[0]:
                # Reset click cooldown
                self.click_time = pygame.time.get_ticks()
                self.can_click = False  # Disable subsequent clicks during cooldown period
                self.draw()
                self.clicked = True
            else:
                self.clicked = False
        else:
            self.clicked = False

    def draw(self):
        self.display_surface.blit(self.image, self.pos)
        self.check_click()
        self.check_hover()
        if self.hover:
            self.draw_hover()

    def update(self):
        # Update click cooldown based on current time
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= self.click_cooldown:
                self.can_click = True  # Enable clicks after cooldown period

#for minus and plus button
""" class Button:
    def __init__(self, pos, image, display_surface):
        self.pos = pos
        self.image = image
        self.display_surface = display_surface
        self.hover = False
        self.click_time = None
        self.can_click = True
        self.clicked = False

    def click_cooldown(self):
        if not self.can_click:
            current_time = pygame.time.get_ticks()
            if current_time - self.click_time >= 1000:
                self.can_click = True
                self.clicked = False


    def check_hover(self):
        # check if mouse is hovering over card
        mouse_pos = pygame.mouse.get_pos()
        if pygame.Rect(self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height()).collidepoint(mouse_pos):
            self.hover = True
        else:
            self.hover = False
    
    def draw_hover(self):
        # draw hover border
        pygame.draw.rect(self.display_surface, CARD_BORDER_COLOR_ACTIVE,
                         (self.pos[0], self.pos[1], self.image.get_width(), self.image.get_height()), CARD_BORDER)
    
    def if_clicked(self):
        self.check_hover()
        if self.hover and self.can_click:
            if pygame.mouse.get_pressed()[0]:
                #reset click cooldown
                self.can_click = False
                self.click_time = pygame.time.get_ticks()
                self.draw()
                self.clicked = True
            else:
                self.clicked = False
        else:
            #self.can_click = False
            self.clicked = False
            

    def draw(self):
        self.display_surface.blit(self.image, self.pos)
        self.if_clicked()
        self.click_cooldown()
        self.check_hover()
        if self.hover:
            self.draw_hover()

        
 """