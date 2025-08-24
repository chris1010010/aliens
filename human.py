
from character import Character
import pygame
from constants import Direction, ALIEN_INCUBATION_TIME, ARENA_TILE_SIZE
from alien import Alien

class Human(Character):
    hugger_up = pygame.image.load('assets/hugger_up.png')
    hugger_down = pygame.image.load('assets/hugger_down.png')
    hugger_left = pygame.image.load('assets/hugger_left.png')
    hugger_right = pygame.image.load('assets/hugger_right.png')
    hugger_up_left = pygame.image.load('assets/hugger_up_left.png')
    hugger_up_right = pygame.image.load('assets/hugger_up_right.png')
    hugger_down_left = pygame.image.load('assets/hugger_down_left.png')
    hugger_down_right = pygame.image.load('assets/hugger_down_right.png')

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
        self.infection_countdown = ALIEN_INCUBATION_TIME
        self.colour = (255,255,0)

    def draw(self, screen):
        if self.infected:
            image = None
            match self.direction:
                case Direction.DOWN :
                    image = Human.hugger_down
                case Direction.LEFT:
                    image = Human.hugger_left
                case Direction.RIGHT:
                    image = Human.hugger_right
                case Direction.DOWN_LEFT:
                    image = Human.hugger_down_left
                case Direction.DOWN_RIGHT:
                    image = Human.hugger_down_right
                case Direction.UP_LEFT:
                    image = Human.hugger_up_left
                case Direction.UP_RIGHT:
                    image = Human.hugger_up_right
                case _:
                    image = Human.hugger_up
            screen.blit(image, (self.position[0] - ARENA_TILE_SIZE // 4, 
                                self.position[1] - ARENA_TILE_SIZE // 2))
