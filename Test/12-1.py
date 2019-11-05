import sys

import pygame


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))

    pygame.display.set_caption("Test")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((20, 178, 251))
        image = pygame.image.load('../images/1.bmp')
        image_rect = image.get_rect()
        screen_rect = screen.get_rect()
        image_rect.centerx = screen_rect.centerx
        image_rect.centery = screen_rect.centery
        screen.blit(image, image_rect)
        pygame.display.flip()


run_game()