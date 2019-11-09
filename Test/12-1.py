import sys

import pygame
from file_12_3 as file

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))

    pygame.display.set_caption("Test")
    image1 = image(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((20, 178, 251))
        image1.image
        pygame.display.flip()


run_game()