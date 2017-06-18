from cocos.layer import Layer
from cocos.menu import Menu, CENTER, MenuItem, zoom_in, zoom_out
from cocos.scene import Scene

from src.MatchOptionsLayer import OptionsLayer
from src.colors import *


class MainMenuLayer(Layer):
	def __init__(self,director):
		super(MainMenuLayer, self).__init__()
		self.director = director
		self.menu = MainMenu(self,self.director,"A New Game")
		self.add(self.menu)


class MainMenu(Menu):
	def __init__(self, parent,director,title=""):
		super(MainMenu, self).__init__(title)
		self.parent = parent
		self.director = director
		self.font_title['color'] = green
		self.font_title['font_size'] = 50

		self.font_item['font_size']=14
		self.font_item['color']=white

		self.font_item_selected['font_size']=18
		self.font_item_selected['color']=yellow

		self.menu_halign = CENTER
		self.menu_valign = CENTER

		self.menu_items = [
			MenuItem("New Game", self.newGame),
			MenuItem("Settings", self.settingsOpen),
			MenuItem("Exit", self.exitGame)]
		self.create_menu(self.menu_items)
	def newGame(self):
		pass

	def settingsOpen(self):
		self.director.replace(Scene(OptionsLayer(self.director,self.parent)))
		pass

	def exitGame(self):
		exit()
