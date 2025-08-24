from character import Character
import pygame
from constants import ARENA_TILE_SIZE, Direction, ALIEN_START_SPEED

class Alien(Character):
    alien_up = pygame.image.load('assets/alien_up.png')
    alien_down = pygame.image.load('assets/alien_down.png')
    alien_left = pygame.image.load('assets/alien_left.png')
    alien_right = pygame.image.load('assets/alien_right.png')
    alien_up_left = pygame.image.load('assets/alien_up_left.png')
    alien_up_right = pygame.image.load('assets/alien_up_right.png')
    alien_down_left = pygame.image.load('assets/alien_down_left.png')
    alien_down_right = pygame.image.load('assets/alien_down_right.png')

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, ALIEN_START_SPEED)
        self.colour = (0,30,0)

    def update(self, dt):
        self.try_change_direction(dt, 2.0)
        super().update(dt)
    
    def draw(self, screen):
        # super().draw(screen)
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
            image = Alien.alien_down_left
        case Direction.DOWN_RIGHT:
            image = Alien.alien_down_right
        case Direction.UP_LEFT:
            image = Alien.alien_up_left
        case Direction.UP_RIGHT:
            image = Alien.alien_up_right
        case _:
            image = Alien.alien_up
    screen.blit(image, (pos[0] - ARENA_TILE_SIZE // 2, 
                        pos[1] - ARENA_TILE_SIZE // 2))