from cocos.layer import Layer
from cocos.menu import Menu, MenuItem
from cocos.scene import Scene
from cocos.scenes import *

from src.MatchOptions import MatchOptions
from src.colors import *


class OptionsLayer(Layer):
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


class OptionsMenu(Menu):
	def __init__(self, parent, title=""):
		super(OptionsMenu, self).__init__(title)
		self.options = MatchOptions()

		self.font_title['color'] = green
		self.font_title['font_size'] = 50

		self.font_item['font_size'] = 14
		self.font_item['color'] = white

		self.font_item_selected['font_size'] = 18
		self.font_item_selected['color'] = yellow

		self.menu_items = [
			MenuItem(self.options.playercountDes + "  " + str(self.options.playercount),
			         self.modifiyplayercount),
			MenuItem(self.options.matchtimeDes + "  " + str(self.options.matchtime),
			         self.modifymatchtime),
			MenuItem(self.options.matchcountDes + "  " + str(self.options.matchcount),
			         self.modifymatchcount),
			MenuItem(self.options.poweruplevelDes + "  " + str(self.options.poweruplevel),
			         self.modifypoweruplever),
			MenuItem("Back", self.backToPrevious)
		]

		self.create_menu(self.menu_items)

	def modifiyplayercount(self):
		pass

	def modifymatchcount(self):
		pass

	def modifymatchtime(self):
		pass

	def modifypoweruplever(self):
		pass

	def backToPrevious(self):
		self.parent.backToPrevious()

	def on_quit(self):
		self.parent.on_quit()
