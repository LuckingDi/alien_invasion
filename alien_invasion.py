import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏
    pygame.init()
    # 导入设置类
    ai_settings = Settings()
    # 确定游戏屏幕尺寸
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 游戏框上的标题
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    '''开始游戏的主循环'''
    while True:

        # 监视键盘和鼠标事件方法
        gf.check_events(ai_settings, screen, ship, bullets)
        # 飞船位置调整方法
        ship.update()
        # 更新子弹位置，并删除已消失的子弹
        gf.update_bullets(bullets)
        # 更新屏幕方法
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()



