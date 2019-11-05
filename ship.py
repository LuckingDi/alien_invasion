import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

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

        # 在飞船的属性center中存储小数值
        self.center1 = float(self.rect.centerx)
        self.center2 = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center1 += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.height < self.screen_rect.top:
            self.center2 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom > 0:
            self.center2 += self.ai_settings.ship_speed_factor

        #

        # 根据self.center更新rect对象
        self.rect.centerx = self.center1
        self.rect.centery = self.center2



    def blitme(self):
        '''在指定位置绘制飞机'''
        self.screen.blit(self.image, self.rect)