import pygame
import sys
import time
from settings import *
from sprites import BG


class Program:

    # Display and Clock setup;
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("")
        self.clock = pygame.time.Clock()

        # Sprite Group
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Sprite Configuration
        BG(self.all_sprites)

    # Program main loop;
    def run(self):
        last_time = time.time()
        while True:

            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Updates the display and limits the frame-rate;
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    program = Program()
    program.run()
