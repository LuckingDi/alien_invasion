import pygame


class Settings():
    '''设置类'''
    def __init__(self, screen):
        # 导入图片
        self.image = pygame.image.load("../../images/xx.bmp")
        self.screen_wight = 1200
        self.screen_height = 800
        self.screen = screen
        self.image_rect = self.image.get_rect()

        self.image_rect.x = self.image_rect.width
        self.image_rect.y = self.image_rect.height

        self.x = float(self.image_rect.x)

    def chenge_bg_color(self, event=''):
        bg_color = (240, 240, 240)
        if event == 0:
            bg_color = (150, 240, 160)
        elif event == 1:
            bg_color = (240, 120, 160)
        return bg_color

    def blitme(self):
        self.screen.blit(self.image, self.image_rect)
