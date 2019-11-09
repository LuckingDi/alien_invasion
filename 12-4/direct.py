import sys

import pygame


def run_game():

    pygame.init()
    screen = pygame.display.set_mode((800, 500))
    while True:
        screen.fill((250, 114, 140))
        KeyDown()
        pygame.display.flip()


def KeyDown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)




run_game()