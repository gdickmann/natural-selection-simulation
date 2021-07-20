from random import randrange
import pygame
from pygame import math
from constants.constants import Constants

class Hamster(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

        # Generate random initial color for hamster
        self.color = generate_random_color()
        # Did the hamster already eat?
        self.eaten_food = True # TODO...


    def draw(self):
        pygame.draw.rect(self.game.screen,
                         (122, 0, 0),
                         pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += 0.05
        

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)


def generate_random_color():
    return randrange(2)