#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 6

num = int(input("Enter a number "))
sum = 0

while(num<20 or num>60):
	num = int(input("Invaild input. Try again "))

quit = False
while(not quit):
	for i in range (2,num+1,2):
		sum += i 
	quit = True
print("Sum of the even numbers between 2 and " + str(num) + " is " + str(sum))