import sys
import pygame

from xx import Settings


def Run():
    # 初始化游戏
    pygame.init()
    # 导入设置类
    ai_settings = Settings()
    # 确定屏幕尺寸
    screen = pygame.display.set_mode(
        (ai_settings.screen_wight, ai_settings.screen_height)
    )
    # 标题
    pygame.display.set_caption("漫天繁星")
    # 更新背景颜色
    color = ai_settings.chenge_bg_color()
    screen.fill(color)

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
                    color1 = ai_settings.chenge_bg_color(0)
                    screen.fill(color1)
                elif event.key == pygame.K_1:
                    color1 = ai_settings.chenge_bg_color(1)
                    screen.fill(color1)

        pygame.display.flip()


Run()