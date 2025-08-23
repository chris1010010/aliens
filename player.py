from pack import Pack
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE, Direction


class Player(Pack):

    def __init__(self, arena):
        grid_x = arena.grid_width // 2
        grid_y = arena.grid_height // 2
        super().__init__(grid_x, grid_y)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = Direction.UP
        elif keys[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT
        elif keys[pygame.K_DOWN]:
            self.direction = Direction.DOWN
        elif keys[pygame.K_LEFT]:
            self.direction = Direction.LEFT

        super().update(dt)