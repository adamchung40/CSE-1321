class counterClass:
	def __init__(self,counter = 0):
		self.counter = counter

	def increment(self):
		self.counter += 1
		return self.counter
	def getValue(self):
		return self.counter

