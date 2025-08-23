from character import Character
import pygame
from constants import ARENA_TILE_SIZE, Direction


class Pack(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)

    def triangle(self):
        rotation = 0
        match self.direction:
            case Direction.UP:
                rotation = 180
            case Direction.RIGHT: 
                rotation = 270
            case Direction.LEFT:
                rotation = 90

        radius = ARENA_TILE_SIZE // 2
        forward = pygame.Vector2(0, 1).rotate(rotation)
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * radius / 1.5
        a = self.position + forward * radius
        b = self.position - forward * radius - right
        c = self.position - forward * radius + right
        return [a, b, c]

    def draw(self, screen):
        #pygame.draw.circle(screen, (255,255,255), self.position, ARENA_TILE_SIZE // 2, 2)
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

