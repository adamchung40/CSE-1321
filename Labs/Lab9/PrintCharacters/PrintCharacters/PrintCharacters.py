#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 9

def printChars(ch1,ch2):
	count = 0
	for i in range (ord(ch1),ord(ch2)+1):
		print(chr(i), end=" ")
		count += 1
		if (count % 5 == 0):
			print()

def main():
	ch1 = input("Enter a character ")
	ch2 = input("Enter a second character ")
	while (ord(ch1) > ord(ch2)):
		print("Start to end character is out of order. Try again (0 to Quit) ")
		print()
		ch1 = input("Enter a character ")
		if ch1 == "0":
			return 
		ch2 = input("Enter a second character ")
		if ch2 == "0":
			return
	print("Start character:", ch1)
	print("End character:", ch2)
	printChars(ch1,ch2)
	print()
main()