from character import Character
import pygame
from constants import ARENA_TILE_SIZE


class Pack(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, ARENA_TILE_SIZE // 2, 2)

