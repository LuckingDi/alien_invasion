import pygame
import file2 as file
from pygame.sprite import Group


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 800))

    pygame.display.set_caption("Test")
    # 定义背景颜色

    # 创建子弹编组
    bullets = Group()

    image1 = file.Ship(screen, bullets)
    while True:
        image1.bj()
        image1.moving()
        image1.event_down()
        image1.blit()
        image1.update_bullets()
        pygame.display.flip()


run_game()