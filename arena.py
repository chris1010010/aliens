import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ARENA_TILE_SIZE, MARINE_SPAWN_CHANCE, HUMAN_SPAWN_RATE, SPEED_INCREASE_ON_CONSUMING_HUMAN
from egg import Egg
from civilian import Civilian
from marine import Marine
import random
from game import exit_game


class Arena:
    grid_color = (30,30,30)

    def __init__(self, stats):
        self.stats = stats
        self.grid_width = SCREEN_WIDTH // ARENA_TILE_SIZE
        self.grid_height = SCREEN_HEIGHT // ARENA_TILE_SIZE
        self.human_spawn_rate = HUMAN_SPAWN_RATE
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
                self.stats.civilians_spawned += 1
            else:
                Marine(self)
                self.stats.marines_spawned += 1
            self.time_since_last_human = 0


    def hits_wall(self, character):
        return character.grid_x <= 0 or character.grid_x >= self.grid_width - 1 or character.grid_y <= 0 or character.grid_y >= self.grid_height - 1
    

    def collision_checks(self, player, humans, aliens):
        if self.hits_wall(player):
            exit_game(self.stats, "You hit the wall")
        if  player.colliding_with(player):
            exit_game(self.stats, "You collided with yourself")
        
        for human in humans:
            if self.hits_wall(human):
                if not human.infected:
                    human.infect()
                    self.stats.humans_infected += 1
                human.bounce(self)
            elif player.colliding_with(human):
                human.kill()
                player.speed += SPEED_INCREASE_ON_CONSUMING_HUMAN
                self.stats.humans_consumed_by_player += 1
                if isinstance(human, Marine):
                    player.shrink(self.stats)
                    self.stats.attacked_by_marine += 1
            else:
                for alien in aliens:
                    if human.colliding_with(alien):
                        if isinstance(human, Marine):
                            alien.kill()
                        else:
                            alien.speed += SPEED_INCREASE_ON_CONSUMING_HUMAN
                        human.kill()
                        break

        for alien in aliens:
            if self.hits_wall(alien):
                alien.bounce(self)
            elif player.colliding_with(alien):
                alien.kill()
                player.grow()
                self.stats.aliens_added_to_pack += 1
                
