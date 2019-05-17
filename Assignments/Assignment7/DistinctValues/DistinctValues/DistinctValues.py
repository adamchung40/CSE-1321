from array import *

def getValues(array):
	distinct = list()
	for x in array:
		for i in range(len(array)):
			if(x in distinct):
				break
			elif x == array[i]:
				distinct.append(x)
	return distinct

def main():
	newArray = array('i', [0]*10)
	for i in range(len(newArray)):
		num = int(input("Enter a number "))
		newArray[i] = num

	print('Original array: ',end='')
	for x in newArray:
		print(x,end=' ')
	print('\nDistinct array: ',end='')
	for x in (getValues(newArray)):
		print(x,end=' ')
	print()
main()
