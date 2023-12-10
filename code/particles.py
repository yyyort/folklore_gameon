import pygame
from support import import_folder
from random import choice, randint
from settings import *


class AnimationPlayer:
    def __init__(self):

        self.frames = {
            #items
            'molotov': import_folder('../graphics/particles/molotov/frames'),
            'gun': import_folder('../graphics/particles/gun/frames'),

            # magic
            'flame': import_folder('../graphics/particles/flame/frames'),
            'aura': import_folder('../graphics/particles/aura'),
            'heal': import_folder('../graphics/particles/heal/frames'),

            # attacks
            'claw': import_folder('../graphics/particles/claw'),
            'slash': import_folder('../graphics/particles/slash'),
            'sparkle': import_folder('../graphics/particles/sparkle'),
            'leaf_attack': import_folder('../graphics/particles/leaf_attack'),
            'thunder': import_folder('../graphics/particles/thunder'),

            # monster deaths
            'squid': import_folder('../graphics/particles/smoke_orange'),
            'raccoon': import_folder('../graphics/particles/raccoon'),
            'spirit': import_folder('../graphics/particles/nova'),
            'bamboo': import_folder('../graphics/particles/bamboo'),

            # leafs
            'leaf': (
                import_folder('../graphics/particles/leaf1'),
                import_folder('../graphics/particles/leaf2'),
                import_folder('../graphics/particles/leaf3'),
                import_folder('../graphics/particles/leaf4'),
                import_folder('../graphics/particles/leaf5'),
                import_folder('../graphics/particles/leaf6'),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf1')),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf2')),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf3')),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf4')),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf5')),
                self.reflect_images(import_folder(
                    '../graphics/particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

    def create_projectile(self, animation_type, pos, groups, direction):
        animation_frames = self.frames[animation_type]
        Projectile(pos, animation_frames, groups, direction)

    def create_gun_projectile(self, animation_type, pos, groups, direction):
        animation_frames = self.frames[animation_type]
        gun_projectile(pos, animation_frames, groups, direction)

    def create_monster_flame(self, pos, direction, animation_type, groups, damage):
        animation_frames = self.frames[animation_type]
        MonsterFlame(pos, direction, animation_frames, groups, damage)

class MonsterFlame(pygame.sprite.Sprite):
    def __init__(self, pos, direction, animation_frames, groups, damage):
        super().__init__(groups)
        self.sprite_type = 'monster_flame'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction
        self.damage = damage
    
    def animate(self):
        #print(self.direction)
        self.frame_index += self.animation_speed
        #make flame offset using random

        self.rect.x += self.direction.x * 5
        self.rect.y += self.direction.y * 5 

        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
        

class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups, direction):
        super().__init__(groups)
        self.sprite_type = 'molotov'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction

    def animate(self):
        #print(self.sprite_type)
        self.frame_index += self.animation_speed

        if self.direction == 'right':
            self.rect.x += 5 
        elif self.direction == 'left':
            self.rect.x -= 5 
        elif self.direction == 'up':
            self.rect.y -= 5 
        elif self.direction == 'down':
            self.rect.y += 5 

        if self.frame_index >= len(self.frames):
            self.create_particle_effects(10)
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]


    def create_particle_effects(self, num_effects):
        for _ in range(num_effects):
            # Calculate a random position around the projectile's center
            offset_x = randint(-50, 50)  # Adjust the offset values as needed
            offset_y = randint(-50, 50)  # Adjust the offset values as needed
            spawn_position = (self.rect.centerx + offset_x, self.rect.centery + offset_y)
            
            # Create a particle effect at the calculated position
            ParticleEffect(spawn_position, self.frames, self.groups())

    def update(self):
        self.animate()

class gun_projectile(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups, direction):
        super().__init__(groups)
        self.sprite_type = 'gun'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.direction = direction

    def animate(self):
        #print(self.sprite_type)
        self.frame_index += self.animation_speed

        if self.direction == 'right':
            self.rect.x += TILESIZE
        elif self.direction == 'left':
            self.rect.x -= TILESIZE
        elif self.direction == 'up':
            self.rect.y -= TILESIZE
        elif self.direction == 'down':
            self.rect.y += TILESIZE 

        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()


class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'item'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
