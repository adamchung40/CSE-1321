#Class:	CSE 1321L
#Section: 16          
#Term: Spring 2019
#Instructor: Kristin Hegna 
#Name: Adam Chung    
#Lab#: 2

#First circle
x1 = int(input("Enter the x-value for the center point for the first circle "))
y1 = int(input("Enter the y-value for the center point for the first circle "))
r1 = float(input("Enter the radius for the first circle "))
center1 = (x1,y1)
#Second circle
x2 = int(input("Enter the x-value for the center point for the second circle "))
y2 = int(input("Enter the y-value for the center point for the second circle "))
r2 = float(input("Enter the radius for the second circle "))
center2 = (x2,y2)

distance = (((x2-x1)**2+(y2-y1)**2)**(.50))

#Judgement
if (distance > (r1 + r2)):
	judgement = "Circle 2 is completely outside circle 1 "
elif (distance < (r1 - r2)):
	judgement = "Circle 2 is completely inside circle 1 "
else:
	judgement = "Circle 2 is overlapping with circle 1 "

#Print Statements
print("Circle 1 center is: ", center1)
print("Circle 1 radius is: ", r1)
print("Circle 2 center is: ", center2)
print("Circle 2 radius is: ", r2)
print("Judgement: ", judgement)