#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

num = int(input("Enter a five digit number "))
temp = num
rev = 0

while temp != 0:
	rev = (rev * 10) + (temp % 10)
	temp //= 10
if (num == rev):
	print("Number is palindrome")
else:
	print("Number is not palindrome")