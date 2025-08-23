from character import Character
import random
import pygame
from constants import ARENA_TILE_SIZE, Direction

class Alien(Character):
    alien_up = pygame.image.load('assets/alien_up.png')
    alien_down = pygame.image.load('assets/alien_down.png')
    alien_left = pygame.image.load('assets/alien_left.png')
    alien_right = pygame.image.load('assets/alien_right.png')

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, 1.0)
        self.colour = (255,0,255)

    def update(self, dt):
        self.try_change_direction(dt, 2.0)
        super().update(dt)
    
    def draw(self, screen):
        draw_alien(screen, self.position, self.direction)



def draw_alien(screen, pos, direction):
    image = None
    match direction:
        case Direction.DOWN :
            image = Alien.alien_down
        case Direction.LEFT:
            image = Alien.alien_left
        case Direction.RIGHT:
            image = Alien.alien_right
        case Direction.DOWN_LEFT:
            image = Alien.alien_down
        case Direction.DOWN_RIGHT:
            image = Alien.alien_down
        case _:
            image = Alien.alien_up
    screen.blit(image, (pos[0] - ARENA_TILE_SIZE // 2, 
                        pos[1] - ARENA_TILE_SIZE // 2))