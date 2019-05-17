#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

#Declaring variables
sumDigits = 0
num = int(input("Entered number: "))

#Calculations 
while num != 0:
   sumDigits += num % 10
   num //= 10

#Print Statement
print("Sum of digits: ", int(sumDigits))