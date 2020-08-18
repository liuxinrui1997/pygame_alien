import sys
import pygame
def check_events(ship):
	#响应案件和鼠标事件
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					ship.rect.centerx += 1
					ship.moving_right = True
				elif event.key == pygame.K_LEFT:
					ship.rect.centerx += 1
					ship.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					ship.moving_right = False
				elif event.key == pygame.K_LEFT:
					ship.moving_left = False

def update_screen(ai_settings, ship, screen):
	#每次循环都绘制屏幕
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		#最近绘制的屏幕可见
		pygame.display.flip()