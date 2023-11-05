import pygame as pg 

d_width =  1280
d_height = 720
fps = 60

tile_size = 64

font = '../graphics/font/joystix.ttf'
font_size = (18, 18 * 2, 18 * 3, 18 * 4)
font_color = ((255, 0, 0), (0, 255, 0), (0, 0, 255))

player_data = {
    'male' : {
        'health' : 100,
        'stamina' : 100,
        'damage' : 1.75,
        'range' : 1.25,
        'speed' : 5,
        'sprint' : 2.50,
    },
    
    'female' : {
        'health' : 75,
        'stamina' : 50,
        'damage' : 1.25,
        'range' : 2.25,
        'speed' : 7.5,
        'sprint' : 3.00,
    },
    
    '' : {
        'health' : 0,
        'stamina' : 0,
        'damage' : 0,
        'range' :  0,
        'speed' :  0,
        'sprint' : 0,
    },
}