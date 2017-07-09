from cocos.layer import Layer
from cocos.menu import *
from cocos.scene import Scene
from cocos.scenes import *
from pyglet.window.key import symbol_string

from src.MatchOptions import MatchOptions
from src.MenuTemplate import MenuTemplate


class OptionsLayer(Layer):
	is_event_handler = True

	def __init__(self, director, previousScene):
		super(OptionsLayer, self).__init__()
		self.director = director
		self.previous = previousScene
		self.menu = OptionsMenu(self, "Match Options")
		self.add(self.menu)

	def on_quit(self):
		exit()

	def backToPrevious(self):
		destScene = Scene(self.previous)
		self.director.replace(SlideInTTransition(destScene, duration=self.menu.slideDuration))

	def on_key_press(self, key, modifiers):
		if symbol_string(key) == 'LEFT':
			pass
		if symbol_string(key) == "RIGHT":
			pass
		if symbol_string(key) == "ESCAPE":
			self.backToPrevious()
		if symbol_string(key) == "SPACE":
			self.print_options()
		pass

	def print_options(self):
		pass


class OptionsMenu(MenuTemplate):
	def __init__(self, parent, title):
		super(OptionsMenu, self).__init__(parent, title)
		self.options = MatchOptions()

		self.menu_items = [
			MenuItem("PLAY", self.startgame),
			MultipleMenuItem(self.options.playercountDes, self.modifiyplayercount,
			                 self.options.playercountrange),
			MultipleMenuItem(self.options.matchtimeDes, self.modifymatchtime,
			                 self.options.matchtimerange),
			MultipleMenuItem(self.options.matchcountDes, self.modifymatchcount,
			                 self.options.matchcountrange),
			MultipleMenuItem(self.options.poweruplevelDes, self.modifypoweruplevel,
			                 self.options.poweruplevelrange),
			ToggleMenuItem(self.options.suddendeathdes, self.togglesuddendeath,
			               self.options.suddendeath),
			ToggleMenuItem(self.options.randombombsdes, self.randombombstoggle,
			               self.options.randombombs),
			MenuItem("Back", self.backToPrevious)
		]

		self.create_menu(self.menu_items)

	def startgame(self):
		print(self.options.toString())

	def modifiyplayercount(self, idx):
		self.options.playercount = self.options.playercountrange[idx]

	def modifymatchcount(self, idx):
		self.options.matchcount = self.options.matchcountrange[idx]

	def modifymatchtime(self, idx):
		self.options.matchtime = self.options.matchtimerange[idx]

	def modifypoweruplevel(self, idx):
		self.options.poweruplevel = self.options.poweruplevelrange[idx]

	def togglesuddendeath(self, idx):
		self.options.suddendeath = bool(idx)

	def randombombstoggle(self, idx):
		self.options.randombombs = bool(idx)
