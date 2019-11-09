import pygame


def image(screen):
    image = pygame.image.load('../images/1.bmp')
    image_rect = image.get_rect()
    screen_rect = screen.get_rect()
    image_rect.centerx = screen_rect.centerx
    image_rect.centery = screen_rect.centery
    screen.blit(image, image_rect)