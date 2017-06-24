from cocos.layer import Layer
from cocos.menu import *
from cocos.scene import Scene
from cocos.scenes import *
from pyglet.window.key import symbol_string

from src.AudioHandler import Audio
from src.MatchOptions import MatchOptions
from src.MenuTemplate import MenuTemplate
from src.colors import *


class OptionsLayer(Layer):
	is_event_handler = True

	def __init__(self, director, previousScene):
		super(OptionsLayer, self).__init__()
		self.director = director
		self.previous = previousScene
		self.menu = OptionsMenu(self, "Options")
		self.add(self.menu)

	def on_quit(self):
		exit()

	def backToPrevious(self):
		destScene = Scene(self.previous)
		self.director.replace(SlideInTTransition(destScene, duration=0.5))

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
		super(OptionsMenu, self).__init__(parent,title)
		self.options = MatchOptions()

		self.menu_items = [
			MultipleMenuItem(self.options.playercountDes, self.modifiyplayercount,
			                 self.options.playercount),
			MultipleMenuItem(self.options.matchtimeDes, self.modifymatchtime,
			                 self.options.matchtime),
			MultipleMenuItem(self.options.matchcountDes, self.modifymatchtime,
			                 self.options.matchcount),
			MultipleMenuItem(self.options.poweruplevelDes, self.modifypoweruplever,
			                 self.options.poweruplevel),
			MultipleMenuItem(self.options.poweruplevelDes, self.poweruplevelmodif,
			                 self.options.poweruplevel),
			ToggleMenuItem(self.options.suddendeathdes, self.togglesuddendeath,
			               self.options.suddendeath),
			ToggleMenuItem(self.options.randombombsdes, self.randombombstoggle,
			               self.options.randombombs),
			MenuItem("Back", self.backToPrevious)
		]

		self.create_menu(self.menu_items)

	def modifiyplayercount(self, idx):
		pass
	def modifymatchcount(self, idx):
		pass

	def modifymatchtime(self, idx):
		pass

	def modifypoweruplever(self, idx):
		pass

	def togglesuddendeath(self, idx):
		# if self.options.suddendeath == False:
		# 	self.options.suddendeath = True
		# elif self.options.suddendeath == True:
		# 	self.options.suddendeath = False
		pass

	def randombombstoggle(self, idx):
		# if self.options.randombombs == False:
		# 	self.options.randombombs = True
		# elif self.options.randombombs == True:
		# 	self.options.randombombs = False
		pass

	def poweruplevelmodif(self, idx):
		pass
