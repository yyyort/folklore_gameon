import pygame as pg
from settings import *

class Entity(pg.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)
        self.direction = pg.math.Vector2()
        self.frame_index = 0
        self.animation_speed = 0.15
        
    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        self.collision('x')
        self.hitbox.y += self.direction.y * speed
        self.collision('y')
        self.rect.center = self.hitbox.center
        
    def collision(self, direction):
        if direction == 'x': # X = Horizontal
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == 'y': # Y = Vertical
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom