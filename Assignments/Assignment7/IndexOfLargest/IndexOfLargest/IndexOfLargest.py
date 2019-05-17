from array import *

def findIndex(array):
	max = array[0]
	index = 0
	for i in range(len(array)):
		if max < array[i]:
			max = array[i]
			index = i
	return index

def main():
	newArray = array('i',[0]*5)
	for i in range(len(newArray)):
		num = int(input('Enter a number '))
		newArray[i] = num
	print('\nEntered integers: ', end='')
	for x in newArray:
		print(x,end=' ')
	print()
	print('Index of the largest value is', findIndex(newArray))
main()