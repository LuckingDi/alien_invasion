import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))

    pygame.display.set_caption("Test")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((140, 190, 255))
        pygame.display.flip()


run_game()