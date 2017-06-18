import cocos
from cocos import scene
from cocos.layer import *
from cocos.text import Label


class MainMenu(Layer):
	def __init__(self):
		super(MainMenu,self).__init__()

		pos = (240,240)
		hwlabel = Label(
			text= "das ist ein test",
			position=pos,
			font_size=32,
			bold=True,
			anchor_x="center",
			anchor_y="center",
			color=(255,0,0,255)
						)
		self.add(hwlabel)


director.init()

director.run(scene.Scene(MainMenu()))
