from cocos import scene
from cocos.layer import Layer, director
from cocos.menu import Menu, MenuItem
from cocos.text import Label

from src.MatchOptions import MatchOptions
from src.colors import *


class OptionsLayer(Layer):
	def __init__(self,director,previousScene):
		super(OptionsLayer, self).__init__()
		self.director = director
		self.menu = OptionsMenu("Options",previousScene,director)
		self.add(self.menu)


class OptionsMenu(Menu):
	def __init__(self, title,previousScene,director):
		super(OptionsMenu, self).__init__(title)
		self.previous = previousScene
		self.options = MatchOptions()

		self.font_title['color'] = green
		self.font_title['font_size'] = 50

		self.font_item['font_size']=14
		self.font_item['color']=white

		self.font_item_selected['font_size']=18
		self.font_item_selected['color']=yellow

		self.menu_items=[
			MenuItem(self.options.playercountDes + "  "+str(self.options.playercount),
			         self.modifiyplayercount),
			MenuItem(self.options.matchtimeDes + "  "+str(self.options.matchtime),
			         self.modifymatchtime),
			MenuItem(self.options.matchcountDes+ "  "+str(self.options.matchcount),
			         self.modifymatchcount),
			MenuItem(self.options.poweruplevelDes+ "  "+str(self.options.poweruplevel),
			         self.modifypoweruplever),
			MenuItem("Back",self.backToPrevious)

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
		director.replace(self.previous)

