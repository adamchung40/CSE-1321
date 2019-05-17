from Counter import counterClass 
import random

def main():
	heads = counterClass()
	tails = counterClass()
	for i in range (100):
		j = random.randrange(1,3)
		if j == 1:
			heads.increment()
		else:
			tails.increment()
	print("Number of heads:", heads.getValue())
	print("Number of tails:", tails.getValue())
main()
