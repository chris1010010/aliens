from pack import Pack
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE, Direction


class Player(Pack):

    def __init__(self, arena):
        grid_x = arena.grid_width // 2
        grid_y = arena.grid_height // 2
        super().__init__(grid_x, grid_y)
        # Make sure direction one of UP, RIGHT, DOWN, LEFT
        if self.direction == Direction.UP_RIGHT:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.UP_LEFT:
            self.direction = Direction.UP
        elif self.direction == Direction.DOWN_RIGHT:
            self.direction = Direction.DOWN
        elif self.direction == Direction.DOWN_LEFT:
            self.direction = Direction.LEFT
        self.colour = (255,0,0)
        self.cooldown_timer = 0

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
        elif keys[pygame.K_RETURN]:
            if self.cooldown_timer <= 0:
                self.cooldown_timer = 0.3
                self.grow()
        self.cooldown_timer -= dt

        super().update(dt)