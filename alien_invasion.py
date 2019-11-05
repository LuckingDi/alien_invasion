import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


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

    '''开始游戏的主循环'''
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()



