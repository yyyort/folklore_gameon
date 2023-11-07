import pygame
from settings import *
from debug import debug

class NewUpgrade:
    def __init__(self, player):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        #self.weapon = weapon
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE + 20)
        
        self.cards = []
        self.weapon_cards = []

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
        
        # weapon card setup
        """ self.weapon_card_pos = [(CARD_WIDTH + CARD_SPACING) * i +
                            CARD_SPACING for i in range(3)]
        self.weapon_card_pos_y = [CARD_SPACING for i in range(3)]
        self.weapon_card_text = [
            'knife',
            'bolo',
            'molotov']
        self.weapon_card_value = [
            self.player.knife,
        
         """

    def create_cards(self):
        for i in range(len(self.card_pos)):
            self.cards.append(Card((self.card_pos[i], self.card_pos_y[i]),
                              self.card_text[i], self.card_value[i], self.player, self.display_surface))

    def display_stats(self):
        # display player stats in right of the cards
        health = self.font.render('Health: ' + str(self.player.health), False, TEXT_COLOR)
        defense = self.font.render('Defense: ' + str(self.player.defense), False, TEXT_COLOR)
        attack = self.font.render('Attack: ' + str(self.player.attack), False, TEXT_COLOR)
        speed = self.font.render('Speed: ' + str(self.player.speed), False, TEXT_COLOR)
        """ knife = self.font.render('Knife: ' + str(self.player.knife), False, TEXT_COLOR)
        bolo = self.font.render('Bolo: ' + str(self.player.bolo), False, TEXT_COLOR)
        molotov = self.font.render('Molotov: ' + str(self.player.molotov), False, TEXT_COLOR) """
        
        self.display_surface.blit(health, (self.card_pos[-1] + CARD_WIDTH + 50, self.card_pos_y[-1]))
        self.display_surface.blit(defense, (self.card_pos[-1] + CARD_WIDTH + 50, self.card_pos_y[-1] + 50))
        self.display_surface.blit(attack, (self.card_pos[-1] + CARD_WIDTH + 50, self.card_pos_y[-1] + 100))
        self.display_surface.blit(speed, (self.card_pos[-1] + CARD_WIDTH + 50, self.card_pos_y[-1] + 150))
        """ self.display_surface.blit(knife, (self.card_pos[0] + CARD_WIDTH + 50, self.card_pos_y[0] + 200))
        self.display_surface.blit(bolo, (self.card_pos[0] + CARD_WIDTH + 50, self.card_pos_y[0] + 250))
        self.display_surface.blit(molotov, (self.card_pos[0] + CARD_WIDTH + 50, self.card_pos_y[0] + 300)) """


    def display(self):
        self.create_cards()
        for card in self.cards:
            card.update()
        
        self.display_stats()


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
        self.draw_value()
        
    def draw_value(self):
        #draw value between plus and minus buttons
        value = self.font.render(str(self.value), False, TEXT_COLOR)
        self.display_surface.blit(value,
                                    (self.pos[0] + CARD_WIDTH/2 - value.get_width()/2,
                                     self.pos[1] + CARD_HEIGHT/2 - value.get_height()/2 + 50))
        
    def update_value(self):
        #update value
        if self.text == 'health':
            self.value = self.player.health
        elif self.text == 'defense':
            self.value = self.player.defense
        elif self.text == 'attack':
            self.value = self.player.attack
        elif self.text == 'speed':
            self.value = self.player.speed
        """ elif self.text == 'knife':
            self.value = self.player.knife
        elif self.text == 'bolo':
            self.value = self.player.bolo
        elif self.text == 'molotov':
            self.value = self.player.molotov """

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
        self.add_btn = Button((self.pos[0] + CARD_WIDTH/2 - self.plus_button.get_width()/2 + 50,
             self.pos[1] + CARD_HEIGHT/2 - self.plus_button.get_height()/2 + 100), self.plus_button, self.display_surface)
        self.add_btn.draw()
        #check if clicked and update value and player stat
        if self.add_btn.clicking:
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
            #update value
            self.update_value()
            self.draw_value()
            

    def minus(self):
        self.minus_btn = Button((self.pos[0] + CARD_WIDTH/2 - self.minus_button.get_width()/2 - 50,
             self.pos[1] + CARD_HEIGHT/2 - self.minus_button.get_height()/2 + 100), self.minus_button, self.display_surface)
     
        self.minus_btn.draw()
        #check if clicked and update value and player stat
        if self.minus_btn.clicking:
            print(self.value)
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
            #update value
            self.update_value()
            self.draw_value()

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
        self.clicking = False

        
    def click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.check_hover()
                if self.hover:
                    print('test')
                    self.clicking = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.clicking = False

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

    def draw(self):
        debug(self.clicking)
        self.display_surface.blit(self.image, self.pos)
        #self.cooldown()
        self.check_hover()
        if self.hover:
            self.draw_hover()
            self.click()