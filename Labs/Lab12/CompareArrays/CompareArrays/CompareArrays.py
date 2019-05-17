from array import *

def compare(array1,array2):
	if array1 == array2:
		return "The array are identical"
	else:
		return "The array are not identical"

def main():
	size = int(input("Enter the size of the array "))

	firstArray = array('i', [0]*size) #First Array
	for i in range(len(firstArray)):
		num = int(input("Enter a number for the first array "))
		firstArray[i] = num
	print()
	secondArray = array('i', [0]*size) #Second Array
	for i in range(len(secondArray)):
		num = int(input("Enter a number for the second array "))
		secondArray[i] = num
	print()
#Print Statements
	print("Array size:", size)
	print("First Array: ", end="")
	for x in firstArray:
		print(x, end=' ')
	print("\nSecond Array: ", end="")
	for x in secondArray:
		print(x, end=' ')
	print("\nJudgement:", compare(firstArray,secondArray))
main()
