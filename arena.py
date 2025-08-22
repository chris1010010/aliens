import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE

class Arena:

    def __init__(self):
        self.grid_width = SCREEN_WIDTH // ARENA_TILE_SIZE
        self.grid_height = SCREEN_HEIGHT // ARENA_TILE_SIZE

    grid_color = (64,64,64)

    def draw(self, screen):

        for x in range(ARENA_TILE_SIZE, SCREEN_WIDTH, ARENA_TILE_SIZE):
            pygame.draw.line(screen, Arena.grid_color, pygame.Vector2(x, 0), pygame.Vector2(x, SCREEN_HEIGHT))

        for y in range(ARENA_TILE_SIZE, SCREEN_HEIGHT, ARENA_TILE_SIZE):
            pygame.draw.line(screen, Arena.grid_color, pygame.Vector2(0, y), pygame.Vector2(SCREEN_WIDTH, y))
