import pygame
from constants import *
from arena import Arena
from player import Player
from egg import Egg
from human import Human
from alien import Alien

# Activate virtual enviironment in terminal:
# source .venv/bin/activate

def main():
    print("Starting Aliens!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Aliens")
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    humans = pygame.sprite.Group()
    aliens = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Egg.containers = (updatable, drawable)
    Human.containers = (humans, updatable, drawable)
    Alien.containers = (aliens, updatable, drawable)

    arena = Arena()
    player = Player(arena)


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        arena.try_spawn_civilian(dt)
            
        updatable.update(dt)

        arena.collision_checks(player, humans, aliens)
            
        screen.fill((0,0,0))

        arena.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
