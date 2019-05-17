#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 7

num = int(input("Enter a number "))
symbol = input("Enter a symbol ")


for i in range (1,num+1):
    for j in range (1,num+1):
        print(symbol, end="")
    print()