#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 10

class Stocks:
#Default Contructor
	def __init__(self, symbol = "", Name = "", previousClosingPrice = 0.0, currentPrice = 0.0):
		self.Symbol = symbol
		self.Name = Name
		self.previousClosingPrice = previousClosingPrice
		self.currentPrice = currentPrice

	#Constructors Methods
	def getName(self):
		return self.Name
	def getSymbol(self):
		return self.Symbol
	def setClosingPrice(self, previousClosingPrice):
		self.previousClosingPrice = previousClosingPrice
	def setCurrentPrice(self, currentPrice):
		self.currentPrice = currentPrice
	def getChangePercent(self):
		changePercent = (self.currentPrice - self.previousClosingPrice) / self.currentPrice * 100
		return int(changePercent)
	def toString(self):
		return print("\t", self.Name, "\b's closing price is $", self.previousClosingPrice)
