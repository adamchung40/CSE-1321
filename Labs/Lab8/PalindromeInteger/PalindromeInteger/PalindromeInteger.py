#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 8

def reverse(num):
	temp = num
	rev = 0
	while temp != 0:
		rev = (rev * 10) + (temp % 10)
		temp //= 10
	return rev

def isPalindorme(num, rev_num):
	if (num == rev_num):
		judgement = "Palindrome"
	else:
		judgement = "Not Palindrome"
	return judgement

def main():
	num = int(input("Enter a number "))
	print("Entered value: ", num)
	print("Judgement: ", isPalindorme(num,reverse(num)))
main()