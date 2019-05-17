#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 10

class RectangleClass:
	def __init__(self,height = 1,width = 1):
		self.height = height
		self.width = width

	#Class methods
	def getArea(self):
		return self.height * self.width
	def getPerimeter(self):
		return 2*self.height + 2*self.width
	def getHeight(self):
		return self.height
	def getWidth(self):
		return self.width