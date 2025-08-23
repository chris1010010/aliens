from character import Character
import pygame
from constants import ARENA_TILE_SIZE, Direction, ALIEN_MAX_PACK_SIZE


class Pack(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y)
        self.position_history = [] # Tuple (pos, grid_x, grid_y, direction)
        self.size = 1
        self.target_size = 1


    def update(self, dt):
        if len(self.position_history) == 0:
            self.position_history.append((self.position, self.grid_x, self.grid_y, self.direction))
        super().update(dt)

    def draw(self, screen):
        lenght = len(self.position_history)
        for i in range(lenght - 1, lenght - self.size - 1, -1):
            pos = self.position_history[i]
            pygame.draw.polygon(screen, self.colour, self.triangle(pos[0], pos[3]), 2)

    def move(self):
        super().move()
        self.position_history.append((self.position, self.grid_x, self.grid_y, self.direction))
        if len(self.position_history) > ALIEN_MAX_PACK_SIZE:
            del self.position_history[0]
        
        if self.target_size > self.size and self.size < len(self.position_history) - 1:
            self.size += 1


    def grow(self):
        if self.target_size < ALIEN_MAX_PACK_SIZE:
            self.target_size += 1
            #print("grow")
    