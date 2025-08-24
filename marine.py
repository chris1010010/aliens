
from human import Human
import pygame
from constants import ARENA_TILE_SIZE, Direction

class Marine(Human):
    marine_up = pygame.image.load('assets/marine_up.png')
    marine_down = pygame.image.load('assets/marine_down.png')
    marine_left = pygame.image.load('assets/marine_left.png')
    marine_right = pygame.image.load('assets/marine_right.png')
    marine_up_left = pygame.image.load('assets/marine_up_left.png')
    marine_up_right = pygame.image.load('assets/marine_up_right.png')
    marine_down_left = pygame.image.load('assets/marine_down_left.png')
    marine_down_right = pygame.image.load('assets/marine_down_right.png')
    def __init__(self, arena):

        super().__init__(arena, 0.8)
        self.colour = (0,0,255)

    def draw(self, screen):
        image = None
        match self.direction:
            case Direction.DOWN :
                image = Marine.marine_down
            case Direction.LEFT:
                image = Marine.marine_left
            case Direction.RIGHT:
                image = Marine.marine_right
            case Direction.DOWN_LEFT:
                image = Marine.marine_down_left
            case Direction.DOWN_RIGHT:
                image = Marine.marine_down_right
            case Direction.UP_LEFT:
                image = Marine.marine_up_left
            case Direction.UP_RIGHT:
                image = Marine.marine_up_right
            case _:
                image = Marine.marine_up
        screen.blit(image, (self.position[0] - ARENA_TILE_SIZE // 2, 
                            self.position[1] - ARENA_TILE_SIZE // 2))


    