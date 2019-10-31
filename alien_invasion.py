import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    '''初始化游戏并创建一个屏幕对象'''
    # 初始化背景设置
    pygame.init()

    ai_settings = Settings()

    # 调用 pygame.display.set_mode()创建一个名为screen的显示窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # 窗口标题
    pygame.display.set_caption("外星人入侵")

    # 创建一艘飞船
    ship = Ship(screen)

    '''开始游戏主循环'''
    while True:

        '''监视键盘和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        '''每次循环时都重绘屏幕'''
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        '''让最近绘制的屏幕可见
            每次执行while循环时都绘制一个空屏幕并擦去旧屏幕，使得只有新屏幕可见，
            在我们移动游戏元素时，pygame.display.file()将不断更新屏幕，
            以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果'''
        pygame.display.flip()


run_game()

