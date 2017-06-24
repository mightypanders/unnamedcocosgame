from cocos.layer import Layer
from cocos.menu import Menu, MenuItem
from cocos.scene import Scene
from cocos.scenes import SlideInTTransition

from src.MenuTemplate import MenuTemplate
from src.colors import *


class SettingsLayer(Layer):
	def __init__(self, director, previousScene):
		super(SettingsLayer, self).__init__()
		self.director = director
		self.previous = previousScene
		self.menu = SettingsMenu(self, "Settings")
		self.add(self.menu)

	def on_quit(self):
		self.backToPrevious()

	def backToPrevious(self):
		destScene = Scene(self.previous)
		self.director.replace(SlideInTTransition(destScene, duration=0.5))


class SettingsMenu(MenuTemplate):
	def __init__(self, parent, title):
		super(SettingsMenu, self).__init__(parent,title)

		self.menu_items = [
			MenuItem("Nothing to see here yet", self.backToPrevious),
			MenuItem("Back", self.backToPrevious)
		]
		self.create_menu(self.menu_items)

