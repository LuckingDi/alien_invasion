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

    def blitme(self):
        self.screen.blit(self.image, self.rect)

