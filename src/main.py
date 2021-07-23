import pygame

from constants.constants import Constants
from model.food import Food
from model.hamster import Hamster

from settings.settings import Settings

pygame.init()

screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

Settings.set_default_configurations(pygame)

clock = pygame.time.Clock()
fps = 60

running = True

# All hamsters!
all_hamsters = pygame.sprite.Group(Hamster() for _ in range(Constants.HAMSTERS))
# and all foods! 
all_foods = pygame.sprite.Group(Food() for _ in range(Constants.FOOD))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_hamsters.update()

    screen.fill((56, 56, 56))

    all_hamsters.draw(screen)
    all_foods.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

    collision = pygame.sprite.groupcollide(all_hamsters, all_foods, False, False)
    for hamster, food in collision.items():
        hamster.eat(1)
        food[0].kill()

pygame.quit()