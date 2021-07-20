# Author: Biscoitinho
import pygame
from constants.constants import Constants
from model.hamster import Hamster
from settings.settings import Settings

class Game:
	Settings.set_default_configurations(pygame)

	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH))
		self.screen.fill((61, 115, 75))
		self.clock = pygame.time.Clock()

		x = Constants.HAMSTER_X_POSITION
		y = Constants.HAMSTER_Y_POSITION

		width = Constants.HAMSTER_WIDTH
		height = Constants.HAMSTER_HEIGHT

		speed = Constants.HAMSTER_SPEED

		hamster = Hamster(self, width / 2, height - 20)

		running = True
		while running:
			pygame.time.delay(10)
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False

			pygame.display.flip()
			self.clock.tick(60)
			self.screen.fill((61, 115, 75))

			hamster.draw()
			
		pygame.quit()

if __name__ == '__main__':
	game = Game()