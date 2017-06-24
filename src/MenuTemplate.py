from cocos.menu import Menu, CENTER

from src.AudioHandler import Audio
from src.colors import green, white, yellow


class MenuTemplate(Menu):
	is_event_handler = True
	def __init__(self,parent,title=""):
		super(MenuTemplate,self).__init__(title=title)
		self.parent = parent

		self.font_title['color'] = green
		self.font_title['font_size'] = 50

		self.font_item['font_size'] = 14
		self.font_item['color'] = white

		self.font_item_selected['font_size'] = 18
		self.font_item_selected['color'] = yellow

		self.menu_halign = CENTER
		self.menu_valign = CENTER

		self.select_sound = Audio("../ast/menu_selection.ogg")
		self.activate_sound = Audio("../ast/click.wav")

	def backToPrevious(self):
		self.parent.backToPrevious()

	def on_quit(self):
		self.parent.on_quit()
