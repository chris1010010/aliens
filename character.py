import pygame
from constants import ARENA_TILE_SIZE

class Character(pygame.sprite.Sprite):

    def __init__(self, grid_x, grid_y):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(grid_x * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2, 
                                       grid_y * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2)
        self.velocity = pygame.Vector2(0, 0)