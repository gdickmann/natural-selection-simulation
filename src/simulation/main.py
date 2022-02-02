from resource import prlimit
import pygame
import time

from constants.constants import Constants
from constants.stages import Stages

from model.food import Food
from model.hamster import Hamster

from settings.settings import Settings


def print_hamster_history(fast_hamsters, slow_hamsters, green_hamsters, days):
    print('')
    print('======= History of hamsters =======')
    print('Fast hamsters')
    for fast_hamster in fast_hamsters:
        print(str(fast_hamster) + ',')
    print('Slow hamsters')
    for slow_hamster in slow_hamsters:
        print(str(slow_hamster) + ',')
    print('Green hamsters')
    for green_hamster in green_hamsters:
        print(str(green_hamster) + ',')
    

    print('Total days: ' + str(days))
    print('======= History of hamsters =======')


def day_is_over(count):
    return time.time() > count


def set_hamsters_quantity(hamsters, fast_hamster, slow_hamster, green_hamster):
    fast_hamster_count = 0
    slow_hamster_count = 0  
    green_hamster_count = 0

    reproduced_hamsters = 0
    dead_hamsters = 0
    
    for hamster in hamsters:

        reproduce_yellow_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters)
        reproduce_blue_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters)
        reproduce_green_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters)
        
        # In the end of the day, hamsters will be hungry again!
        hamster.eaten_food = 0

        if hamster.is_blue:
            fast_hamster_count += 1
        if hamster.is_yellow:
            slow_hamster_count += 1
        if hamster.is_green:
            green_hamster_count += 1


    print('')
    print(str(reproduced_hamsters) + ' hamster(s) reproduced and ' + str(dead_hamsters) + ' hamster(s) died.')

    print('Fast hamsters: ', str(fast_hamster_count))
    print('Slow hamsters: ', str(slow_hamster_count))
    print('Green hamsters: ', str(green_hamster_count))

    fast_hamster.append(fast_hamster_count)
    slow_hamster.append(slow_hamster_count)
    green_hamster.append(green_hamster_count)


def reproduce_yellow_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters):
    if hamster.eaten_food >= 1:
        if hamster.has_chances_of(Constants.REPRODUCE):
            reproduced_hamsters += 1

            new_hamster = Hamster()

            if hamster.has_chances_of(Constants.BE_A_BLUE_HAMSTER):
                print("Blue hamster spawned by a yellow hamster.")  

                new_hamster.speed = pygame.Vector2(Stages.BLUE_HAMSTER_SPEED, Stages.BLUE_HAMSTER_SPEED)
                new_hamster.color = Constants.BLUE

                new_hamster.is_blue = True
                new_hamster.is_yellow = False

                new_hamster.draw()
                hamsters.add(new_hamster)
            # or a yellow one.
            else:
                print('Yellow hamster spawned by a yellow hamster.')

                new_hamster.speed = pygame.Vector2(Stages.YELLOW_HAMSTER_SPEED, Stages.YELLOW_HAMSTER_SPEED)
                new_hamster.color = Constants.YELLOW

                new_hamster.draw()
                hamsters.add(new_hamster)
                
    elif hamster.eaten_food == 0:
        hamster.kill()
        dead_hamsters += 1


def reproduce_blue_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters):
    if hamster.eaten_food >= 4:
        if hamster.has_chances_of(Constants.REPRODUCE):
            reproduced_hamsters += 1

            new_hamster = Hamster()

            if hamster.has_chances_of(Constants.BE_A_GREEN_HAMSTER):
                print("Green hamster spawned by a blue hamster.")  

                new_hamster.speed = pygame.Vector2(Stages.GREEN_HAMSTER_SPEED, Stages.GREEN_HAMSTER_SPEED)
                new_hamster.color = Constants.GREEN

                new_hamster.is_green = True
                new_hamster.is_yellow = False

                new_hamster.draw()
                hamsters.add(new_hamster)
            # or a yellow one.
            else:
                print('Blue hamster spawned by a blue hamster.')

                new_hamster.speed = pygame.Vector2(Stages.BLUE_HAMSTER_SPEED, Stages.BLUE_HAMSTER_SPEED)
                new_hamster.color = Constants.BLUE

                new_hamster.is_blue = True
                new_hamster.is_yellow = False

                new_hamster.draw()
                hamsters.add(new_hamster)
                
    elif hamster.eaten_food == 0:
        hamster.kill()
        dead_hamsters += 1


def reproduce_green_hamsters(hamster, reproduced_hamsters, dead_hamsters, hamsters):
    if hamster.eaten_food >= 5:
        if hamster.has_chances_of(Constants.REPRODUCE):
            reproduced_hamsters += 1

            new_hamster = Hamster()

            # Green hamster reproduce a green one
            if hamster.is_green:
                print("Green hamster spawned by a green hamster.")  

                new_hamster.speed = pygame.Vector2(Stages.GREEN_HAMSTER_SPEED, Stages.GREEN_HAMSTER_SPEED)
                new_hamster.color = Constants.GREEN

                new_hamster.is_green = True
                
                new_hamster.is_blue = False
                new_hamster.is_yellow = False

                new_hamster.draw()
                hamsters.add(new_hamster) 
                
    elif hamster.eaten_food == 0:
        hamster.kill()
        dead_hamsters += 1


def main():
    pygame.init()
    
    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    Settings.set_default_configurations(pygame)

    clock = pygame.time.Clock()
    fps = 60

    day_speed = Stages.DAY_SPEED
    day = 1

    fast_hamsters = []
    slow_hamsters = []
    green_hamsters = []

    hamsters = pygame.sprite.Group(Hamster() for _ in range(Constants.HAMSTERS))

    while True:
        print('')
        print('Day ' + str(day) + ' started.')
        day += 1

        foods = pygame.sprite.Group(Food() for _ in range(Constants.FOOD))

        count = time.time() + day_speed
        while not day_is_over(count):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print_hamster_history(fast_hamsters, slow_hamsters, green_hamsters, day)

                    pygame.quit()
                    exit()

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

        set_hamsters_quantity(hamsters, fast_hamsters, slow_hamsters, green_hamsters)


if __name__ == "__main__":
    main()