from character import Character
import pygame
from constants import ARENA_TILE_SIZE

class Egg(Character):
    egg_closed = pygame.image.load('assets/egg_closed.png')

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, 0)

    def draw(self, screen):
        # pygame.draw.circle(screen, (255,255,255), self.position, ARENA_TILE_SIZE // 2, 2)
        screen.blit(Egg.egg_closed, (self.position[0] - ARENA_TILE_SIZE // 2, 
                                     self.position[1] - ARENA_TILE_SIZE // 2))

