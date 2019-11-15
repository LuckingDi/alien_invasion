import pygame


class Settings():
    '''设置类'''
    def __init__(self):
        # 导入图片
        self.image = pygame.image.load("../../images/xx.bmp")
        self.screen_weight = 1200
        self.screen_height = 800
        self.color = ()