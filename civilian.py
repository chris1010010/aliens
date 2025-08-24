
from human import Human
import pygame
from constants import ARENA_TILE_SIZE, Direction, CIVILIAN_START_SPEED

class Civilian(Human):
    civ_up = pygame.image.load('assets/human_a_up.png')
    civ_down = pygame.image.load('assets/human_a_down.png')
    civ_left = pygame.image.load('assets/human_a_left.png')
    civ_right = pygame.image.load('assets/human_a_right.png')
    civ_up_left = pygame.image.load('assets/human_a_up_left.png')
    civ_up_right = pygame.image.load('assets/human_a_up_right.png')
    civ_down_left = pygame.image.load('assets/human_a_down_left.png')
    civ_down_right = pygame.image.load('assets/human_a_down_right.png')

    def __init__(self, arena):
        super().__init__(arena, CIVILIAN_START_SPEED)
        self.colour = (0,255,0)

    def draw(self, screen):
        image = None
        match self.direction:
            case Direction.DOWN :
                image = Civilian.civ_down
            case Direction.LEFT:
                image = Civilian.civ_left
            case Direction.RIGHT:
                image = Civilian.civ_right
            case Direction.DOWN_LEFT:
                image = Civilian.civ_down_left
            case Direction.DOWN_RIGHT:
                image = Civilian.civ_down_right
            case Direction.UP_LEFT:
                image = Civilian.civ_up_left
            case Direction.UP_RIGHT:
                image = Civilian.civ_up_right
            case _:
                image = Civilian.civ_up
        screen.blit(image, (self.position[0] - ARENA_TILE_SIZE // 2, 
                            self.position[1] - ARENA_TILE_SIZE // 2))
        super().draw(screen)

    