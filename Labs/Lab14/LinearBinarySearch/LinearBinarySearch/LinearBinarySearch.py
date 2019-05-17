from array import *
import random
def linearSearch(myArray,target):
	count = 0
	for i in range(len(myArray)):
		if myArray[i] != target:
			count += 1
		elif myArray[i] == target:
			count += 1
			return count
	return "Target value was not found"
def binarySearch(myArray, target):
	count = 0
	first = 0
	last = len(myArray)
	found = False
	while not found:
		midpoint = (first + last) // 2
		if myArray[midpoint] == target:
			found = True
			count += 1
			return count
		else:
			count += 1
			if myArray[midpoint] > target:
				last = midpoint - 1
			elif myArray[midpoint] < target:
				first = midpoint + 1
	return "Target value was not found"
def main():
	length = int(input("Enter the length of the array "))
	myArray = array('i', [0]*length)
	for i in range(len(myArray)):
		#num = random.randrange(50)
		num = int(input("Enter a number for index " + str(i) + " → "))
		myArray[i] = num
	target = int(input("Enter your target value: "))
	print()
#Print Statement
	print("Array Values: ", end="")
	for x in myArray:
		print(x, end=' ')
	print()
	print("Target value:", target, "\n")
	print("Linear Search Comparisons:", linearSearch(myArray,target))
	print("Binary Search Comparisons:", binarySearch(myArray,target))
main()
