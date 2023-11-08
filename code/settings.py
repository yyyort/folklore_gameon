import pygame as pg 

pg.init()
WIDTH = pg.display.Info().current_w
HEIGHT = pg.display.Info().current_h
TILESIZE = 64

FPS = 60

FONT = '../graphics/font/joystix.ttf'
FONT_SIZE = (18, 21, 24, 26, 32, 46, 52) # 0:1:2:3:4:5:6
FONT_COLOR = ((255, 0, 0), # RED 0
              (0, 255, 0), # GREEN 1
              (0, 0, 255), # BLUE 2 
              (0, 0, 0), # BLACK 3
              (255, 255, 255), # WHILE 4
              (255, 215, 0)) # YELLOW 5

HITBOX_OFFSET = {
    'outer_border' : (-26, -26),
    'inner_border' : (-32, -32),
    'other_border' : None,
    'player_hitbox' : (-21, -21)
}

player_data = {
    '' : {
        'health' : 100,
        'stamina' : 100,
        'speed' : 3,
        'sprint' : 1.50,
        'regen' : 1,
        }, # Default
    'male' : {
        'health' : 100,
        'stamina' : 100,
        'speed' : 3,
        'sprint' : 1.75,
        'regen' : 1.75,
        }, # Male
    'female' : {
        'health' : 75,
        'stamina' : 150,
        'speed' : 3,
        'sprint' : 2.50,
        'regen' : 1.75,
        }, # Female
}

player_info = {
    'exp' : 0,
    'level' : 0,
    'score' : 0,
    'total_score' : 0,
    'exp_cap' : 15,
}

weapon_data = {
    'knife' : {
        'damage' : 10,
        'cooldown' : 250,
        'graphics' : '../graphics/weapons/sword/full.png'  
    },
}

firearm_data = {
    'pistol' : {
        'damage' : 5,
        'cooldown' : 250,
        'graphics' : '../graphics/firearm/pistol/full.png'
    }
}

equipment_data = {
    'medkit' : {
        'strength' : 50,
        'cooldown' : 1000 * 20,
        'cost' : 75,
        'graphics' : '../graphics/equipment/medkit/full.png'
    },
    
    'molotov' : {
        'strength' : 50,
        'cooldown' : 1000 * 5,
        'cost' : 10,
        'graphics' : '../graphics/equipment/molotov/fill.png'
    }
}