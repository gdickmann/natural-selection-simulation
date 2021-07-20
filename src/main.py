# Author: Biscoitinho
import pygame
from constants.constants import Constants
from settings.settings import Settings

pygame.init()

screen = pygame.display.set_mode((Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH))
screen.fill((61, 115, 75))

Settings.set_default_configurations(pygame)

x = Constants.HAMSTER_X_POSITION
y = Constants.HAMSTER_Y_POSITION

width = Constants.HAMSTER_WIDTH
height = Constants.HAMSTER_HEIGHT

speed = Constants.HAMSTER_SPEED

running = True

while running:
	pygame.time.delay(10)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > 0:
		x -= speed
		
	if keys[pygame.K_RIGHT] and x < Constants.SCREEN_WIDTH - width:
		x += speed
		
	if keys[pygame.K_UP] and y > 0:
		y -= speed
		
	if keys[pygame.K_DOWN] and y < Constants.SCREEN_HEIGHT - height:
		y += speed
		
	screen.fill((61, 115, 75))
	
	pygame.draw.rect(screen, (74, 0, 7), (x, y, width, height))
	
	pygame.display.update()

pygame.quit()
