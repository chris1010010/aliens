import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE, MARINE_SPAWN_CHANCE
from egg import Egg
from civilian import Civilian
from marine import Marine
import sys
import random


class Arena:
    grid_color = (40,40,40)

    def __init__(self):
        self.grid_width = SCREEN_WIDTH // ARENA_TILE_SIZE
        self.grid_height = SCREEN_HEIGHT // ARENA_TILE_SIZE
        self.human_spawn_rate = 5 # per minute
        self.time_since_last_human = 0.0

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

    def try_spawn_human(self, dt):
        self.time_since_last_human += dt
        
        if self.time_since_last_human > 60.0 / self.human_spawn_rate:
            if random.random() > MARINE_SPAWN_CHANCE:
                Civilian(self)
            else:
                Marine(self)
            self.time_since_last_human = 0


    def hits_wall(self, character):
        return character.grid_x <= 0 or character.grid_x >= self.grid_width - 1 or character.grid_y <= 0 or character.grid_y >= self.grid_height - 1
    

    def collision_checks(self, player, humans, aliens):
        if self.hits_wall(player) or player.colliding_with(player):
            print("Game over!")
            sys.exit(0)
        
        for human in humans:
            if self.hits_wall(human):
                if not human.infected:
                    human.infect()
                human.bounce(self)
            elif player.colliding_with(human):
                human.kill()
                player.speed += 0.1
                if isinstance(human, Marine):
                    player.shrink()
            else:
                for alien in aliens:
                    if human.colliding_with(alien):
                        if isinstance(human, Marine):
                            alien.kill()
                        else:
                            alien.speed += 0.1
                        human.kill()
                        break

        for alien in aliens:
            if self.hits_wall(alien):
                alien.bounce(self)
            elif player.colliding_with(alien):
                alien.kill()
                player.grow()
                
