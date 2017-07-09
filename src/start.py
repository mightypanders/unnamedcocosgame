import sys

sys.path.append("/home/markus/development/unnamedgame")
from cocos.audio.pygame import mixer
from cocos.director import director
from cocos.scene import Scene

from src.MainMenuLayer import MainMenuLayer


def startroutine():
	director.init()
	mixer.init()
	print("director started")
	director.run(Scene(MainMenuLayer(director, None)))


if __name__ == '__main__':
	startroutine()
