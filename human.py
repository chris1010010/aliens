
from character import Character
import pygame
import random
from constants import Direction
from alien import Alien

class Human(Character):

    def __init__(self, arena, speed):
        super().__init__(0, 0, speed)
        # Always spawns at center of one arena side
        if self.direction == Direction.DOWN or self.direction == Direction.DOWN_RIGHT:
            self.grid_x = arena.grid_width // 2
            self.grid_y = 1
        elif self.direction == Direction.LEFT or self.direction == Direction.DOWN_LEFT:
            self.grid_x = arena.grid_width - 2
            self.grid_y = arena.grid_height // 2
        elif self.direction == Direction.UP or self.direction == Direction.UP_LEFT:
            self.grid_x = arena.grid_width // 2
            self.grid_y = arena.grid_height - 2
        elif self.direction == Direction.RIGHT or self.direction == Direction.UP_RIGHT:
            self.grid_x = 1
            self.grid_y = arena.grid_height // 2

        self.calc_position()
        self.infected = False
        self.infection_countdown = 0.0


    def update(self, dt):
        self.try_change_direction(dt, 1.0)
        super().update(dt)

        if self.infected:
            self.infection_countdown -= dt
            if self.infection_countdown < 0:
                self.kill()
                Alien(self.grid_x, self.grid_y)


    def infect(self):
        self.infected = True
        self.infection_countdown = 5.0
        self.colour = (255,255,0)