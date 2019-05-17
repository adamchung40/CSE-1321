class quadraticEquation:
	import math
	def __init__(self, a,b,c):
		self.A = a
		self.B = b
		self.C = c
	#Variables Getters
	def getA(self):
		return self.A
	def getB(self):
		return self.B
	def getC(self):
		return self.C
	#Quadratic Equation
	def getDiscriminant(self):
		return (self.B)**2 - 4*(self.A)*(self.C)

	def getRoot1(self):
		disc = (self.B)**2 - 4*(self.A)*(self.C)
		if disc < 0:
			return print("Root 1 is Undefined")
		else:
			root = ( -(self.B) + (disc)**(1/2) ) / (2*self.A)
			return print("Root 1 =", root)
	
	def getRoot2(self):
		disc = (self.B)**2 - 4*(self.A)*(self.C)
		if disc < 0:
			return print("Root 2 is Undefined")
		else:
			root = ( -(self.B) - (disc)**(1/2) ) / (2*self.A)
			return print("Root 2 =", root)
