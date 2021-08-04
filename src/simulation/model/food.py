import random
import pygame
from pygame.math import Vector2

from constants.constants import Constants

class Food(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = 20
		
        self.tick_size = 1

        self.position = Vector2(random_initial_position(), random_initial_position())

        self.color = (87, 7, 21)

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), 10)

        self.rect = self.image.get_rect(center = self.position)


    def update(self):
        self.rect.center = self.position


def random_initial_position():
    # Food will spawn between map limits - 10 (so the food doesn't spawn in the edge of the map)
    return random.randrange(Constants.SCREEN_WIDTH - 100)