from constants import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "True"
import pygame

Clock = pygame.time.Clock()
dt = 0

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = Clock.tick(60)/1000


if __name__ == "__main__":
    main()
