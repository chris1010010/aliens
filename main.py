import pygame
from constants import *
from arena import Arena
from player import Player
from egg import Egg

# Activate virtual enviironment in terminal:
# source .venv/bin/activate

def main():
    print("Starting Aliens!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Egg.containers = (updatable, drawable)

    arena = Arena()
    player = Player(arena)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
            
        screen.fill((0,0,0))

        arena.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
