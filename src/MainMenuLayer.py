from cocos.layer import Layer
from cocos.menu import Menu, CENTER, MenuItem
from cocos.scene import Scene
from cocos.scenes import *

from src.MatchOptionsLayer import OptionsLayer
from src.MenuTemplate import MenuTemplate
from src.SettingsLayer import SettingsLayer
from src.colors import *


class MainMenuLayer(Layer):
	is_event_handler = True

	def __init__(self, director, previousScene):
		super(MainMenuLayer, self).__init__()
		self.director = director
		self.menu = MainMenu(self, title="A New Game")
		self.add(self.menu)

	def on_key_press(self, key, modifiers):
		pass

	def newGame(self):
		destScene = Scene(OptionsLayer(self.director, self.parent))
		self.changeScene(destScene)

	def settingsOpen(self):
		destScene = Scene(SettingsLayer(self.director, self.parent))
		self.changeScene(destScene)

	def changeScene(self, destScene):
		self.director.replace(SlideInBTransition(destScene, duration=0.5))

	def on_quit(self):
		exit()


class MainMenu(MenuTemplate):
	def __init__(self, parent, title):
		super(MainMenu, self).__init__(parent,title)

		self.menu_items = [
			MenuItem("New Game", self.parent.newGame),
			MenuItem("Settings", self.parent.settingsOpen),
			MenuItem("Exit", self.parent.on_quit)]

		self.create_menu(self.menu_items)

