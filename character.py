import pygame
from constants import ARENA_TILE_SIZE, Direction
import random


class Character(pygame.sprite.Sprite):

    def __init__(self, grid_x, grid_y, speed = 1.0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.grid_x = grid_x
        self.grid_y = grid_y
        self.position = pygame.Vector2(0, 0)
        self.calc_position()
        self.direction = random.choice(list(Direction))
        self.speed = speed
        self.move_countdown = 1.0
        self.turn_cooldown = 0.5
        self.colour = (255,255,255)


    def update(self, dt):

        if (self.speed > 0):
            self.move_countdown -= dt * self.speed

            if self.move_countdown <= 0:
                self.move()
                self.move_countdown = 1.0


    def triangle(self, position = None, direction = None):
        if position == None:
            position = self.position
        if direction == None:
            direction = self.direction
        rotation = 0
        match direction:
            case Direction.UP:
                rotation = 180
            case Direction.UP_RIGHT:
                rotation = 225
            case Direction.RIGHT: 
                rotation = 270
            case Direction.DOWN_RIGHT: 
                rotation = 315
            case Direction.LEFT:
                rotation = 90
            case Direction.DOWN_LEFT:
                rotation = 45
            case Direction.UP_LEFT:
                rotation = 135

        radius = ARENA_TILE_SIZE // 2
        forward = pygame.Vector2(0, 1).rotate(rotation)
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * radius / 1.5
        a = position + forward * radius
        b = position - forward * radius - right
        c = position - forward * radius + right
        return [a, b, c]


    def draw(self, screen):
        pygame.draw.polygon(screen, self.colour, self.triangle(), 2)


    def move(self):
        if self.direction == Direction.UP or self.direction == Direction.UP_LEFT or self.direction == Direction.UP_RIGHT:
            self.grid_y -= 1
        if self.direction == Direction.RIGHT or self.direction == Direction.UP_RIGHT or self.direction == Direction.DOWN_RIGHT:
            self.grid_x += 1
        if self.direction == Direction.DOWN or self.direction == Direction.DOWN_RIGHT or self.direction == Direction.DOWN_LEFT:
            self.grid_y += 1
        if self.direction == Direction.LEFT or self.direction == Direction.UP_LEFT or self.direction == Direction.DOWN_LEFT:
            self.grid_x -= 1
        self.calc_position()


    def calc_position(self):
        self.position = pygame.Vector2(self.grid_x * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2, 
                                       self.grid_y * ARENA_TILE_SIZE + ARENA_TILE_SIZE // 2)
        

    def colliding_with(self, other):
        return self.grid_x == other.grid_x and self.grid_y == other.grid_y
    
    def turn_left(self):
        if self.direction == Direction.DOWN:
            self.direction = Direction.DOWN_RIGHT
        elif self.direction == Direction.DOWN_RIGHT:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.UP_RIGHT
        elif self.direction == Direction.UP_RIGHT:
            self.direction = Direction.UP
        elif self.direction == Direction.UP:
            self.direction = Direction.UP_LEFT
        elif self.direction == Direction.UP_LEFT:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.DOWN_LEFT
        elif self.direction == Direction.DOWN_LEFT:
            self.direction = Direction.DOWN

    def turn_right(self):
        if self.direction == Direction.DOWN:
            self.direction = Direction.DOWN_LEFT
        elif self.direction == Direction.DOWN_LEFT:
            self.direction = Direction.LEFT
        elif self.direction == Direction.LEFT:
            self.direction = Direction.UP_LEFT
        elif self.direction == Direction.UP_LEFT:
            self.direction = Direction.UP
        elif self.direction == Direction.UP:
            self.direction = Direction.UP_RIGHT
        elif self.direction == Direction.UP_RIGHT:
            self.direction = Direction.RIGHT
        elif self.direction == Direction.RIGHT:
            self.direction = Direction.DOWN_RIGHT
        elif self.direction == Direction.DOWN_RIGHT:
            self.direction = Direction.DOWN


    def try_change_direction(self, dt, upper_bound):
        self.turn_cooldown -= dt
        if self.turn_cooldown < 0 and random.uniform(0.0, upper_bound) < dt:
            if bool(random.choice([True, False])):
                self.turn_left()
            else:
                self.turn_right()
            self.turn_cooldown = 0.5
        
    
    def bounce(self, arena):
        left = 0
        right = arena.grid_width - 1
        top = 0
        bottom = arena.grid_height - 1

        if self.grid_x == left and self.grid_y == top:
            self.direction = Direction.DOWN_RIGHT
        elif self.grid_x == left and self.grid_y == bottom:
            self.direction = Direction.UP_RIGHT
        elif self.grid_x == right and self.grid_y == top:
            self.direction = Direction.DOWN_LEFT
        elif self.grid_x == right and self.grid_y == bottom:
            self.direction = Direction.UP_LEFT
        elif self.grid_x == left:
            self.direction = Direction.RIGHT
        elif self.grid_x == right:
            self.direction = Direction.LEFT
        elif self.grid_y == top:
            self.direction = Direction.DOWN
        elif self.grid_y == bottom:
            self.direction = Direction.UP
