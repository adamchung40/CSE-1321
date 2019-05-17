from array import *
import random

def bubbleSort(unsorted):
	swaps = 0
	for i in range(len(unsorted)-1):
			for j in range(0,len(unsorted)-i-1):
				if unsorted[j] > unsorted[j+1]:
					temp = unsorted[j]
					unsorted[j] = unsorted[j+1]
					unsorted[j+1] = temp
					swaps += 1
	print("\nBubble Sorted values:", end ="")
	for x in unsorted:
		print(x, end=' ')
	print("\nBubble Sort Swaps:", swaps)

def insertionSort(unsorted):
	swaps = 0
	for index in range(1,len(unsorted)):
		currentvalue = unsorted[index]
		position = index
		while position>0 and unsorted[position-1]>currentvalue:
			unsorted[position]=unsorted[position-1]
			position = position-1
			swaps += 1
		unsorted[position]=currentvalue

	print("\nInsertion Sorted Values:", end='')
	for x in unsorted:
		print(x, end=' ')
	print("\nInsertion Sort Swaps:", swaps)


def selectionSort(unsorted):
	swaps = 0
	for i in range(len(unsorted)):
		positionOfMin=i
		for j in range(i+1,len(unsorted)):
			if unsorted[positionOfMin]>unsorted[j]:
				positionOfMin = j
		temp = unsorted[i]
		unsorted[i] = unsorted[positionOfMin]
		unsorted[positionOfMin] = temp
		swaps += 1
	print("\nSelection Sorted Values:", end='') #Print Statements
	for x in unsorted:
		print(x, end=' ')
	print("\nSelection Sort Swaps:", swaps)

def main():
	myArray = array("i", [0]*50)
	for i in range(len(myArray)):
		myArray[i] = random.randrange(1,101)

#Print Statements
	print("Array Values: ", end='')
	for x in myArray:
		print(x, end=' ')
	print()
	bubbleSort(myArray[:])
	insertionSort(myArray[:])
	selectionSort(myArray[:])
main()
