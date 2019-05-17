#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

#Top half
for row in range(9,0,-2):
    print(' ' * ((9-row)//2), end="")
    for star in range(row):
        print("*", end = "")
    print()
#Bottom Half
for row in range(3,10,2):
    print(' ' * ((9-row)//2), end="")
    for star in range(row):
        print("*", end = "")
    print()

