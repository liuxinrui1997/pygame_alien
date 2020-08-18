import pygame

class Ship():

	def  __init__(self, screen, ai_settings):
		#初始化飞船并且设置初始位置
		self.screen = screen

		self.ai_settings = ai_settings

		#加载飞船图形
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image, (40,60))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#
		self.center = float(self.rect.centerx)

		#移动标志
		self.moving_right = False
		self.moving_left = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left < self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed_factor

	def blitme(self):
		self.screen.blit(self.image, self.rect)