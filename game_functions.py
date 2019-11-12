import sys

import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向前移动
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向后移动
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    '''响应松开'''
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


def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    '''更新屏幕上的图像，并切换到新屏幕'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重新绘制所有子弹
    for bullets in bullets.sprites():
        # 先创建出对象，在这里为对象赋颜色，尺寸等信息
        bullets.draw_bullet()
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    '''更新子弹的位置，并删除已消失的子弹'''
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        # 空格键 创建一颗子弹，并将其加入到编组bullets中
        now_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(now_bullet)