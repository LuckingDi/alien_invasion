import sys

import pygame


def check_events(ship):
    '''响应鼠标键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向左移动
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # 停止向右移动飞船
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # 停止向左移动
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                # 停止向左移动
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                # 停止向左移动
                ship.moving_down = False


def update_screen(ai_settings, screen, ship):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


