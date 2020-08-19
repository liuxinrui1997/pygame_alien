import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_settings, screen, ship):
		super(Bullet, self).__init__()
		self.screen = screen

		#at(0,0) create a bullet
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
			ai_settings.bullet_height)
		#set position
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_spped_factor


		