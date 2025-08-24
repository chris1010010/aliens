from character import Character
import pygame
from constants import ARENA_TILE_SIZE, Direction, ALIEN_MAX_PACK_SIZE, PLAYER_START_SPEED
from alien import draw_alien
from game import exit_game


class Pack(Character):

    def __init__(self, grid_x, grid_y):
        super().__init__(grid_x, grid_y, PLAYER_START_SPEED)
        self.position_history = [] # Tuple (pos, grid_x, grid_y, direction)
        self.size = 1
        self.target_size = 1


    def update(self, dt):
        if len(self.position_history) == 0:
            self.position_history.append((self.position, self.grid_x, self.grid_y, self.direction))
        super().update(dt)


    def draw(self, screen):
        # Lead alien
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.grid_x * ARENA_TILE_SIZE, 
                                                          self.grid_y * ARENA_TILE_SIZE, 
                                                          ARENA_TILE_SIZE + 1, ARENA_TILE_SIZE + 1))
        draw_alien(screen, self.position, self.direction)
        # Rest of pack
        lenght = len(self.position_history)
        for i in range(lenght - 2, lenght - self.size - 1, -1):
            pos = self.position_history[i]
            draw_alien(screen, pos[0], pos[3])
            # pygame.draw.polygon(screen, self.colour, self.triangle(pos[0], pos[3]), 2)


    def move(self):
        super().move()
        self.position_history.append((self.position, self.grid_x, self.grid_y, self.direction))
        if len(self.position_history) > ALIEN_MAX_PACK_SIZE:
            del self.position_history[0]
        
        if self.target_size > self.size and self.size < len(self.position_history) - 1:
            self.size += 1


    def grow(self):
        if self.target_size < ALIEN_MAX_PACK_SIZE:
            self.target_size += 1
            #print("grow")


    def shrink(self, stats):
        self.size -= 1
        self.target_size -= 1
        if self.size == 0:
            exit_game(stats, "Colonial marines killed all xenomorphs of ypur pack")
    

    def colliding_with(self, other):
        lenght = len(self.position_history)
        start_offset = 0
        if self == other:
            start_offset = 1
        for i in range(lenght - 1 - start_offset, lenght - self.size - 1, -1):
            pos = self.position_history[i]
            if pos[1] == other.grid_x and pos[2] == other.grid_y:
                return True
        return False