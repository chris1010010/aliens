from pack import Pack
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE


class Player(Pack):

    def __init__(self, arena):
        grid_x = arena.grid_width // 2
        grid_y = arena.grid_height // 2
        super().__init__(grid_x, grid_y)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        #if keys[pygame.K_a]:
        #    self.rotate(-dt)
        #if keys[pygame.K_d]:
        #    self.rotate(dt)
        #if keys[pygame.K_w]:
        #    self.move(dt)
        #if keys[pygame.K_s]:
        #    self.move(-dt)