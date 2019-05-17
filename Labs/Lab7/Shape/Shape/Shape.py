#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 7

for i in range(1,17,2):
    print(" " * (7-i//2), end="")
    for j in range(1,i+1):
        print("*", end ="")
    print()