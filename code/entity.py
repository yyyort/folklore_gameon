import pygame as pg 
from settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pg.math.Vector2()
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.hitbox.y += self.direction.y * speed
        
        self.rect.center = self.hitbox.center
        
        # self.rect.center = self.hitbox.center