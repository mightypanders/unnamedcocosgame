from src import Movable
from src.constants import DEFAULTSPEED


class Player(Movable):
	def __init__(self, name, x, y, hitpoints, controlled):
		super(Player, self).__init__(name,x,y,hitpoints,controlled)
		self.speed = DEFAULTSPEED

