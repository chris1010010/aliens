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
        self.calc_position()
        self.direction = random.choice(list(Direction))
        self.speed = speed
        self.move_countdown = 1.0
        self.colour = (255,255,255)


    def update(self, dt):

        if (self.speed > 0):
            self.move_countdown -= dt * self.speed

            if self.move_countdown <= 0:
                self.move()
                self.move_countdown = 1.0

    def triangle(self):
        rotation = 0
        match self.direction:
            case Direction.UP:
                rotation = 180
            case Direction.UP_RIGHT:
                rotation = 225
            case Direction.RIGHT: 
                rotation = 270
            case Direction.DOWN_RIGHT: 
                rotation = 315
            case Direction.LEFT:
                rotation = 90
            case Direction.DOWN_LEFT:
                rotation = 45
            case Direction.UP_LEFT:
                rotation = 135

        radius = ARENA_TILE_SIZE // 2
        forward = pygame.Vector2(0, 1).rotate(rotation)
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * radius / 1.5
        a = self.position + forward * radius
        b = self.position - forward * radius - right
        c = self.position - forward * radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)



    def move(self):
        if self.direction == Direction.UP or self.direction == Direction.UP_LEFT or self.direction == Direction.UP_RIGHT:
            self.grid_y -= 1
        if self.direction == Direction.RIGHT or self.direction == Direction.UP_RIGHT or self.direction == Direction.DOWN_RIGHT:
            self.grid_x += 1
        if self.direction == Direction.DOWN or self.direction == Direction.DOWN_RIGHT or self.direction == Direction.DOWN_LEFT:
            self.grid_y += 1
        if self.direction == Direction.LEFT or self.direction == Direction.UP_LEFT or self.direction == Direction.DOWN_LEFT:
            self.grid_x -= 1
        self.calc_position()

    def calc_position(self):
        self.position = pygame.Vector2(self.grid_x * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2, 
                                       self.grid_y * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2)