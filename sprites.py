import pygame
from settings import *
from random import choice, randint


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


class Ground(pygame.sprite.Sprite):
    def __init__(self, groups, scaling_factor):
        super().__init__(groups)

        # Image import and scaling;
        ground_surface = pygame.image.load(
            "../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/ground.png").convert_alpha()
        assert isinstance(scaling_factor, object)
        self.image = pygame.transform.scale(ground_surface,
                                            pygame.math.Vector2(ground_surface.get_size()) * scaling_factor)

        # Position set;
        self.rect = self.image.get_rect(bottomleft=(0, HEIGHT))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # Mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 360 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0

        self.rect.x = round(self.pos.x)


class Plane(pygame.sprite.Sprite):
    def __init__(self, groups, scaling_factor):
        super().__init__(groups)

        # Image import and scaling;
        self.mask = None
        self.import_frames(scaling_factor)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Rect
        self.rect = self.image.get_rect(midleft=(WIDTH / 20, HEIGHT / 2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        # Movement
        self.gravity = 484
        self.direction = 0

    def import_frames(self, scaling_factor):
        self.frames = []
        for i in range(2):
            surf = pygame.image.load(
                f'../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/Plane{i}.png').convert_alpha()
            scaled_surface = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scaling_factor)
            self.frames.append(scaled_surface)

    def applied_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def Jump(self):
        self.direction = - 242

    def animate(self, dt):
        self.frame_index += 21 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def rotate(self, dt):
        rotated_plane = pygame.transform.rotozoom(self.image, -self.direction * 0.10, 1)
        self.image = rotated_plane     
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.applied_gravity(dt)
        self.animate(dt)
        self.rotate(dt)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, groups, scaling_factor):
        super().__init__(groups)

        orientation = choice(("up", "down"))
        surf = pygame.image.load(f"../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/{choice((0, 1))}.png").convert_alpha()
        self.image = pygame.transform.scale(surf, pygame.math.Vector2(surf.get_size()) * scaling_factor)

        x = WIDTH + randint(40, 100)

        if orientation == 'up':
            y = HEIGHT + randint(10, 50)
            self.rect = self.image.get_rect(midbottom=(x, y))
        else:
            y = randint(-50, -10)
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect(midtop=(x, y))

        self.pos = pygame.math.Vector2(self.rect.topleft)

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()
