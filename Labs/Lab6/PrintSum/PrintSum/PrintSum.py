#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 6

num = int(input("Enter a number between 1 and 100: "))
while (num < 0 or num > 100):
	num = int(input("Invalid input. Try again: "))
if (num >= 1 or num <= 100):
	total = 0
	for count in range(1,num+1):
		total += count
print(total)