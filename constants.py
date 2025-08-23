from enum import Enum

SCREEN_WIDTH = 3200
SCREEN_HEIGHT = 1800

ARENA_TILE_SIZE = 100

Direction = Enum('Direction', ['UP', 'UP_RIGHT', 'RIGHT', 'DOWN_RIGHT', 'DOWN', 'DOWN_LEFT', 'LEFT', 'UP_LEFT'])
