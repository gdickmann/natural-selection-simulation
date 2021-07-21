import random
import pygame
from pygame.math import Vector2

from constants.constants import Constants


class Hamster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = 40
		
        self.tick_size = 1

		# Hamster initial position
        self.position = Vector2(Constants.HAMSTER_X_POSITION, Constants.HAMSTER_Y_POSITION)
        # Hamster speed
        self.speed = Vector2(1.3, 1.3)

        self.color = generate_random_color()
        self.eaten_food = True # TODO...

        # Set sprite image
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2), 20)

        self.rect = self.image.get_rect(center = self.position)

    def update(self):
        self.speed.rotate_ip(random.gauss(0, 1) * 10)
        self.position += self.speed
        self.rect.center = self.position

        # Hamster random walk. Thanks, Reddit!
        if self.rect.left < 0:
            self.speed.x *= -1
            self.rect.left = 0
        elif self.rect.right > Constants.SCREEN_WIDTH:
            self.speed.x *= -1
            self.rect.right = Constants.SCREEN_WIDTH
        if self.rect.top < 0:
            self.speed.y *= -1
            self.rect.top = 0
        elif self.rect.bottom > Constants.SCREEN_HEIGHT:
            self.speed.y *= -1
            self.rect.bottom = Constants.SCREEN_HEIGHT

        
    def is_collided_with(self, food):
        return self.rect.colliderect(food.rect)


def generate_random_color():
    is_yellow = random.choice([True, False])
    return (148, 108, 0) if is_yellow else (14, 48, 97)

