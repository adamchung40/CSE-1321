from array import *
import random

def arrayMax(array): #Max value in array
	max = array[0]
	for x in array:
		if max < x:
			max = x
	return max
def arrayMin(array): #Min value in array
	min = array[0]
	for x in array:
		if min > x:
			min = x
	return min
def arraySquared(array): #Squaring values in array
	for i in range(len(array)):
		array[i] = array[i]**2
	return array
def arrayReversed(array1): #Reverse the order of the array
	revArray = array('i',[0]*len(array1)) #Creating another w/ same numbers
	for x in range(len(revArray)):
		revArray[x] = array1[x]
	x = len(array1)-1
	for i in range (len(array1)):
		array1[i] = revArray[x]
		x -= 1
	return array1


def main():
	size = 5
	newArray = array('i',[0]*size)

	for i in range(len(newArray)):
		newArray[i] = random.randrange(1,101)

	print("Original array: ", end='')
	for x in newArray:
		print(x, end=' ')

	print("\nMax Value: ", arrayMax(newArray))
	print("Min Value: ", arrayMin(newArray))
	print("Squared array: ", end='')
	for x in arraySquared(newArray):
		print(x,end=' ')
	print("\nReversed array: ", end='')
	for x in arrayReversed(newArray):
		print(x, end=' ')
	print()
main()