import pygame
from constants import ARENA_TILE_SIZE, Direction
import random


class Character(pygame.sprite.Sprite):

    def __init__(self, grid_x, grid_y, speed = 1.0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.grid_x = grid_x
        self.grid_y = grid_y
        self.position = pygame.Vector2(grid_x * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2, 
                                       grid_y * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2)
        self.direction = random.choice(list(Direction))
        self.speed = speed
        self.move_countdown = 1.0

    def update(self, dt):

        self.move_countdown -= dt * self.speed

        if self.move_countdown <= 0:
            self.move()
            self.move_countdown = 1.0


    def move(self):
        if self.direction == Direction.UP:
            self.grid_y -= 1
        elif self.direction == Direction.RIGHT:
            self.grid_x += 1
        elif self.direction == Direction.DOWN:
            self.grid_y += 1
        elif self.direction == Direction.LEFT:
            self.grid_x -= 1
        self.position = pygame.Vector2(self.grid_x * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2, 
                                       self.grid_y * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2)
