
from character import Character
import pygame
from constants import Direction

class Civilian(Character):

    def __init__(self, arena):
        super().__init__(0, 0)
        self.colour = (0,255,0)
        # Always spawns at center of one arena side
        if self.direction == Direction.DOWN or self.direction == Direction.DOWN_RIGHT:
            self.grid_x = arena.grid_width // 2
        elif self.direction == Direction.LEFT or self.direction == Direction.DOWN_LEFT:
            self.grid_x = arena.grid_width - 1
            self.grid_y = arena.grid_height // 2
        elif self.direction == Direction.UP or self.direction == Direction.UP_LEFT:
            self.grid_x = arena.grid_width // 2
            self.grid_y = arena.grid_height - 1
        elif self.direction == Direction.RIGHT or self.direction == Direction.UP_RIGHT:
            self.grid_y = arena.grid_height // 2

        self.calc_position()


    