import pygame


class Ship():

    # 传进来整个程序窗口
    def __init__(self, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen

        '''加载飞船图像并获取其外接矩形'''
        # 加载图像，返回surface，存储在self.image中
        self.image = pygame.image.load('images/ship.bmp')
        # 获取相应surface的属性rect,处理rect对象时，可使用矩形四角和中心的x和y坐标，可通过设置这些值来指定矩形的位置
        # self.rect为飞船  self.screen 为屏幕
        self.rect = self.image.get_rect()
        # 屏幕矩形存储在self.screen_rect中拿到飞船位置的矩形
        self.screen_rect = screen.get_rect()

        '''将每艘新飞船放在屏幕底部中央'''
        # 将飞船中心的x坐标设置为表示屏幕的矩形的属性centerx
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
