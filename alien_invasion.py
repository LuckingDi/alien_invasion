import sys

import pygame
from settings import Settings
from ship import Ship

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
    ship = Ship(screen)

    '''开始游戏的主循环'''
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 每次循环时都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()



