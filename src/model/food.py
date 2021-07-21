import random
import pygame
from pygame.math import Vector2

from constants.constants import Constants

class Food(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = 13
		
        self.tick_size = 1

		# Hamster initial position
        self.position = Vector2(random_initial_position(), random_initial_position())
        # Hamster speed

        self.color = (87, 7, 21)

        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), 13)

        self.rect = self.image.get_rect(center = self.position)


    def update(self):
        self.rect.center = self.position


def random_initial_position():
    return random.randrange(680)