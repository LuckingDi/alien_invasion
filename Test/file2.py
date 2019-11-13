import sys
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, screen, bulltes):
        super().__init__()
        self.screen = screen
        self.bullets = bulltes

        self.image = pygame.image.load('../images/2.bmp')
        self.bullet = pygame.image.load('../images/21.bmp')
        # 定义图片的x/y轴
        self.image_rect = self.image.get_rect()
        # 定义子弹的x/y轴
        self.bullet_rect = self.bullet.get_rect()
        # 定义界面的x/y轴
        self.screen_rect = self.screen.get_rect()
        # 定义图片的位置在游戏界面的中间
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.centery = self.screen_rect.centery
        # 设置子弹的位置
        self.bullet_rect.centerx = self.image_rect.centerx
        self.bullet_rect.centery = self.image_rect.centery
        self.bullet_rect.top = self.image_rect.top
        # 存储小数表示子弹的设置
        self.y = float(self.bullet_rect.y)
        # 子弹的速度
        self.bullet_speed = 1.5
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
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

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

    def update(self):
        '''向上移动子弹'''
        self.y -= self.bullet_speed
        self.bullet_rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        w = self.screen.blit(self.bullet, self.bullet_rect)
        return w

    def update_bullets(self):
        #更新子弹的位置
        self.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottem < 0:
                self.bullets.remove(bullet)
        # 打印出编组中目前的子弹数量
        print(len(self.bullets))

    def fire_bullet(self):

        now_bullet = self.draw_bullet()
        self.bullets.add(now_bullet)