from xx import Settings
<<<<<<< HEAD:Test/xingxing/Function.py
from random import random
=======
from random import randint
>>>>>>> 64193db9146a9b208b5ce854a47275de0835281f:Test/Function.py


def chenge_bg_color(event=''):
    bg_color = (240, 240, 240)
    if event == 0:
        bg_color = (150, 240, 160)
    elif event == 1:
        bg_color = (240, 120, 160)
    return bg_color


def get_number_xxs_x(ai_settings, image_rect_width):
    available_space_x = ai_settings.screen_wight - (2 * image_rect_width)
    number_xxs_x = int(available_space_x / (2 * image_rect_width))
    return  number_xxs_x


def get_number_xxs_y(ai_settings, image_rect_height):
    available_space_y = ai_settings.screen_height - (3 * image_rect_height)
    number_ssx_y = int(available_space_y / (2 * image_rect_height))
    return number_ssx_y


def create_xx(screen, xxs, xx_number, row_number, ):
    xx = Settings(screen)
    xx_width = xx.rect.width
    xx.x = xx_width + 2 * xx_width * xx_number
    xx.rect.x = xx.x
    xx.rect.y = xx.rect.height + 2 * xx.rect.height * row_number
    xxs.add(xx)


def create_fleet(ai_settings, screen, xxs):
    xx = Settings(screen)
    number_xxs_x = get_number_xxs_x(ai_settings, xx.rect.width)
    row_number = get_number_xxs_y(ai_settings, xx.rect.height)
    # random_number = randint(-10, 10)

    for row_number in range(row_number):

        for number_xxs in range(number_xxs_x):

            create_xx(screen, xxs, number_xxs, row_number, )


def update_xxs(xxs):
    '''更新外星人群中所有外星人的位置'''
    xxs.update()