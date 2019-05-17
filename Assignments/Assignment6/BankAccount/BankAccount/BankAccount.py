class bankAccount:
#Default Contructor
	def __init__(self,id = 0, balance = 0.0, annualInterestRate = .00, dateCreated = ""):
		self.id = id
		self.balance = balance
		self.annualInterestRate = annualInterestRate
		self.dateCreated = dateCreated

#ID (Getter/Setter)
	def getId(self):
		return self.id
	def setId(self, id):
		self.id = id
#Balance (Getter/Setter)
	def getBalance(self):
		return self.balance
	def setBalance(self,balance):
		self.balance = balance
#AnnualInterestRate (Getter/Setter)
	def getAnnualInterestRate(self):
		return self.annualInterestRate
	def setAnnualInterestRate(self,annualInterestRate):
		self.annualInterestRate = annualInterestRate
#Date when Account created
	def getDateCreated(self):
		return self.dateCreated
	def getMonthlyInterestRate(self):
		monthlyInterestRate = (self.annualInterestRate / 12) * 100
		return str(round(monthlyInterestRate,2))+"%"
	def getMonthlyInterest(self):
		monthlyInterestRate = (self.annualInterestRate / 12)
		getMonthlyInterest = self.balance * monthlyInterestRate
		return "$"+ str(round(getMonthlyInterest,2))
	def withdraw(self,withdraw):
		self.balance -= withdraw
		return self.balance
	def deposit(self,deposit):
		self.balance += deposit
		return self.balance
	def toStrings(self):
		return print("Account ID:", self.id, 
			   "\nAccount Balance:", self.balance, 
			   "\nInterest Rate:", self.annualInterestRate * 100, "\b%"
			   "\nDate Opened:", self.dateCreated)