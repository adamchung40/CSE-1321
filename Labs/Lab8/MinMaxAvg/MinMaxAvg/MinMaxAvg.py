#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 8

def max(num1, num2, num3):
	max = num1
	if (max < num2):
		max = num2
	if (max < num3):
		max = num3
	return max

def min(num1, num2, num3):
	min = num1
	if (min > num2):
		min = num2
	if (min > num3):
		min = num3
	return min

def avg(num1, num2, num3):
	avg = int((num1 + num2 + num3)/3)
	return avg

def main():
	num1 = int(input("Enter a number "))
	num2 = int(input("Enter a second number "))
	num3 = int(input("Enter a  third number "))
	print("You entered : ", end='')
	print(num1, end=", ")
	print(num2, end=", ")
	print(num3)
	print("Max value: ", max(num1,num2,num3))
	print("Min value: ", min(num1,num2,num3))
	print("Average value: ", avg(num1,num2,num3))
main()