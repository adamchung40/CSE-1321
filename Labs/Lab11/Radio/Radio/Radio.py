class radio:
	def __init__(self,station = 1, volume = 1, boolean = False):
		self.station = station
		self.volume = volume
		self.boolean = boolean

	def getStation(self):
		return self.station
	def getVolume(self):
		return self.volume
	def turnOn(self):
		self.boolean = True
		return self.boolean
	def turnOff(self):
		self.boolean = False
		return self.boolean
	def stationUp(self,station):
		if self.boolean == False:
			return 
		else:
			self.station += station 
			return self.station
	def stationDown(self,station):
		if self.boolean == False:
			return 
		else:
			self.station -= station
			return self.station
	def volumeUp(self,volume):
		if self.boolean == False:
			return
		else:
			self.volume += volume
			return self.volume
	def volumeDown(self,volume):
		if self.boolean == False:
			return 
		else:
			self.volume -= volume
			return self.volume
	def toString(self):
		if self.boolean == False:
			return print("\tThe radio is off.\n")
		else:
			return print("\tThe radio station is", self.station, "and the volume level is", self.volume, "\n")