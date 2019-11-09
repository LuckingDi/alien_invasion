import sys
import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen

        self.image = pygame.image.load('../images/2.bmp')
        # 定义图片的x/y轴
        self.image_rect = self.image.get_rect()
        # 定义界面的x/y轴
        self.screen_rect = self.screen.get_rect()
        # 定义图片的位置在游戏界面的中间
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.centery = self.screen_rect.centery
        # 判断是否移动的属性
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 移动速度
        self.speed = 2

        # 小数化X/Y轴
        self.imagex = float(self.image_rect.centerx)
        self.imagey = float(self.image_rect.centery)

    def bj(self):
        self.screen.fill((20, 178, 251))

    def blit(self):
        # 将图片放到既定的图片位置
        self.screen.blit(self.image, self.image_rect)

    def checks_keydown_event(self, event):
        '''响应按下按键'''
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_UP:
            self.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.moving_down = True

    def checks_keyup_event(self, event):
        '''响应松开按键'''
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
        elif event.key == pygame.K_UP:
            self.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.moving_down = False

    def event_down(self):
        '''图片移动的具体操作'''
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.imagex += self.speed
        if self.moving_left and self.image_rect.left > self.screen_rect.left:
            self.imagex -= self.speed
        if self.moving_up and self.image_rect.top > self.screen_rect.top:
            self.imagey -= self.speed
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.imagey += self.speed

        self.image_rect.centerx = self.imagex
        self.image_rect.centery = self.imagey

    def moving(self):
        '''捕捉键盘操作'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                '''按键操作'''
            elif event.type == pygame.KEYDOWN:
                self.checks_keydown_event(event)
                print(event.key)
                '''松键操作'''
            elif event.type == pygame.KEYUP:
                self.checks_keyup_event(event)
                print(event.key)


