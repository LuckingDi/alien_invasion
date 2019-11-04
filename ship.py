import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen

        '''加载飞机图像并获取外界矩形'''
        # 加载图片
        self.image = pygame.image.load('images/ship.bmp')
        # 获取外接矩形
        self.rect = self.image.get_rect()
        # 获取游戏界面的矩形
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在指定屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞机'''
        self.screen.blit(self.image, self.rect)