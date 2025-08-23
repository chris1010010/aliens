import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE
from egg import Egg
from civilian import Civilian
import sys


class Arena:
    grid_color = (64,64,64)

    def __init__(self):
        self.grid_width = SCREEN_WIDTH // ARENA_TILE_SIZE
        self.grid_height = SCREEN_HEIGHT // ARENA_TILE_SIZE
        self.civilian_spawn_rate = 5 # per minute
        self.time_since_last_civilian = 0.0

        self.top_eggs = []
        self.bottom_eggs = []
        self.left_eggs = []
        self.right_eggs = []

        self.spawn_eggs()



    def draw(self, screen):

        for x in range(ARENA_TILE_SIZE, SCREEN_WIDTH, ARENA_TILE_SIZE):
            pygame.draw.line(screen, Arena.grid_color, pygame.Vector2(x, 0), pygame.Vector2(x, SCREEN_HEIGHT))

        for y in range(ARENA_TILE_SIZE, SCREEN_HEIGHT, ARENA_TILE_SIZE):
            pygame.draw.line(screen, Arena.grid_color, pygame.Vector2(0, y), pygame.Vector2(SCREEN_WIDTH, y))


    def spawn_eggs(self):
        for i in range(0, self.grid_width):
            if (i != self.grid_width // 2):
                self.top_eggs.append(Egg(i, 0))
                self.bottom_eggs.append(Egg(i, self.grid_height - 1))
        for i in range(0, self.grid_height):
            if (i != self.grid_height // 2):
                self.left_eggs.append(Egg(0, i))
                self.right_eggs.append(Egg(self.grid_width - 1, i))

    def try_spawn_civilian(self, dt):
        self.time_since_last_civilian += dt
        
        if self.time_since_last_civilian > 60.0 / self.civilian_spawn_rate:
            Civilian(self)
            self.time_since_last_civilian = 0


    def hits_wall(self, character):
        return character.grid_x <= 0 or character.grid_x >= self.grid_width - 1 or character.grid_y <= 0 or character.grid_y >= self.grid_height - 1
    

    def collision_checks(self, player, humans, aliens):
        if self.hits_wall(player):
            print("Game over!")
            sys.exit(0)
        
        for human in humans:
            if self.hits_wall(human):
                if not human.infected:
                    human.infect()
                human.bounce(self)
            elif human.colliding_with(player):
                human.kill()
                player.speed += 0.1
            else:
                for alien in aliens:
                    if human.colliding_with(alien):
                        human.kill()
                        alien.speed += 0.1
                        break

        for alien in aliens:
            if self.hits_wall(alien):
                alien.bounce(self)
                
