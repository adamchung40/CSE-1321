#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 6

#Even numbers between 50 to 100
num = 50
print("Even numbers between 50 to 100: ", end="")
while (num <= 100 ): 
	print(num, end=", ")
	num += 2
print()

#Odd numbers between 50 to 100
num = 50
print("Odd number between 50 to 100: ", end="")
while (num <= 99 ): 
	num += 1
	if (num % 2 == 0):
		continue
	print(num, end=", ")
	