#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

for i in range (7,0,-1):
    print(' ' * ((7-i)), end="")
    for j in range(1, i):
        print(j, end="")
    print()