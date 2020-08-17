import pygame

class Ship():

	def  __init__(self, screen):
		#初始化飞船并且设置初始位置
		self.screen = screen

		#加载飞船图形
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image, (40,60))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#移动标志
		self.moving_right = False

	def update(self):
		if self.moving_right:
			self.rect.centerx += 1
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)