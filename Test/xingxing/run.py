import sys
import pygame
from pygame.sprite import Group
from xx import Settings
import Function as fg


def Run():
    # 初始化游戏
    pygame.init()
    # 确定屏幕尺寸
    screen = pygame.display.set_mode(
        (1200, 800)
    )
    # 导入设置类
    ai_settings = Settings(screen)
    # 标题
    pygame.display.set_caption("漫天繁星")
    # 更新背景颜色
    color = fg.chenge_bg_color()
    screen.fill(color)

    # 创建星星实例
    xxs = Group()
    # 创建星星群
    fg.create_fleet(ai_settings, screen, xxs)

    '''开始游戏'''
    while True:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_0:
                    color1 = fg.chenge_bg_color(0)
                    screen.fill(color1)
                elif event.key == pygame.K_1:
                    color1 = fg.chenge_bg_color(1)
                    screen.fill(color1)
        xxs.draw(screen)
        fg.update_xxs(xxs)
        fg.create_fleet(ai_settings, screen, xxs)
        pygame.display.flip()





Run()