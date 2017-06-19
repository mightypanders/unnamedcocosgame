from cocos.layer import Layer
from cocos.menu import Menu, MenuItem
from cocos.scene import Scene
from cocos.scenes import SlideInTTransition

from src.colors import *


class SettingsLayer(Layer):
	def __init__(self, director, previousScene):
		super(SettingsLayer, self).__init__()
		self.director = director
		self.previous = previousScene
		self.menu = SettingsMenu(self,"Settings")
		self.add(self.menu)

	def on_quit(self):
		self.backToPrevious()

	def backToPrevious(self):
		destScene = Scene(self.previous)
		self.director.replace(SlideInTTransition(destScene, duration=0.5))


class SettingsMenu(Menu):
	def __init__(self, parent, title=""):
		super(SettingsMenu, self).__init__()
		self.font_title['color'] = green
		self.font_title['font_size'] = 50

		self.font_item['font_size'] = 14
		self.font_item['color'] = white

		self.font_item_selected['font_size'] = 18
		self.font_item_selected['color'] = yellow

		self.menu_items=[
			MenuItem("Nothing to see here yet",self.backToPrevious),
			MenuItem("Back",self.backToPrevious)
		]
		self.create_menu(self.menu_items)

	def backToPrevious(self):
		self.parent.backToPrevious()