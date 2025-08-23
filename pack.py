from character import Character
import pygame
from constants import ARENA_TILE_SIZE, Direction


class Pack(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)

    