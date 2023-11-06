import pygame as pg 
pg.init()
# game setup
WIDTH    = pg.display.Info().current_w
HEIGTH   = pg.display.Info().current_h

FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -60,
	'grass': -40,
	'outer_wall': (0, 0),
 	'inner_wall' : (-32, -32)}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR = 200
ENERGY_BAR = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

TEXT_COLOR_HOVER = 'red'

# player
male_player_data = {
    'health': 100,
    'energy':60,
    'attack': 10,
    'magic': 4,
    'speed': 5
}

female_player_data = {
	'health': 80,
	'energy':80,
	'attack': 8,
	'magic': 6,
	'speed': 7
}

player_data = {
	'male' : {'health' : 100, 'stamina' : 75, 'speed' : 5, 'damage' : 2.50, 'sprint' : 1.50, 'regen' : 1.50},
	'female' : {'health' : 100, 'stamina' : 125, 'speed' : 7.5, 'damage' : 1.75, 'sprint' : 2.25, 'regen' : 1.50},
 	'' : {'health' : 100, 'stamina' : 100, 'speed' : 5, 'damage' : 2.50, 'sprint' : 1.50, 'regen' : 1.50}
}

# weapons 
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}
 }

# enemy
monster_data = {
	'squid': {'health': 100, 'exp':25, 'score': 10, 'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':100, 'score': 10, 'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':40, 'score': 10, 'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':15, 'score': 10, 'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
