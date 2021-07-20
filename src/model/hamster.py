from random import randint, random, randrange, choice
import pygame

class Hamster():
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

        self.x += randint(-1, 1)
        self.y += randint(-1, 1)


def generate_random_color():
    return randrange(2)
