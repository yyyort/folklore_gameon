# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 64
HITBOX_OFFSET = {
	'player': -26,
	'object': -40,
	'grass': -10,
	'invisible': 0}

SOUDN_VOLUME = 0

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
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
UI_FONT_COLOR = 'white'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

#new upgrade menu
CARD_WIDTH = 200
CARD_HEIGHT = 300
CARD_BORDER = 5
CARD_BORDER_COLOR = 'black'
CARD_BORDER_COLOR_SELECTED = 'gold'
CARD_BORDER_COLOR_ACTIVE = 'gold'
CARD_BG_COLOR = 'white'
CARD_BG_COLOR_SELECTED = 'gold'
TEXT_COLOR = 'black'
CARD_SPACING = 20




TEXT_COLOR_HOVER = 'red'

""" 
player stat
health
defense
attack
speed
 """

#player
male_player_data = {
	'health': 100,
    'energy':60,
	'defense': 10,
    'attack': 10,
	'speed': 5,
}

female_player_data = {
	'health': 80,
    'energy':80,
	'defense': 8,
	'attack': 8,
	'speed': 7,
}

# player
""" male_player_data = {
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
} """

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
	'heal' : {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'},
    'normal': {'strength': 1,'cost': 1,'graphic':'../graphics/particles/flame/fire.png'},
	}

#item
item_data = {
	'molotov': {'strength': 5,'cost': 1,'graphic':'../graphics/particles/molotov/molotov.png'},
    'gun': {'strength': 5,'cost': 1,'graphic':'../graphics/items/gun.png'},
}

throwable_item_data = {
	'molotov': {'strength': 5,'cost': 1,'graphic':'../graphics/particles/molotov/molotov.png'},
}

# enemy
""" monster_data = {
	'squid': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
	'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'spirit': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
	'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}}
	 """

dialog_data = {
    'Dwende': {
        'Dwende',
	},
    'Engkanto': {
        'Engkanto'
	},
    'Kapre': {
		'Kapre',
	},
    'Tiyanak': {
        'Tiyanak',
	}
}

monster_data = {
    'Dwende': {'health': 100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'Engkanto': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw',  'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'Kapre': {'health': 100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    #'Tikbalang': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300},
	'Tiyanak': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

#enemy effect
""" 
Tikbalang - Melee (Knockback effects)
 Kapre - Melee (Crippled Effect or Slow)
 Dwende - Range (Magical Damage)
 Engkanto - Melee Normal Mob Tiyanak - Melee
 (May Speed Boost) Multo (Male/Female Ghost) - Melee Normal Mob
 """

#dialog
""" dialog_data = {
    'player_start': {
        'Ugh, this swampy place gives me the creeps.',
        'I shouldve just stayed back home in Iloilo.', 
		'Oh well, I took this job to cleanse that woman, so I better get to it, even though I have no idea where to start...',
		'Explore'
	},
	'player_sense': {
        'Hmm, I sense many restless spirits in this area. Something evil must be drawing them here. Explore'
	},
	'player_tired': {
        'Whew, that was tiring.', 
		'But why do I feel like there are even more monsters now?',
		'Something is behind this'
		'This cant be good...'
		'Albularyo comes across a Mangkukulam'
	},
    'mangkukulam': {
		'Ohh?',
        'What an unusual sight',
        'You dont belong here',
        'An albularyo that came all the way from Iloilo to act like the hero?',
        'You should be punished!'
	},
    'player_replay': {
        'How did you even know where I came from Iloilo?'
	},
    'mangkukulam_replay': {
		'Doesnt matter',
		'Things that dont belong here… We get rid of them',
		'Same goes to people',
		'Ohh, how pitiful',
		'Youre family wont see you for the last time',
		'Because Capiz will become your grave',
	}
} """