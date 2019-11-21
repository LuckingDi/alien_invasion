import pygame
from pygame.sprite import Sprite


class Settings(Sprite):
    '''设置类'''
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        # 导入图片
        self.image = pygame.image.load("../../images/xx.bmp")

        self.rect = self.image.get_rect()
        self.screen_wight = 1200
        self.screen_height = 800
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        # 星星移动的速度
        self.xx_speed_factor = 1
        # 星星向下移动的速度
        self.fleet_drop_speed = 10
        # fleet_direction为1的时候表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.xx_speed_factor
        self.rect.x = self.x
