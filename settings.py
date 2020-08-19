class Settings():
	#储存所有设置的类	

	def __init__(self):
		#初始化游戏设置
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230, 50, 100)
		#ship setting
		self.ship_speed_factor = 1.5

		#bullet
		self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60) ###似乎不加括号也行