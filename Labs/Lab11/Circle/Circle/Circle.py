class circle:
	def __init__(self,radius = 1.0):
		self.radius = radius

	def getRadius(self):
		return self.radius
	def setRadius(self,radius):
		self.radius = radius
	def getArea(self):
		return (self.radius)**2 * 3.14
	def getPerimeter(self):
		return 2 * 3.14 * self.radius
	def toString(self):
		return print("The circle has radius", self.radius)