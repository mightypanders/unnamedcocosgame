class MatchOptions():
	def __init__(self):
		self.matchcountrange = ['1', '2', '3', '4', '5']
		self.matchcount = int(self.matchcountrange[0])
		self.matchcountDes = "Number of Matches till Win "

		self.playercountrange = ['2', '3', '4', '5', '6', '7', '8']
		self.playercount = int(self.playercountrange[0])
		self.playercountDes = "Number of Players "

		self.poweruplevelrange = ['1', '2', '3', '4', '5']
		self.poweruplevel = int(self.poweruplevelrange[0])
		self.poweruplevelDes = "Level of Powerup Spawns (0-5) "

		self.matchtimerange = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		self.matchtime = int(self.matchtimerange[0])
		self.matchtimeDes = "Duration of Matches "

		self.startpowerups = []
		self.mutators = []

		self.suddendeathdes = "Sudden Death "
		self.suddendeath = True

		self.randombombsdes = "Random Bombs in Sudden Death "
		self.randombombs = False

	def toString(self):
		outstring = (""
		             + ("PlayerNumber: " + str(self.playercount) + "\n")
		             + ("MatchTime: " + str(self.matchtime) + "\n")
		             + ("MatchNumber: " + str(self.matchcount) + "\n")
		             + ("PowerUpLevel: " + str(self.poweruplevel) + "\n")
		             + ("Sudden Death: " + str(self.suddendeath) + "\n")
		             + ("Random Bombs: " + str(self.randombombs) + "\n")
		             )
		return outstring
