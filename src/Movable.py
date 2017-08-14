class Movable():
	def __init__(self,name,x,y,hitpoints,controlled):
		self.name = name
		self.pos = (x,y)
		self.x = self.pos[0]
		self.y = self.pos[1]
		self.hitpoints = hitpoints
		self.controlled = controlled
