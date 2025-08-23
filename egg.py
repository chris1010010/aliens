from character import Character
import pygame

class Egg(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, 0)

    