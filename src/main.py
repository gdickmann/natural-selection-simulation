import pygame
import time

from constants.constants import Constants
from constants.stages import Stages

from model.food import Food
from model.hamster import Hamster

from settings.settings import Settings


def day_is_over(count):
    return time.time() > count


def calculate_results(hamsters):
    for hamster in hamsters:
        # If a hamster eats 2 (or more) foods,
        if hamster.eaten_food >= 2:
             # ... it has a chance of reproduce
            if hamster.has_chances_of(Constants.REPRODUCE):
                print('A hamster reproduced.')
                new_hamster = Hamster()

                # If a hamster isn't fast already, it will has just a probability of reproduce a faster cub.
                if not hamster.is_fast_hamster and hamster.has_chances_of(Constants.BE_A_FASTER_HAMSTER):
                    print("Fast cub spawned, but the hamster wasn't fast already")
                    new_hamster.speed = pygame.Vector2(Stages.FAST_HAMSTER_SPEED, Stages.FAST_HAMSTER_SPEED)
                    new_hamster.is_fast_hamster = True
                # If a hamster is fast already and can reproduce, it will be automatically a fast hamster.
                elif hamster.is_fast_hamster:
                    print('Fast cub spawned, the hamster was fast already.')
                    new_hamster.speed = pygame.Vector2(Stages.FAST_HAMSTER_SPEED, Stages.FAST_HAMSTER_SPEED)

                hamsters.add(new_hamster)
        if hamster.eaten_food == 0:
            hamster.kill()


def main():
    
    pygame.init()

    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    Settings.set_default_configurations(pygame)

    clock = pygame.time.Clock()
    fps = 60

    running = True
    day = Stages.DAY_SPEED

    # All hamsters!
    hamsters = pygame.sprite.Group(Hamster() for _ in range(Constants.HAMSTERS))
    # and all foods! 
    foods = pygame.sprite.Group(Food() for _ in range(Constants.FOOD))

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        count = time.time() + day
        while not day_is_over(count):

            hamsters.update()

            screen.fill((56, 56, 56))

            hamsters.draw(screen)
            foods.draw(screen)

            pygame.display.flip()
            clock.tick(fps)

            collision = pygame.sprite.groupcollide(hamsters, foods, False, False)
            for hamster, food in collision.items():
                hamster.eat(1)
                food[0].kill()


        calculate_results(hamsters)

    pygame.quit()

if __name__ == "__main__":
    main()
