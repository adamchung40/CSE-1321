#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 9

def sumOfDigits(num):
	sum = 0
	while num != 0:
		sum += num % 10
		num //= 10
	return sum

def main():
    num = int(input("Enter a number "))
    print("You entered: ", num)
    print("Sum of digits: ", sumOfDigits(num))
main()