from array import *

def count(newArray):
	distinct = list()
	for x in newArray:
		if(x in distinct):
			print(end='')
		else:
			distinct.append(x)
			count = 0
			for i in range(len(newArray)):
				if x == newArray[i]:
					count += 1
			if count == 1:
				print(x, 'occurred', count, "time")
			else:
				print(x, 'occurred', count, "times")
				

def main():
	newArray =  array('i', [0]*10)

	for i in range(len(newArray)):
		num = int(input('Enter 10 numbers '))
		newArray[i] = num
	print()
	count(newArray)
main()
