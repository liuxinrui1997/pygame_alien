import sys
import pygame
from pygame.sprite import Group
#倒入设置文件
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
	#初始化并创建一个屏幕对象
	pygame.init()
	#从设置里导入
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	#
	pygame.display.set_caption("Alien Invasion")

	#创建飞船
	ship = Ship(screen, ai_settings)

	#设置背景颜色
	bg_color = (230, 50, 100)

	#创建组
	bullets = Group()

	#开始游戏主循环
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, ship, screen, bullets)


run_game()