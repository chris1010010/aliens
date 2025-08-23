from character import Character
import random

class Alien(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, 1.0)
        self.colour = (255,0,255)

    def update(self, dt):
        self.try_change_direction(dt, 2.0)
        super().update(dt)