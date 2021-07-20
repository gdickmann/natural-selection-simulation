import random
import pygame
from pygame.math import Vector2
from constants.constants import Constants
from settings.settings import Settings

pygame.init()

screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
width, height = screen.get_size()

Settings.set_default_configurations(pygame)

clock = pygame.time.Clock()
fps = 60

running = True

class Hamster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.size = 40
        self.color = (255, 255, 255)
        self.tick_size = 1

		# Hamster initial position
        self.position = Vector2(Constants.HAMSTER_X_POSITION, Constants.HAMSTER_Y_POSITION)
        # Hamster speed
        self.speed = Vector2(1.3, 1.3)

        # Set sprite image
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size // 2, self.size // 2),
                           self.size // 2, self.tick_size)

        self.rect = self.image.get_rect(center=self.position)

    def update(self):
        self.speed.rotate_ip(random.gauss(0, 1) * 10)
        self.position += self.speed
        self.rect.center = self.position

        # Hamster random walk. Thanks, Reddit!
        if self.rect.left < 0:
            self.speed.x *= -1
            self.rect.left = 0
        elif self.rect.right > width:
            self.speed.x *= -1
            self.rect.right = width
        if self.rect.top < 0:
            self.speed.y *= -1
            self.rect.top = 0
        elif self.rect.bottom > height:
            self.speed.y *= -1
            self.rect.bottom = height

# All hamsters!
all_hamster = pygame.sprite.Group(Hamster() for _ in range(Constants.HAMSTERS))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_hamster.update()  # updating hamsters

    screen.fill((51, 51, 51))
    all_hamster.draw(screen)  # drawing hamsters on screen

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()