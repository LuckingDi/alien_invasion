import pygame
import file2 as file


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))

    pygame.display.set_caption("Test")
    # 定义背景颜色

    image1 = file.Ship(screen)

    while True:
        image1.bj()
        image1.moving()
        image1.event_down()
        image1.blit()

        pygame.display.flip()


run_game()