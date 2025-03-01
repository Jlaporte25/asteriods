from constants import *
from player import *
from circleshape import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame

clock = pygame.time.Clock()

def main():
    running = True
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while running:
        dt = clock.tick(60)/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
