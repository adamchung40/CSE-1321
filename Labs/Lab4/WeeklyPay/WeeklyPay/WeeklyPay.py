#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

hours = int(input("How many hour did you work? "))
std_hours = 40


if hours > 40:
    overtime = (hours - 40)*15 + (std_hours*10)
    print(overtime)
else:
    print(hours*10)