from cocos import scene
from cocos.director import director
from cocos.scene import Scene

from src.MainMenuLayer import MainMenuLayer


def startroutine():
    director.init()
    print("director started")
    director.run(Scene(MainMenuLayer(director)))

if __name__ == '__main__':
    startroutine()