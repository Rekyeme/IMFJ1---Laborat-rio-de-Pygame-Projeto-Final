import pygame
from settings import *


class BG(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/background.png").convert()
        self.rect = self.image.get_rect(topleft=(0, 0))
