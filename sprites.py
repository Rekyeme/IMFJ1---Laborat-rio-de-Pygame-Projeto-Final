import pygame
from settings import *


class BG(pygame.sprite.Sprite):
    def __init__(self, groups, scaling_factor):
        super().__init__(groups)
        bg_image = pygame.image.load("../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/background.png").convert()

        f_HEIGHT = bg_image.get_height() * scaling_factor
        f_WIDTH = bg_image.get_width() * scaling_factor
        f_sized_image = pygame.transform.scale(bg_image, (f_WIDTH, f_HEIGHT))

        self.image = pygame.Surface((f_WIDTH * 2, f_HEIGHT))
        self.image.blit(f_sized_image, (0, 0))
        self.image.blit(f_sized_image, (f_WIDTH, 0))

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 300 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)