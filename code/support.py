import pygame as pg 
from csv import reader
from os import walk

def import_csv(path):
    terrain_map = []
    
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = []
    
    for _,_, image_files in walk(path):
        for image in image_files:
            full_path = f'{path}/{image}'
            image_surface = pg.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)
        return surface_list